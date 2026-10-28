#include <stdbool.h>
#include <stdint.h>

typedef struct {
    uint8_t data_size;
    uint64_t data;
} DataBlock;


bool get_n_bit(DataBlock *block, uint8_t n);
void set_n_bit(DataBlock *block, uint8_t n, bool value);

DataBlock permute_bits(DataBlock *block, const uint8_t *table, uint8_t table_size);
DataBlock xor_bits(DataBlock *a, DataBlock *b);
DataBlock concat_bits(DataBlock *a, DataBlock *b);
DataBlock left_bits(DataBlock *a, uint8_t shift);
DataBlock slice_bits(DataBlock *block, uint8_t start, uint8_t length);
