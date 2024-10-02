import json 
import os

from app.data import list_files


def open_file(path: str = list_files.PATIENTS) -> list:
    if not os.path.exists(path):
        with open(path, "w") as fh:
            json.dump([], fh)
    with open(path, "r", encoding="utf-8") as file:
        patients = json.load(file)
    return patients


def save_file(file: list, path: str = list_files.PATIENTS):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(file, fh, indent=4, ensure_ascii=False)


def add_patient(patient, path: str = list_files.PATIENTS) -> str:
    patients = open_file()
    if patient not in patients:
        patients.append(patient)
        save_file(patients)
        msg = f"Пацієнт '{patient}' успішно додано."
    else:
        msg = f"Пацієнт '{patient}' вже є в базі."
    return msg
