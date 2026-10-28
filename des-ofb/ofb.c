#include "ofb.h"
#include <errno.h>



bool ofb_encrypt(const char *input_filename, const char *key_filename, const char *output_filename, uint64_t initial_vector) {
    DataBlock key = {
        .data_size = 64,
        .data = read_uint64(key_filename)
    };
    if (!is_key_valid(&key)) {
        errno = EINVAL;
        return false;
    }
    DataBlock kns[KS_SIZE];
    ks(&key, kns);

    FILE *input_file = open_blocks_read(input_filename);
    if (input_file == NULL) {
        close_blocks(input_file);
        return false;
    }

    FILE *output_file = open_blocks_write(output_filename);
    if (output_file == NULL) {
        close_blocks(input_file);
        close_blocks(output_file);
        return false;
    }

    DataBlock oi = {
        .data_size = 64,
        .data = initial_vector
    };
    write_block(output_file, &oi);

    DataBlock input = {
        .data_size = 64,
        .data = 0
    };
    while (read_block(input_file, &input)) {
        oi = des_encrypt(&oi, kns);
        DataBlock output = {
            .data_size = input.data_size,
            .data = input.data ^ (oi.data >> (64 - input.data_size))
        };
        write_block(output_file, &output);
    }
    close_blocks(input_file);
    close_blocks(output_file);
    return true;
}



bool ofb_decrypt(const char *input_filename, const char *key_filename, const char *output_filename) {
    DataBlock key = {
        .data_size = 64,
        .data = read_uint64(key_filename)
    };
    if (!is_key_valid(&key)) {
        errno = EINVAL;
        return false;
    }
    DataBlock kns[KS_SIZE];
    ks(&key, kns);

    FILE *input_file = open_blocks_read(input_filename);
    if (input_file == NULL) {
        close_blocks(input_file);
        return false;
    }

    FILE *output_file = open_blocks_write(output_filename);
    if (output_file == NULL) {
        close_blocks(input_file);
        close_blocks(output_file);
        return false;
    }

    DataBlock oi = {
        .data_size = 64,
        .data = 0
    };
    if (!read_block(input_file, &oi)) {
        close_blocks(input_file);
        return false;
    }

    DataBlock input = {
        .data_size = 64,
        .data = 0
    };
    while (read_block(input_file, &input)) {
        oi = des_encrypt(&oi, kns);
        DataBlock output = {
            .data_size = input.data_size,
            .data = input.data ^ (oi.data >> (64 - input.data_size))
        };
        write_block(output_file, &output);
    }
    close_blocks(input_file);
    close_blocks(output_file);
    return true;
}
