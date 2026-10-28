#include "file.h"

bool ofb_encrypt(const char *input_filename, const char *key_filename, const char *output_filename, uint64_t initial_vector);
bool ofb_decrypt(const char *input_filename, const char *key_filename, const char *output_filename);
