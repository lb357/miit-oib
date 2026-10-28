#include "datablock.h"

bool get_n_bit(DataBlock *block, uint8_t n) {
    return (block->data >> (block->data_size - 1 - n)) & 1;
}

void set_n_bit(DataBlock *block, uint8_t n, bool value) {
    if (value) {
        block->data |= (uint64_t)1 << (block->data_size - 1 - n);
    } else {
        block->data &= ~((uint64_t)1 << (block->data_size - 1 - n));
    }
}

DataBlock permute_bits(DataBlock *block, const uint8_t *table, uint8_t table_size) {
    DataBlock out = {
        .data_size = table_size,
        .data = 0
    };
    for (int8_t i = 0; i < table_size; i++) {
        set_n_bit(&out, i, get_n_bit(block, table[i] - 1));
    }
    return out;
}


DataBlock xor_bits(DataBlock *a, DataBlock *b) {
    DataBlock out = {
        .data_size = (a->data_size >= b->data_size) ? a->data_size : b->data_size,
        .data = a->data^b->data
    };
    return out;
}

DataBlock concat_bits(DataBlock *a, DataBlock *b) {
    DataBlock out = {
        .data_size = a->data_size + b->data_size,
        .data = (a->data << b->data_size) | b->data
    };
    return out;
}

DataBlock left_bits(DataBlock *a, uint8_t shift) {
    uint64_t mask = a->data_size == 64 ? UINT64_MAX : ((uint64_t)1 << a->data_size) - 1;
    DataBlock out = {
        .data_size = a->data_size,
        .data = ((a->data << shift) | (a->data >> (a->data_size-shift))) & mask
    };
    return out;
}

DataBlock slice_bits(DataBlock *block, uint8_t start, uint8_t length) {
    uint64_t mask = length == 64 ? UINT64_MAX : ((uint64_t)1 << length) - 1;
    DataBlock out = {
        .data_size = length,
        .data = (block->data >> (block->data_size - start - length)) & (mask)
    };
    return out;
}
