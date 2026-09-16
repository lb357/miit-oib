from cli import *
from alphabet import Alphabet


def encrypt():
    alphabet: Alphabet = get_alphabet()
    data: str = input_data()

    size: int = alphabet.get_size()
    encoded: str = ""
    for index, symbol in enumerate(data):
        symbol_index = alphabet.get_index(symbol)
        encoded_index = (symbol_index + index + 1) % size
        encoded += alphabet.get_symbol(encoded_index)

    output_result(encoded)


def decrypt():
    alphabet: Alphabet = get_alphabet()
    encoded: str = input_encoded()

    size: int = alphabet.get_size()
    data: str = ""
    for index, symbol in enumerate(encoded):
        encoded_index = alphabet.get_index(symbol)
        symbol_index = (encoded_index - index - 1) % size
        data += alphabet.get_symbol(symbol_index)
    output_result(data)


if __name__ == "__main__":
    menu(2, "Многоалфавитная одноконтурная подстановка", encrypt, decrypt)

