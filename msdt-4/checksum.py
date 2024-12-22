import json
import hashlib
import logging
import csv
import re
from typing import List

from paths import RESULT_PATH, CSV_PATH, REGULAR, LOGS


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s',
    handlers=[
        logging.FileHandler(LOGS, encoding="utf-8")
    ]
)

"""
В этом модуле обитают функции, необходимые для автоматизированной проверки результатов ваших трудов.
"""


def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет md5 хеш от списка целочисленных значений.

    ВНИМАНИЕ, ВАЖНО! Чтобы сумма получилась корректной, считать, что первая строка с данными csv-файла имеет номер 0
    Другими словами: В исходном csv 1я строка - заголовки столбцов, 2я и остальные - данные.
    Соответственно, считаем что у 2 строки файла номер 0, у 3й - номер 1 и так далее.

    :param row_numbers: список целочисленных номеров строк csv-файла, на которых были найдены ошибки валидации
    :return: md5 хеш для проверки через github action
    """
    logging.info('Вычисление md5 хэша')
    row_numbers.sort()
    hash_sum = hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()
    logging.info(f'Полученная сумма {hash_sum}')
    return hash_sum


def serialize_result(variant: int, checksum: str) -> None:
    """
    Метод для сериализации результатов лабораторной пишите сами.
    Вам нужно заполнить данными - номером варианта и контрольной суммой - файл, лежащий в папке с лабораторной.
    Файл называется, очевидно, result.json.

    ВНИМАНИЕ, ВАЖНО! На json натравлен github action, который проверяет корректность выполнения лабораторной.
    Так что не перемещайте, не переименовывайте и не изменяйте его структуру, если планируете успешно сдать лабу.

    :param variant: номер вашего варианта
    :param checksum: контрольная сумма, вычисленная через calculate_checksum()
    """
    logging.info('Начало записи результата')
    result = {
        "variant": variant,
        "checksum": checksum
    }
    with open(RESULT_PATH, 'w', encoding='utf-8') as file:
        json.dump(result, file)
    logging.info(f'Результат успешно записан в файл по адресу {RESULT_PATH}')


def read_csv(path: str) -> list[list[str]]:
    """
    read csv to list
    """
    logging.info('Начало чтения файла')
    with open(path, 'r', encoding="utf-16") as file:
        data = [row for row in csv.reader(file, delimiter=";")][1:]
        logging.info('Файл успешно прочитан и результат записан в data')
        return data


def validate_data(data: list[list[str]], regular: dict) -> list[int]:
    """
    find invalide indexs in file
    """
    logging.info('Начало поиска невалидных строк')
    invalid_rows = []
    for row_number, row in enumerate(data):
        for _, (field, key) in enumerate(zip(row, regular.keys())):
            pattern = regular[key]
            if not re.fullmatch(pattern, field):
                logging.warning(f'Найдена невалидная строка под номером {row_number}')
                invalid_rows.append(row_number)
                break
    logging.info('Список строк успешно найден')
    return invalid_rows


if __name__ == "__main__":
    logging.info('Начло выполнения программы')
    data = read_csv(CSV_PATH)
    rows = validate_data(data, REGULAR)
    checksum = calculate_checksum(rows)
    serialize_result(4, checksum)
    logging.info('Программа успешно выполнена')