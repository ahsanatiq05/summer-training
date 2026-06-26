"""
Task 1 — Dictionary Analysis

Practice dictionaries and nested dictionaries.
Complete this file without using AI tools.
"""

patients = {
    1: {
        "name": "Ayesha Khan",
        "age": 32,
        "contact": {"city": "Karachi", "phone": "000-000"},
        "condition": "diabetes",
    },
    2: {
        "name": "Omar Ali",
        "age": 45,
        "contact": {"city": "Lahore", "phone": "111-111"},
        "condition": "hypertension",
    },
}


def get_patient_city(patient_id):
    """Return the city for a given patient ID."""
    if patient_id not in patients:
        return None
    return patients[patient_id]["contact"]["city"]



def update_patient_condition(patient_id, new_condition):
    """Update a patient's condition."""
    patients[patient_id]["condition"] = new_condition


def build_patient_summary():
    """Build and return a summary dictionary."""
    summary = {
        "total_patients" : len(patients.items()),
        "max_age" : (max(p["age"] for p in patients.values())),
        "cities" : (p["contact"]["city"] for p in patients.values())

    }
    return summary


if __name__ == "__main__":
    get_patient_city(1)
    pass
