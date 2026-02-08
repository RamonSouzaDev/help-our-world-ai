import math

class MedicalDiagnosticAI:
    """
    The Intelligence Core. 
    Analyzes telemetry to predict adverse health events.
    """
    
    def __init__(self):
        self.model_version = "v1.0.4-Healthcare-Alpha"
        self.risk_threshold = 0.8
        
    def analyze_vitals(self, vitals) -> dict:
        """
        Runs heuristics and ML-lite logic to assess patient status.
        Returns a risk assessment analysis.
        """
        risk_score = 0.0
        anomalies = []
        
        # 1. Rule-Based Triage (The "Emergency Room" Logic)
        if vitals.heart_rate_bpm > 100:
            risk_score += 0.3
            anomalies.append("TACHYCARDIA")
        elif vitals.heart_rate_bpm < 50:
            risk_score += 0.4
            anomalies.append("BRADYCARDIA")
            
        if vitals.spo2_percent < 94:
            risk_score += 0.5
            anomalies.append("HYPOXIA")
        
        if vitals.temperature_c > 38.0:
            risk_score += 0.2
            anomalies.append("FEVER")

        # 2. Advanced Correlation (Sepsis Detector)
        # Sepsis often presents as Fever + Tachycardia + Low Blood Pressure
        if vitals.temperature_c > 38 and vitals.heart_rate_bpm > 90 and vitals.systolic_bp < 95:
             risk_score = 1.0
             anomalies.append("!! POSSIBLE SEPSIS SHOCK !!")

        # Normalize score
        risk_score = min(risk_score, 1.0)
        
        result = {
            "patient_id": vitals.patient_id,
            "ai_risk_score": risk_score,
            "status": "CRITICAL" if risk_score >= 0.7 else "STABLE",
            "detected_anomalies": anomalies,
            "recommendation": self._get_recommendation(risk_score)
        }
        return result

    def _get_recommendation(self, score):
        if score > 0.8:
            return "IMMEDIATE MEDICAL INTERVENTION REQUIRED"
        elif score > 0.4:
            return "Monitor patient closely. Schedule follow-up."
        else:
            return "Continue standard monitoring."
