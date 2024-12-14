# Этот файл будет основным входом в ваш проект. Здесь обрабатывается входящий запрос и вызываются правильные функции в зависимости от типа запроса.
from handlers import handle_calculation_request, handle_start_request, handle_help_request

def handler(event, context):
    if event["request"]["type"] == "LaunchRequest":
        return handle_start_request(event)

    if event["request"]["type"] == "IntentRequest":
        if event["request"]["intent"]["name"] == "CalculateIntent":
            return handle_calculation_request(event)
        elif event["request"]["intent"]["name"] == "HelpIntent":
            return handle_help_request(event)

    return handle_unknown_request(event)