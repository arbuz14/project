import os
import json

REVIEWS = "path/to/reviews.json"  # Змініть на фактичний шлях до файлу

def open_reviews_file(path: str = REVIEWS) -> list:
    # Відкриває файл з відгуками
    if not os.path.exists(path):
        with open(path, "w") as fh:
            json.dump([], fh)
    
    with open(path, "r", encoding="utf-8") as file:
        try:
            reviews = json.load(file)
        except json.JSONDecodeError:
            return []  # Повертає порожній список, якщо файл не містить валідного JSON
    
    return reviews

def save_reviews_file(file: list, path: str = REVIEWS):
    # Зберігає оновлені дані у файл
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(file, fh, indent=4, ensure_ascii=False)

def add_review(review: str, path: str = REVIEWS) -> str:
    # Додає новий відгук
    reviews = open_reviews_file()
    reviews.append(review)
    save_reviews_file(reviews)
    return f"Відгук '{review}' успішно додано."

# Приклад використання
print(add_review("Чудовий магазин"))

