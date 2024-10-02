import json
import os
from app import main

PATIENTS = "app/files/patients.json"
VISITS = "app/files/visits.json"
REVIEWS = "app/files/reviews.json"

def open_file(path: str) -> list:
    """Відкриває файл або створює порожній файл, якщо він не існує."""
    if not os.path.exists(path):
        with open(path, "w") as fh:
            json.dump([], fh)
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_file(file: list, path: str):
    """Зберігає оновлені дані у файл."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(file, fh, indent=4, ensure_ascii=False)

# Функції для роботи з пацієнтами
def add_patient(patient: str) -> str:
    patients = open_file(PATIENTS)
    if patient not in patients:
        patients.append(patient)
        save_file(patients, PATIENTS)
        return f"Пацієнт '{patient}' успішно додано."
    return f"Пацієнт '{patient}' вже є в базі."

def list_patients() -> list:
    """Повертає список пацієнтів."""
    return open_file(PATIENTS)

# Функції для роботи з візитами
def add_visit(visit: str) -> str:
    visits = open_file(VISITS)
    visits.append(visit)
    save_file(visits, VISITS)
    return f"Запис про візит '{visit}' успішно додано."

def list_visits() -> list:
    """Повертає список візитів."""
    return open_file(VISITS)

# Функції для роботи з відгуками
def add_review(review: str) -> str:
    reviews = open_file(REVIEWS)
    reviews.append(review)
    save_file(reviews, REVIEWS)
    return f"Відгук '{review}' успішно додано."

def list_reviews() -> list:
    """Повертає список відгуків."""
    return open_file(REVIEWS)

# Головна функція для демонстрації
def main():
    print(add_patient("Котик"))
    print(add_visit("Візит до ветеринара для щеплення Котика"))
    print(add_review("Чудовий магазин"))
    
    print("Пацієнти:", list_patients())
    print("Візити:", list_visits())
    print("Відгуки:", list_reviews())

if __name__ == "__main__":
    main()

