import random
import time
import uuid
import json
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class VitalSigns:
    """Standard Medical Telemetry Data Structure"""
    patient_id: str
    timestamp: str
    heart_rate_bpm: int
    spo2_percent: int
    systolic_bp: int
    diastolic_bp: int
    temperature_c: float
    status: str = "NORMAL"

class BioSensor:
    """
    Simulates a medical-grade wearable device.
    Generates realistic vital signs with physiological noise and occasional anomalies.
    """
    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        # Baseline 'healthy' values for this patient
        self.base_hr = 75
        self.base_spo2 = 98
        self.base_temp = 36.5
        
    def read_vitals(self) -> VitalSigns:
        """Simulates a sensor reading cycle."""
        # Add natural physiological variance (Inter-beat variability simulation)
        current_hr = int(self.base_hr + random.gauss(0, 5))
        current_spo2 = int(min(100, self.base_spo2 + random.gauss(0, 1)))
        
        # Simulate Blood Pressure fluctuating
        sys_bp = int(120 + random.gauss(0, 8))
        dia_bp = int(80 + random.gauss(0, 5))
        
        # Simulate Temperature
        temp = round(self.base_temp + random.gauss(0, 0.2), 1)

        return VitalSigns(
            patient_id=self.patient_id,
            timestamp=datetime.now().isoformat(),
            heart_rate_bpm=current_hr,
            spo2_percent=current_spo2,
            systolic_bp=sys_bp,
            diastolic_bp=dia_bp,
            temperature_c=temp
        )

    def inject_pathology(self, condition: str):
        """Mechanic to simulate medical emergencies for AI training."""
        if condition == "SEPSIS_SHOCK":
            self.base_hr = 115      # Tachycardia
            self.base_temp = 38.9   # Fever
            self.base_spo2 = 91     # Hypoxia
        elif condition == "BRADYCARDIA":
            self.base_hr = 45       # Dangerous low heart rate
