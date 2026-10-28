#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include "des.h"


uint64_t read_uint64(const char *filename);
void write_uint64(const char *filename, uint64_t value);

FILE *open_blocks_write(const char *filename);
bool write_block(FILE *file, const DataBlock *block);

FILE *open_blocks_read(const char *filename);
bool read_block(FILE *file, DataBlock *block);

void close_blocks(FILE *file);
