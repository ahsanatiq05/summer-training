"""
Task 1 — Final Problem: Triage Report

Complete this file without using AI tools.
Use fake/sample data only.

Tip: collections.Counter can make counting by risk label easier, but a
plain dictionary works too — import it yourself if you want to use it.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "risk_score": 72, "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "risk_score": 88, "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "risk_score": 35, "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "risk_score": 91, "active": True},
]


def label_risk(risk_score: int) -> str:
    """Return low, medium, or high based on risk score."""
    if risk_score < 50:
        return "low"
    elif risk_score >= 50 and risk_score < 75:
        return "medium"
    else:
        return "high"
    


def add_risk_labels(patient_records: list[dict]) -> list[dict]:
    """Return copies of patient records with a risk_label field added."""
    patients_arr = []
    for i in patient_records:
        patients = i.copy()
        label = label_risk(i["risk_score"])
        patients["risk_label"] = label
        patients_arr.append(patients)
    return patients_arr


def build_triage_report(patient_records: list[dict]) -> dict:
    """Build a triage report from patient records."""
    patients_with_labels = add_risk_labels(patient_records)
    counts = {"low" : 0, "medium": 0, "high" :0}
    for i in patients_with_labels:
        if i["risk_label"] == "low":
            counts["low"] += 1
        elif i["risk_label"] == "medium":
            counts["medium"] += 1
        elif i["risk_label"] == "high":
            counts["high"] += 1
    
    active_high = [p for p in patients_with_labels if p["active"] == True and p["risk_label"] == "high"]

    report = {
        "summary" : {
            "total_patients": len(patient_records),
        },

        "risk_counts" : counts,
        "active_high_risk_patients" : active_high
    }
    return report


if __name__ == "__main__":
    report = build_triage_report(patients)
    print(report)

