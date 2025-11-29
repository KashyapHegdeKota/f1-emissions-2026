from fastapi import FastAPI, HTTPException
import boto3
from geopy.distance import great_circle
from mangum import Mangum
from decimal import Decimal

app = FastAPI(title="PaddockJet: F1 Logistics API")

# 1. Connect to DynamoDB
# Ensure region matches where you made the table (e.g., us-east-1)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('f1_emissions')

def get_race_data(race_id: str):
    """Helper function to fetch a race from DynamoDB"""
    response = table.get_item(Key={'race_id': race_id})
    item = response.get('Item')
    if not item:
        raise HTTPException(status_code=404, detail=f"Race ID '{race_id}' not found")
    return item

@app.get("/")
def root():
    return {"message": "PaddockJet Logistics API is Online"}

@app.post("/calculate_logistics")
def calculate_logistics(origin_race_id: str, dest_race_id: str, cargo_kg: float):
    
    # 2. Fetch Data from your DynamoDB
    origin = get_race_data(origin_race_id)
    dest = get_race_data(dest_race_id)

    # 3. Extract Coordinates
    # DynamoDB returns Decimals, geopy needs floats
    origin_coords = (float(origin['latitude']), float(origin['longitude']))
    dest_coords = (float(dest['latitude']), float(dest['longitude']))

    # 4. Do the Aviation Math
    # Calculate Great Circle Distance (The path planes actually fly)
    distance_km = great_circle(origin_coords, dest_coords).kilometers
    
    # Estimate Flight Time (Boeing 777F cruises at ~850 km/h + 30 mins taxi/takeoff)
    flight_time_hours = (distance_km / 850) + 0.5
    
    # Estimate Carbon Emissions
    # Approx 500g CO2 per Metric Tonne per km (simplified air freight formula)
    # cargo_tonnes = cargo_kg / 1000
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

# This is the entry point for AWS Lambda
handler = Mangum(app)