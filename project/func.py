import json
import os
from datetime import datetime

current_path = os.path.dirname(os.path.abspath(__file__))
op_file_path = os.path.join(current_path, "..", "operations.json")

def read_file(file_path=op_file_path):
    with open(file_path, "r") as file:
        """Получение перечень операций из файла"""
        data = json.load(file)
        return data

def print_recent_operations(data):
    executed_operations = [op for op in data if op.get("state") == "EXECUTED"]
    """получаем только EXECUTED операции и сортируем их по дате"""
    recent_operations = sorted(executed_operations, key=lambda op: op["date"], reverse=True)[:5]


    result = []
    for operation in recent_operations:
        """получаем нужные данные и добавляем в список"""
        operation_date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        operation_description = operation["description"]
        operation_from = mask_card_number(operation.get("from"))
        operation_to = mask_account_number(operation["to"])
        operation_amount = float(operation["operationAmount"]["amount"])
        operation_currency = operation["operationAmount"]["currency"]["name"]

        result.append(f"{operation_date} {operation_description}")
        result.append(f"{operation_from} -> {operation_to}")
        result.append(f"{operation_amount} {operation_currency}")
        result.append("")

    return "\n".join(result)



def mask_card_number(card_number):
    """преобразуем from в нужный нам вид"""
    if card_number:
        card_name = ' '.join(card_number.split()[:-1])
        num = card_number.split()[-1]
        formatted_account = f"{num[:4]} {num[4:6]}{num[6:12].replace(num[6:12], '** ****')} {num[-4:]}"
        card_number = card_name + ' ' + formatted_account

    return card_number

def mask_account_number(account_number):
    """преобразуем to в нужный нам вид"""
    if account_number:
        name = ' '.join(account_number.split()[:-1])
        number = account_number.split()[-1]
        formatted_account = name + " " + '**' + number[-4:]
        return formatted_account

    return account_number

