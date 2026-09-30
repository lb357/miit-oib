from cli import *

def encrypt():
    key: list[int] = get_int_array_key()
    data: str = input_data()

    encoded_blocks: dict[int, str] = {}
    for key_index, key_value in enumerate(key):
        encoded_blocks[key_value] = data[key_index:key_index+len(data):len(key)]
    encoded: str = "".join(encoded_blocks[key_value] for key_value in sorted(key))
    output_result(encoded)


def decrypt():
    key: list[int] = get_int_array_key()
    encoded: str = input_encoded()

    encoded_blocks: dict[int, str] = {}
    encoded_index: int = 0
    for key_value in sorted(key):
        key_index = key.index(key_value)
        block_size = len(range(key_index, len(encoded), len(key)))
        encoded_blocks[key_value] = encoded[encoded_index:encoded_index + block_size]
        encoded_index += block_size
    data: str = "".join(
        encoded_blocks[key_value][data_index]
        for data_index in range(len(encoded))
        for key_value in key
        if data_index < len(encoded_blocks[key_value])
    )
    output_result(data)


if __name__ == "__main__":
    menu(5, "Простая перестановка", encrypt, decrypt)

