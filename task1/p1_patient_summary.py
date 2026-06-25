"""
Task 1 — Patient Summary

Complete this file without using AI tools.
Use fake/sample data only.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "condition": "diabetes", "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "condition": "hypertension", "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "condition": "asthma", "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "condition": "diabetes", "active": True},
]


def total_patients(patient_records):
    """Return the total number of patients."""
    count = 0
    for i in patient_records:
        count = count +1
    return count


def average_age(patient_records):
    """Return the average patient age."""
    count = 0
    number = 0
    for i in patient_records:
        count = count + i['age']
        number = number +1
    avg_age = count/number
    return avg_age


def count_active_patients(patient_records):
    """Return the number of active patients."""
    count = 0
    for i in patient_records:
        if i['active'] == True:
            count = count +1
    return count


def unique_conditions(patient_records):
    """Return a sorted list of unique conditions."""
    conditions = []
    for i in patient_records:
        if i['condition'] in conditions:
            continue
        else:
            conditions.append(i['condition'])
    conditions.sort()
    return conditions


def count_by_condition(patient_records):
    """Return a dictionary containing patient count by condition."""
    count_dict = {}
    conditions = []
    for j in patient_records:
        if j["condition"] not in conditions:
            conditions.append(j["condition"])
    
    for i in patient_records:
        if i["condition"] in count_dict:
            count_dict[i["condition"]] += 1
        else:
            count_dict[i["condition"]] = 1
            
    return count_dict
        



if __name__ == "__main__":
    total_patients(patients)
    average_age(patients)
    count_active_patients(patients)
    unique_conditions(patients)
    count_by_condition(patients)
    pass
