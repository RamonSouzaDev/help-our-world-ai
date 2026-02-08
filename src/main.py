import time
import sys
import os

# Ensure src is in path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sensors.biosensor import BioSensor
from ai.diagnostic import MedicalDiagnosticAI
from data.gov_integration import GovernmentHealthAPI
from ai.coach import HealthCoachAI
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def main():
    print(Fore.CYAN + "================================================================")
    print(Fore.CYAN + Style.BRIGHT + "   🏥 HEALTH SENTINEL: AI GLOBAL MEDICINE MONITORING SYSTEM")
    print(Fore.CYAN + "   (c) 2026 Project Help Our World - RamonSouzaDev")
    print(Fore.CYAN + "================================================================\n")
    
    # 1. Initialize System Components
    print(Fore.YELLOW + "[INIT] Booting Medical Telemetry Sensors...")
    patient_monitor = BioSensor(patient_id="PATIENT-X-99")
    
    print(Fore.YELLOW + "[INIT] Loading AI Diagnostic Models (Version 1.0.4)...")
    ai_core = MedicalDiagnosticAI()

    print(Fore.YELLOW + "[INIT] Activating AI Health Coach Module...")
    coach = HealthCoachAI()
    
    print(Fore.YELLOW + "[INIT] Connecting to Government Health API (DataSUS/WHO)...")
    gov_api = GovernmentHealthAPI(region="BR-SP")
    
    print(Fore.GREEN + Style.BRIGHT + "\n✅ SYSTEM ONLINE. MONITORING STARTED.\n")
    time.sleep(1)

    # 2. Fetch Context (Epidemiological Data)
    gov_data = gov_api.fetch_epidemiological_alerts()
    print(Fore.MAGENTA + f"🌍 REGIONAL CONTEXT: {gov_data['region']}")
    print(Fore.RED + f"⚠️ ACTIVE OUTBREAKS: {[o['disease'] for o in gov_data['active_outbreaks']]}")
    print(Fore.CYAN + "-" * 60)

    # 3. Main Monitoring Loop
    try:
        iteration = 0
        while True:
            iteration += 1
            
            # A. Simulate reading from wearable
            vitals = patient_monitor.read_vitals()
            
            # B. Simulate a sudden health event at iteration 5
            if iteration == 5:
                print(Fore.RED + Style.BRIGHT + "\n[!!!] SIMULATING PHYSIOLOGICAL EVENT: SEPSIS ONSET [!!!]\n")
                patient_monitor.inject_pathology("SEPSIS_SHOCK")

            # C. AI Analysis
            diagnosis = ai_core.analyze_vitals(vitals)
            advice = coach.generate_advice(vitals)
            
            # D. Output / Logging
            # Color logic for vitals
            heart_color = Fore.RED if vitals.heart_rate_bpm > 100 or vitals.heart_rate_bpm < 50 else Fore.WHITE
            
            print(f"⏱️ {vitals.timestamp} | " + 
                  heart_color + f"HR: {vitals.heart_rate_bpm} BPM" + Fore.RESET + " | " +
                  f"SpO2: {vitals.spo2_percent}% | Temp: {vitals.temperature_c}C")
            
            if diagnosis["status"] == "CRITICAL":
                print(Fore.RED + Style.BRIGHT + f"   🚨 AI ALERT: {diagnosis['detected_anomalies']}")
                print(Fore.YELLOW + f"   💊 ACTION: {diagnosis['recommendation']}")
                
                # Check for Government Data Correlation
                if "FEVER" in diagnosis["detected_anomalies"]:
                    alert_msg = gov_api.correlate_symptoms(["High Fever", "Joint Pain"]) # Simulating symptom input
                    print(Fore.MAGENTA + f"   🏛️ GOV DATA INSIGHT: {alert_msg}")
                    
            elif diagnosis["status"] == "STABLE":
                print(Fore.GREEN + f"   ✅ AI Status: Vital signs within normal limits.")
                print(Fore.BLUE + f"   💬 {coach.coach_name}: {advice}")

            print(Fore.CYAN + "-" * 20)
            time.sleep(2)
            
    except KeyboardInterrupt:
        print(Fore.RED + "\n[STOP] Monitoring Session Ended by User.")

if __name__ == "__main__":
    main()
