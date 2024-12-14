# В этом файле будут определены функции для обработки конкретных запросов, таких как запросы на расчет, стартовые команды и помощь.
import json
from utils import calculate_kbju
import data.products  # Пример импорта данных о продуктах

def handle_start_request(event):
    text = "Привет! Это калькулятор КБЖУ. Какой продукт хотите добавить?"
    return create_response(text)

def handle_calculation_request(event):
    product = event["request"]["intent"]["slots"]["Product"]["value"]
    amount = event["request"]["intent"]["slots"]["Amount"]["value"]

    # Выполняем расчеты
    kbju = calculate_kbju(product, amount)
    text = f"В {amount} граммах {product} содержится {kbju['kcal']} калорий, {kbju['protein']} г белков, {kbju['fats']} г жиров, {kbju['carbs']} г углеводов."
    
    return create_response(text)

def handle_help_request(event):
    text = "Вы можете сказать мне название продукта и количество, чтобы рассчитать КБЖУ."
    return create_response(text)

def handle_unknown_request(event):
    text = "Извините, я не понял вас. Пожалуйста, попробуйте еще раз."
    return create_response(text)
    
def create_response(text, end_session=False):
    return {
        "version": event["version"],
        "session": event["session"],
        "response": {
            "text": text,
            "end_session": end_session,
        },
    }