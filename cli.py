from typing import Callable
from alphabet import *


author = "Брискиндов Леонид Олегович"


def menu(lab_num: int, lab_name: str, encrypt: Callable, decrypt: Callable):
    print(f"Лабораторная работа №{lab_num}. \"{lab_name}\"")
    print("по дисциплине \"Основы информационной безопасности\"")
    print(f"Выполнил: {author}")
    print("УВП-212 / РУТ (МИИТ) 2026")
    print()
    while True:
        print("Выберите действие из списка:\n1. Зашифровать"
              "\n2. Расшифровать\n3. Выйти")
        match get_int():
            case 1:
                encrypt()
            case 2:
                decrypt()
            case 3:
                exit()
            case _:
                print("Неизвестное действие, повторите попытку")

                
def get_int(label: str = ""):
    while True:
        if label != "":
            print(label)
        try:
            return int(input("> "))
        except ValueError:
            print(f"Введено не число, повторите попытку")


def get_int_key() -> int:
    print("Введите ключ (число):")
    return get_int()

def get_int_array_key(unique: bool = True) -> list[int]:
    return get_int_array("Введите ключ (набор чисел через пробел):")


def get_int_array(label: str = "Введите набор чисел через пробел", unique: bool = True) -> list[int]:
    print(label)
    while True:
        try:
            data: list[int] = list(map(int, input("> ").split(" ")))
            if unique:
                assert len(set(data)) == len(data)
            return data
        except (ValueError, AssertionError):
            print(f"Введен не набор уникальных чисел через пробел, повторите попытку")


def get_str_key() -> str:
    print("Введите ключ (строку):")
    return input()


def get_alphabet() -> Alphabet:
    while True:
        try:
            print("Выберите алфавит из списка:\n1. Обобщенный\n"
                  "2. Русский\n3. Русский (реверс.)\n4. Английский\n"
                  "5. Юникод\n6. ASCII\n7. Символы ФИО\n8. Ввести \n9. Загрузить из файла")
            match get_int():
                case 1:
                    return StringAlphabet("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                                          "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                          "abcdefghijklmnopqrstuvwxyz"
                                          "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                          ".,!?;\"'0123456789@#$%^&*()"
                                          "-_+<>={}[]\\/ ")
                case 2:
                    return StringAlphabet("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                                          "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ")
                case 3:
                    return StringAlphabet(" ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА"
                                          "яюэьыъщшчцхфутсрпонмлкйизжёедгвба")
                case 4:
                    return StringAlphabet("abcdefghijklmnopqrstuvwxyz"
                                          "ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
                case 5:
                    return UnicodeAlphabet()
                case 6:
                    return AsciiAlphabet()
                case 7:
                    return StringAlphabet("кдряБи ОнсвЛгчоела")
                case 8:
                    return StringAlphabet(input("Алфавит: "))
                case 9:
                    with open(input("Путь к файлу: "), "r", encoding='utf-8') as file:
                        return StringAlphabet(file.read())
                case _:
                    print("Неизвестное действие, повторите попытку")
        except AssertionError:
            print(f"Некорректный алфавит, повторите попытку")
        except FileNotFoundError:
            print("Файл не найден, повторите попытку")


def input_data(can_by_binary: bool = False) -> str | bytes:
    while True:
        try:
            menu_text = "Входные данные:\n1. ФИО\n2. Ввести\n3. Загрузить из файла"
            if can_by_binary:
                menu_text+="\n4. Загрузка из бинарного файла"
            print(menu_text)
            match get_int():
                case 1:
                    return author
                case 2:
                    return input("Ввод исходных данных: ")
                case 3:
                    with open(
                            input("Путь к файлу: "),
                            "r",
                            encoding='utf-8'
                    ) as file:
                        return file.read()
                case 4:
                    assert can_by_binary
                    with open(
                            input("Путь к бинарному файлу: "),
                            "rb",
                    ) as file:
                        return file.read()
                case _:
                    print("Неизвестное действие, повторите попытку")
        except FileNotFoundError:
            print("Файл не найден, повторите попытку")
        except AssertionError:
            print("Неизвестное действие, повторите попытку")


def input_encoded(can_by_binary: bool = False) -> str | bytes:
    while True:
        try:
            menu_text = "Входные данные:\n1. Ввести\n2. Загрузить из файла"
            if can_by_binary:
                menu_text += "\n3. Загрузить из бинарного файла"
            print(menu_text)
            match get_int():
                case 1:
                    return input("Ввод зашифрованных данных: ")
                case 2:
                    with open(input("Путь к файлу: "), "r", encoding='utf-8') as file:
                        return file.read()
                case 3:
                    assert can_by_binary
                    with open(
                            input("Путь к бинарному файлу: "),
                            "rb",
                    ) as file:
                        return file.read()
                case _:
                    print("Неизвестное действие, повторите попытку")
        except FileNotFoundError:
            print("Файл не найден, повторите попытку")
        except AssertionError:
            print("Неизвестное действие, повторите попытку")


def output_result(result: str):
    while True:
        print("Выходные данные:\n1. Вывести\n2. Сохранить в файл\n3. Сохранить в бинарный файл")
        match get_int():
            case 1:
                print(f"Вывод: {result}")
                return
            case 2:
                with open(input("Путь к файлу: "), "w", encoding='utf-8') as file:
                    file.write(result)
                return
            case _:
                print("Неизвестное действие, повторите попытку")


def output_binary_result(result: bytes):
    with open(input("Путь к бинарному файлу вывода: "), "wb") as file:
        file.write(result)
