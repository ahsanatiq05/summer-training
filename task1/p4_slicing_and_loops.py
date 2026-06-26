"""
Task 1 — Slicing and Loops

Practice slicing, loops, enumerate, zip, and comprehensions.
Complete this file without using AI tools.
"""

patient_ids = [101, 102, 103, 104, 105, 106, 107]
patient_names = ["Ayesha", "Omar", "Sara", "Bilal", "Hina", "Usman", "Maha"]


def slicing_examples():
    """Return examples of list slicing."""
    ids = []
    ids.append(patient_ids[:3])
    ids.append(patient_ids[-3:])
    ids.append(patient_ids[::-1])
    return ids


def loop_examples():
    """Practice range, enumerate, and zip."""
    for i in enumerate(patient_ids):
        zip_result = (zip(patient_ids, patient_names))


def comprehension_examples():
    """Return values created using comprehensions."""
    even = []
    for index, i in enumerate(patient_ids):
        if i % 2 == 0:
            even.append(i)
    upper_names = [p.upper() for p in patient_names]
    return [even, upper_names]


if __name__ == "__main__":
    slicing_examples()
    loop_examples()
    comprehension_examples()
