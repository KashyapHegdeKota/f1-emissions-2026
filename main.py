from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import boto3
from geopy.distance import great_circle
from mangum import Mangum
from decimal import Decimal

# 1. Define the App with the correct root path
app = FastAPI(
    title="PaddockJet: F1 Logistics API",
    root_path="/default" 
)

# 2. ENABLE CORS (The fix for your error)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows localhost:3000 to talk to AWS
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, OPTIONS, GET
    allow_headers=["*"],
)

# 3. Setup Database
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('f1_emissions')

def get_race_data(race_id: str):
    response = table.get_item(Key={'race_id': race_id})
    item = response.get('Item')
    if not item:
        raise HTTPException(status_code=404, detail=f"Race ID '{race_id}' not found")
    return item

@app.post("/calculate_logistics")
def calculate_logistics(origin_race_id: str, dest_race_id: str, cargo_kg: float):
    # Fetch Data
    origin = get_race_data(origin_race_id)
    dest = get_race_data(dest_race_id)

    # Extract Coords
    origin_coords = (float(origin['latitude']), float(origin['longitude']))
    dest_coords = (float(dest['latitude']), float(dest['longitude']))

    # Math
    distance_km = great_circle(origin_coords, dest_coords).kilometers
    flight_time_hours = (distance_km / 850) + 0.5
    co2_kg = (cargo_kg / 1000) * distance_km * 0.5

    return {
        "route": {
            "from": origin['circuit_name'],
            "to": dest['circuit_name'],
            "airports": f"{origin['airport_code']} -> {dest['airport_code']}"
        },
        "logistics": {
            "distance_km": round(distance_km, 2),
            "estimated_flight_time": f"{int(flight_time_hours)}h {int((flight_time_hours % 1) * 60)}m",
            "cargo_weight_kg": cargo_kg
        },
        "environmental_impact": {
            "co2_emissions_kg": round(co2_kg, 2),
            "note": "Based on Boeing 777F fuel burn profile"
        }
    }
    
@app.get("/{full_path:path}")
def catch_all(full_path: str, request: Request):
    return{
        "error":"Path not found",
        "path":full_path,
        "root_path": request.scope.get("root_path")
    }
handler = Mangum(app)
