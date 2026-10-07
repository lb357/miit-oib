from cli import *
import math


def encrypt():
    key: list[int] = get_int_array_key()
    data: list[str | None] = list(input_data())
    disabled: set[int] = set(get_int_array())

    for disabled_index in sorted(disabled):
        data.insert(disabled_index, None)
    encoded_blocks: dict[int, list[str | None]] = {}
    for key_index, key_value in enumerate(key):
        encoded_blocks[key_value] = data[key_index:key_index+len(data):len(key)]
    encoded: str = "".join("".join(
        symbol for symbol in encoded_blocks[key_value] if symbol is not None
    ) for key_value in sorted(key))
    output_result(encoded)

def decrypt():
    key: list[int] = get_int_array_key()
    encoded: str = input_encoded()
    disabled: set[int] = set(get_int_array())

    encoded_blocks: dict[int, list[str | None]] = {}
    encoded_index: int = 0
    size: int = len(encoded) + len(disabled)

    for key_value in sorted(key):
        key_index = key.index(key_value)
        block: list[str | None] = []
        for data_index in range(key_index, size, len(key)):
            if data_index in disabled:
                block.append(None)
            else:
                block.append(encoded[encoded_index])
                encoded_index += 1
        encoded_blocks[key_value] = block

    data: str = ""
    for data_index in range(math.ceil(size/len(key))):
        for key_value in key:
            if data_index < len(encoded_blocks[key_value]):
                symbol = encoded_blocks[key_value][data_index]
                if symbol is not None:
                    data += symbol
    output_result(data)


if __name__ == "__main__":
    menu(6, "Перестановка, усложненная по таблице", encrypt, decrypt)
