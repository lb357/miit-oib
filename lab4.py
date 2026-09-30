from cli import *
from alphabet import Alphabet


def encrypt():
    alphabet: Alphabet = get_alphabet()
    data: str = input_data()
    key: str = get_str_key()

    encoded: str = ""
    size: int = alphabet.get_size()

    for index, symbol in enumerate(data):
        symbol_index = alphabet.get_index(symbol)
        key_index = alphabet.get_index(key[index % len(key)])
        encoded_index = (symbol_index + key_index) % size
        encoded += alphabet.get_symbol(encoded_index)

    output_result(encoded)


def decrypt():
    alphabet: Alphabet = get_alphabet()
    encoded: str = input_encoded()
    key: str = get_str_key()

    data: str = ""
    size: int = alphabet.get_size()


    for index, symbol in enumerate(encoded):
        encoded_index = alphabet.get_index(symbol)
        key_index = alphabet.get_index(key[index % len(key)])
        symbol_index = (encoded_index - key_index) % size
        data += alphabet.get_symbol(symbol_index)

    output_result(data)


if __name__ == "__main__":
    menu(4, "Многоалфавитная подстановка по таблице Виженера", encrypt, decrypt)

