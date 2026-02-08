import random

class HealthCoachAI:
    """
    An engaging AI module that provides personalized health advice 
    and encouragement based on patient trends.
    """
    
    def __init__(self):
        self.coach_name = "Dr. Sentinel"
        
    def generate_advice(self, vitals) -> str:
        """
        Generates context-aware health engagement messages.
        """
        # 1. High Stress / High Heart Rate (but not critical)
        if vitals.heart_rate_bpm > 90 and vitals.status == "NORMAL":
            return self._random_advice("stress_relief")
            
        # 2. Good Health (Positive Reinforcement)
        elif 60 <= vitals.heart_rate_bpm <= 80 and vitals.spo2_percent >= 98:
            return self._random_advice("positive")
            
        # 3. Low SpO2 (Gentle Nudge)
        elif vitals.spo2_percent < 96 and vitals.status == "NORMAL":
            return self._random_advice("breathing")
            
        return "Maintaining stable vitals. Keep up the good work."

    def _random_advice(self, category: str) -> str:
        messages = {
            "stress_relief": [
                "I notice your heart rate is elevated. Let's take a deep breath together. 🌿",
                "You seem stressed. Remember: Health is wealth. Take a 5-minute break.",
                "High BPM detected. Try the 4-7-8 breathing technique now."
            ],
            "positive": [
                "Your vitals are perfect! Great job maintaining your health today. 🌟",
                "Heart rate is optimal. You are in the 'Green Zone'. Keep it up!",
                "Excellent physiological state detected. You're crushing it!"
            ],
            "breathing": [
                "Oxygen levels are slightly lower. Please stand up and stretch.",
                "Let's get some fresh air. Deep breathing can boost your SpO2.",
                "Posture check! Sitting up straight improves lung capacity."
            ]
        }
        return random.choice(messages[category])
