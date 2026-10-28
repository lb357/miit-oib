#include "datablock.h"
#include <stddef.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>


static void uint64_to_bytes(uint64_t value, uint8_t bytes[8], uint8_t size) {
    for (uint8_t i = size; i > 0; --i) {
        bytes[i - 1] = (uint8_t)(value & 0xFF);
        value >>= 8;
    }
}

static uint64_t bytes_to_uint64(const uint8_t *bytes, uint8_t size) {
    uint64_t value = 0;
    for (uint8_t i = 0; i < size; ++i) {
        value = (value << 8) | bytes[i];
    }
    return value;
}

uint64_t read_uint64(const char *filename) {
    if (filename == NULL) return 0;
    FILE *file = fopen(filename, "rb");
    if (file == NULL) return 0;
    uint8_t bytes[8];
    if (fread(bytes, 1, 8, file) != 8) {
        fclose(file);
        return 0;
    }
    fclose(file);
    return bytes_to_uint64(bytes, 8);
}

void write_uint64(const char *filename, uint64_t value) {
    if (filename == NULL) return;
    FILE *file = fopen(filename, "wb");
    if (file == NULL) return;
    uint8_t bytes[8];
    uint64_to_bytes(value, bytes, 8);
    fwrite(bytes, 1, 8, file);
    fclose(file);
}

FILE *open_blocks_write(const char *filename) {
    if (filename == NULL) return NULL;
    return fopen(filename, "wb");
}

bool write_block(FILE *file, const DataBlock *block) {
    if (file == NULL || block == NULL || block->data_size == 0 || block->data_size > 64 || block->data_size % 8 != 0) return false;
    uint8_t bytes[8];
    uint64_to_bytes(block->data, bytes, block->data_size/8);
    return fwrite(bytes, 1, block->data_size/8, file) == block->data_size/8;
}

void close_blocks(FILE *file) {
    if (file != NULL) fclose(file);
}

FILE *open_blocks_read(const char *filename) {
    if (filename == NULL) return NULL;
    return fopen(filename, "rb");
}

bool read_block(FILE *file, DataBlock *block) {
    if (file == NULL || block == NULL || block->data_size == 0 || block->data_size > 64 || block->data_size % 8 != 0) return false;
    uint8_t bytes[8] = {0};
    uint8_t bytes_read = fread(bytes, 1, block->data_size/8, file);
    if (bytes_read == 0) return false;
    block->data = bytes_to_uint64(bytes, bytes_read);
    block->data_size = bytes_read * 8;
    return true;
}
