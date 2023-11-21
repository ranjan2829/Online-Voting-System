class MedicalExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "Headache": ["Rest", "Drink water", "Take over-the-counter pain reliever"],
            "Fever": ["Rest", "Stay hydrated", "Take fever-reducing medication"],
            "Cough": ["Stay hydrated", "Use cough drops", "Consult a doctor if severe"],
            "Sore Throat": ["Gargle with warm saltwater", "Use throat lozenges", "Consult a doctor if persistent"],
            "Stomachache": ["Avoid heavy meals", "Take over-the-counter antacids", "Consult a doctor if severe"]
        }

    def diagnose(self, symptoms):
        recommendations = []
        for symptom in symptoms:
            if symptom in self.knowledge_base:
                recommendations.extend(self.knowledge_base[symptom])
            else:
                recommendations.append(f"Unknown symptom: {symptom}")
        return recommendations

def main():
    print("Medical Expert System")
    expert_system = MedicalExpertSystem()
    symptoms = input("Enter the symptoms (comma-separated): ").split(",")
    recommendations = expert_system.diagnose(symptoms)
    
    print("\nRecommendations:")
    for recommendation in recommendations:
        print("- " + recommendation)

if __name__ == "__main__":
    main()
