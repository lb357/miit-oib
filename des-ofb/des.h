#include "datablock.h"

#define IP_SIZE 64
#define E_SIZE 48
#define P_SIZE 32
#define S_ROWS 4
#define S_COLUMNS 16
#define S_COUNT 8
#define PC1_PART_SIZE 28
#define PC2_SIZE 48
#define KS_SIZE 16
#define KEY_SIZE 64

DataBlock des_encrypt(DataBlock *block, DataBlock *key);
DataBlock des_decrypt(DataBlock *block, DataBlock *key);
void ks(DataBlock *input_key, DataBlock output_scheduled_keys[KS_SIZE]);
bool is_key_valid(DataBlock *key);
