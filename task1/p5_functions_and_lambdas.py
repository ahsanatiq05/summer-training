"""
Task 1 — Functions and Lambda Functions

Practice reusable functions, type hints, and lambda functions.
Complete this file without using AI tools.
"""

patients = [
    {"name": "ayesha khan", "height_m": 1.65, "weight_kg": 68, "active": True},
    {"name": "omar ali", "height_m": 1.78, "weight_kg": 82, "active": False},
    {"name": "sara ahmed", "height_m": 1.60, "weight_kg": 54, "active": True},
]


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI."""
    return weight_kg/ (height_m**2)


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    if bmi <= 17:
        return "underweight"
    if bmi > 17 and  bmi <= 22:
        return "normal"
    if bmi > 22 and bmi <= 27:
        return "overweight"
    else: 
        return "obese"


def format_name(name: str) -> str:
    """Convert a name to title case."""
    name = name.lower()
    name = name.title()
    return name


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    patients = []
    for i in patient_records:
        if i["active"] == True:
            patients.append(i)
    print(patients)
    return patients



def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    
    return sorted (patient_records, key=lambda x: x["weight_kg"])


if __name__ == "__main__":
    pass
