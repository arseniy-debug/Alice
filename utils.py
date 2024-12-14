# Здесь будут расположены вспомогательные функции, такие как функции для расчетов.
import json


def calculate_kbju(product, amount):
    # Здесь можно загружать данные о продуктах из json файла
    with open('data/products.json', 'r') as f:
        products_data = json.load(f)

    # Пример расчета
    if product in products_data:
        # Получение КБЖУ из базы данных
        kbju_data = products_data[product]
        kcal = (kbju_data["calories"] / 100) * amount
        protein = (kbju_data["protein"] / 100) * amount
        fats = (kbju_data["fats"] / 100) * amount
        carbs = (kbju_data["carbs"] / 100) * amount

        return {
            "kcal": kcal,
            "protein": protein,
            "fats": fats,
            "carbs": carbs
        }
    else:
        raise ValueError("Продукт не найден")
