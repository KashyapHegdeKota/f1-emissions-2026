"use client";

import { useState } from "react";
import { Plane, Zap, Globe, ArrowRight, Activity } from "lucide-react";
import { info } from "console";

// --- ANIMATED LOADING COMPONENT ---
function LoadingAnimation() {
  return (
    <div className="h-full flex flex-col items-center justify-center min-h-[300px]">
      {/* Container for the animation */}
      <div className="relative w-32 h-32 flex items-center justify-center mb-8">
        
        {/* The Globe (Pulsing Center) */}
        <div className="absolute inset-0 flex items-center justify-center">
          <Globe size={64} className="text-blue-500 animate-pulse" />
        </div>

        {/* The Orbiting Plane Ring */}
        {/* 'animate-spin' makes this invisible div rotate 360 degrees */}
        <div className="absolute inset-0 animate-spin [animation-duration:3s]">
          {/* The Plane (Positioned at the top of the rotating ring) */}
          <div className="absolute -top-4 left-1/2 -translate-x-1/2">
             {/* Rotate the icon 90deg so it points 'forward' */}
            <Plane size={32} className="text-red-500 rotate-90" fill="currentColor" />
          </div>
        </div>

        {/* Outer Rings (Decorative radar effect) */}
        <div className="absolute inset-0 border-2 border-slate-700 rounded-full animate-ping [animation-duration:2s] opacity-20"></div>
      </div>

      <h3 className="text-xl font-bold text-slate-200 animate-pulse">Calculating Trajectory...</h3>
      <p className="text-sm text-slate-500 mt-2">Connecting to AWS Lambda Logistics Engine</p>
    </div>
  );
}

