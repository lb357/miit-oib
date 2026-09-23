from cli import *
from alphabet import Alphabet


def encrypt():
    alphabet: Alphabet = get_alphabet()
    data: str = input_data()
    encoded: str = ""
    size: int = alphabet.get_size()

    for i in range(3):
        encoded = ""
        key: str = get_str_key()

        for index, symbol in enumerate(data):
            symbol_index = alphabet.get_index(symbol)
            key_index = alphabet.get_index(key[index % len(key)])
            encoded_index = (key_index - symbol_index) % size
            encoded += alphabet.get_symbol(encoded_index)
        data = encoded

    output_result(encoded)


def decrypt():
    alphabet: Alphabet = get_alphabet()
    encoded: str = input_encoded()
    data: str = ""
    size: int = alphabet.get_size()

    for i in range(3):
        data = ""
        key: str = get_str_key()

        for index, symbol in enumerate(encoded):
            encoded_index = alphabet.get_index(symbol)
            key_index = alphabet.get_index(key[index % len(key)])
            symbol_index = (key_index - encoded_index) % size
            data += alphabet.get_symbol(symbol_index)
        encoded = data

    output_result(data)


if __name__ == "__main__":
    menu(3, "Многоалфавитная многоконтурная подстановка", encrypt, decrypt)

