from cli import *
import random


def encrypt():
    data: str | bytes = input_data(can_by_binary = True)
    key: int = get_int_key()
    random.seed(key)
    gamma: bytes = random.randbytes(len(data))
    if isinstance(data, bytes):
        encoded: bytes = b"".join((byte ^ gamma[index]).to_bytes() for index, byte in enumerate(data))
        output_binary_result(encoded)
    else:
        encoded: str = "".join(chr(ord(symbol) ^ gamma[index]) for index, symbol in enumerate(data))
        output_result(encoded)


def decrypt():
    encoded: str | bytes = input_encoded(can_by_binary = True)
    key: int = get_int_key()
    random.seed(key)
    gamma: bytes = random.randbytes(len(encoded))
    if isinstance(encoded, bytes):
        data: bytes = b"".join((byte ^ gamma[index]).to_bytes() for index, byte in enumerate(encoded))
        output_binary_result(data)
    else:
        data: str = "".join(chr(ord(symbol) ^ gamma[index]) for index, symbol in enumerate(encoded))
        output_result(data)


if __name__ == "__main__":
    menu(7, "Гаммирование", encrypt, decrypt)