export default function Home() {
  // --- STATE MANAGEMENT ---
  const [origin, setOrigin] = useState("las_vegas");
  const [dest, setDest] = useState("miami");
  const [cargo, setCargo] = useState(25000);
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState<any>(null);

  // REPLACE THIS WITH YOUR AWS URL
  const API_URL = process.env.NEXT_PUBLIC_API_URL;

  const RACES: Record<string, {iso: string; name: string}> = {
    "melbourne": { iso: "au", name: "Melbourne" },
    "shanghai": { iso: "cn", name: "Shanghai" },
    "suzuka": { iso: "jp", name: "Suzuka" },
    "jeddah": { iso: "sa", name: "Jeddah" },
    "miami": { iso: "us", name: "Miami" },
    "montreal": { iso: "ca", name: "Montreal" },
    "monaco": { iso: "mc", name: "Monaco" },
    "barcelona": { iso: "es", name: "Barcelona" },
    "spielberg": { iso: "at", name: "Spielberg" },
    "silverstone": { iso: "gb", name: "Silverstone" },
    "spa": { iso: "be", name: "Spa-Francorchamps" },
    "hungaroring": { iso: "hu", name: "Hungaroring" },
    "zandvoort": { iso: "nl", name: "Zandvoort" },
    "monza": { iso: "it", name: "Monza" },
    "madrid": { iso: "es", name: "Madrid" },
    "baku": { iso: "az", name: "Baku" },
    "singapore": { iso: "sg", name: "Singapore" },
    "austin": { iso: "us", name: "Austin" },
    "mexico_city": { iso: "mx", name: "Mexico City" },
    "brazil": { iso: "br", name: "São Paulo" },
    "las_vegas": { iso: "us", name: "Las Vegas"},
    "qatar": { iso: "qa", name: "Lusail"},
    "abu_dhabi": { iso: "ae", name: "Abu Dhabi"},
  };

  // --- API HANDLER ---
  const handleCalculate = async () => {
    setLoading(true);
    try {
      // Construct URL with query parameters
      const url = `${API_URL}?origin_race_id=${origin}&dest_race_id=${dest}&cargo_kg=${cargo}`;
      
      const res = await fetch(url, {
        method: "POST", // Your Python endpoint is a POST
        headers: { "Content-Type": "application/json" },
      });

      const result = await res.json();
      setData(result);
    } catch (error) {
      console.error("Failed to fetch logistics data", error);
      alert("Error connecting to Mission Control (AWS). Check console.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 font-sans p-8">
      {/* HEADER */}
      <header className="max-w-4xl mx-auto mb-12 border-b border-slate-800 pb-6 flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold bg-gradient-to-r from-red-500 to-orange-500 bg-clip-text text-transparent">
            PaddockJet
          </h1>
          <p className="text-slate-400 text-sm">F1 Global Logistics & Carbon Engine</p>
        </div>
        <div className="flex items-center gap-2 text-green-400 text-xs uppercase tracking-widest border border-green-900 bg-green-950/30 px-3 py-1 rounded-full">
          <Activity size={14} />
          System Online
        </div>
      </header>

      <main className="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
        
        {/* LEFT COLUMN: CONTROLS */}
        <div className="md:col-span-1 space-y-6">
          <div className="bg-slate-900 p-6 rounded-xl border border-slate-800 shadow-xl">
            <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <Globe size={18} className="text-blue-400" /> Flight Path
            </h2>
            
            {/* INPUTS */}
            <div className="space-y-4">
              <div>
                <label className="text-xs text-slate-500 uppercase font-bold">Origin</label>
                <select 
                  className="w-full bg-slate-800 border border-slate-700 rounded p-2 text-sm focus:ring-2 focus:ring-red-500 outline-none appearance-none"
                  value={origin}
                  onChange={(e) => setOrigin(e.target.value)}
                >
                  {Object.entries(RACES).map(([id, info]) => (
                    <option key={id} value={id}>
                    {info.name}
                    </option>
                  ))}
                </select>
              </div>

              <div className="flex justify-center">
                <ArrowRight className="text-slate-600 rotate-90 md:rotate-0" />
              </div>

              <div>
                <label className="text-xs text-slate-500 uppercase font-bold">Destination</label>
                <select 
                  className="w-full bg-slate-800 border border-slate-700 rounded p-2 text-sm focus:ring-2 focus:ring-red-500 outline-none"
                  value={dest}
                  onChange={(e) => setDest(e.target.value)}
                >
                  {Object.entries(RACES).map(([id, info]) => (
                    <option key={id} value={id}>
                    {info.name}
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="text-xs text-slate-500 uppercase font-bold">Cargo Load (kg)</label>
                <input 
                  type="number" 
                  className="w-full bg-slate-800 border border-slate-700 rounded p-2 text-sm focus:ring-2 focus:ring-red-500 outline-none"
                  value={cargo}
                  onChange={(e) => setCargo(Number(e.target.value.toLocaleString()))}
                />
              </div>

              <button 
                onClick={handleCalculate}
                disabled={loading}
                className="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-3 rounded transition-all flex justify-center items-center gap-2"
              >
                {loading ? "Calculations in progress..." : "Calculate Telemetry"}
              </button>
            </div>
          </div>
        </div>

        {/* RIGHT COLUMN: DATA DISPLAY */}
        <div className="md:col-span-2 space-y-6">
          {loading ? (
            <div className="bg-slate-900/50 rounded-xl border border-slate-800 h-full flex items-center justify-center">
              <LoadingAnimation />
            </div>
          ) : data ? (
            <>
              {/* ROUTE BANNER */}
              <div className="bg-slate-800 p-4 rounded-lg border-l-4 border-red-500 flex justify-between items-center animate-in fade-in slide-in-from-bottom-4 duration-700">
                <div>
                  <p className="text-xs text-slate-400 uppercase">Mission Route</p>
                  {/* ORIGIN FLAG IMAGE */}
                    <div className="flex items-center gap-2">
                        {/* Force width/height and use w40 URL */}
                        <img 
                            src={`https://flagcdn.com/w40/${RACES[origin].iso}.png`}
                            srcSet={`https://flagcdn.com/w80/${RACES[origin].iso}.png 2x`} 
                            width="30"
                            alt={RACES[origin].name}
                            className="rounded shadow-sm border border-slate-600"
                        />
                        <span>{data.route.from}</span>
                    </div>
                    
                    <span className="text-slate-500 text-sm">✈</span>
                    
                    {/* DESTINATION FLAG IMAGE */}
                    <div className="flex items-center gap-2">
                        <img 
                            src={`https://flagcdn.com/w40/${RACES[dest].iso}.png`} 
                            srcSet={`https://flagcdn.com/w80/${RACES[dest].iso}.png 2x`}
                            width="30"
                            alt={RACES[dest].name}
                            className="rounded shadow-sm border border-slate-600"
                        />
                        <span>{data.route.to}</span>
                    </div>
                </div>
                <div className="text-right">
                  <p className="text-xs text-slate-400 uppercase">Airports</p>
                  <p className="font-mono text-yellow-400">{data.route.airports.split(' -> ')[0]}</p>
                  <p className= "text-slate-600">→</p>
                  <p className="font-mono text-yellow-400">{data.route.airports.split(' -> ')[1]}</p>
                </div>
              </div>

              {/* METRICS GRID */}
              <div className="grid grid-cols-2 gap-4">
                <div className="bg-slate-900 p-6 rounded-xl border border-slate-800">
                  <p className="text-xs text-slate-400 uppercase mb-2">Great Circle Distance</p>
                  <p className="text-3xl font-mono text-blue-400">{data.logistics.distance_km.toLocaleString()} <span className="text-sm text-slate-500">km</span></p>
                </div>
                <div className="bg-slate-900 p-6 rounded-xl border border-slate-800">
                  <p className="text-xs text-slate-400 uppercase mb-2">Flight Time (777F)</p>
                  <p className="text-3xl font-mono text-white">{data.logistics.estimated_flight_time}</p>
                </div>
              </div>

              {/* CARBON CARD */}
              <div className="bg-gradient-to-br from-slate-900 to-slate-800 p-6 rounded-xl border border-slate-700 relative overflow-hidden">
                <div className="relative z-10">
                  <p className="text-xs text-green-400 uppercase mb-2 flex items-center gap-2">
                    <Zap size={14} /> Environmental Impact
                  </p>
                  <p className="text-4xl font-bold text-white mb-1">
                    {data.environmental_impact.co2_emissions_kg.toLocaleString()} <span className="text-lg font-normal text-slate-400">kg CO₂</span>
                  </p>
                  <p className="text-xs text-slate-500 mt-2">{data.environmental_impact.note}</p>
                </div>
                {/* Background Decor */}
                <Zap className="absolute -bottom-4 -right-4 text-green-900/20" size={150} />
              </div>
            </>
          ):(
            // 3. EMPTY STATE
            <div className="h-full bg-slate-900/50 rounded-xl border border-slate-800 border-dashed flex flex-col items-center justify-center text-slate-600 min-h-[400px]">
              <div className = "bg-slate-800 p-4 rounded-full mb-4">
                <Plane size={32} className="opacity-50"/>
              </div>
              <p className="text-center px-6">Set your flight parameters and click <strong>"Calculate Telemetry"</strong> to initiate the logistics computation.</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}