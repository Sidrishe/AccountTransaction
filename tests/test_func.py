import pytest
import json
import os
from project.func import mask_card_number, mask_account_number, print_recent_operations, read_file


def test_mask_card_number():
    card_number = "Visa Platinum 1246377376343588"
    masked_number = mask_card_number(card_number)
    assert masked_number == "Visa Platinum 1246 37** **** 3588"

    card_number = "Maestro 3928549031574026"
    masked_number = mask_card_number(card_number)
    assert masked_number == "Maestro 3928 54** **** 4026"

    card_number = None
    assert mask_card_number(card_number) == None

def test_mask_account_number():
    account_number = "Счет 14211924144426031657"
    masked_number = mask_account_number(account_number)
    assert masked_number == "Счет **1657"

    account_number = "Счет 43597928997568165086"
    masked_number = mask_account_number(account_number)
    assert masked_number == "Счет **5086"

    account_number = None
    masked_number = mask_account_number(account_number)
    assert masked_number == None


@pytest.fixture()
def data():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]


def test_read_file():
    expected_result = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  }
  ]

    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_path, "..", 'oper_test.json')
    assert read_file(file_path) == expected_result

def test_print_recent_operations(data):
    assert print_recent_operations(data) == '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n'