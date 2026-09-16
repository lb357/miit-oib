from cli import *
from alphabet import Alphabet


def encrypt():
    alphabet : Alphabet = get_alphabet()
    key : int = get_int_key()
    data : str = input_data()

    size : int = alphabet.get_size()
    encoded : str = ""
    for symbol in data:
        symbol_index = alphabet.get_index(symbol)
        encoded_index = (symbol_index + key) % size
        encoded += alphabet.get_symbol(encoded_index)

    output_result(encoded)


def decrypt():
    alphabet : Alphabet = get_alphabet()
    key : int = get_int_key()
    encoded : str = input_encoded()

    size : int = alphabet.get_size()
    data : str = ""
    for symbol in encoded:
        encoded_index = alphabet.get_index(symbol)
        symbol_index = (encoded_index - key) % size
        data += alphabet.get_symbol(symbol_index)
    output_result(data)
    

if __name__ == "__main__":
    menu(1, "Одноалфавитная подстановка", encrypt, decrypt)

