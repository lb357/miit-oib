#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include "ofb.h"

int main() {
    uint64_t initial_vector = read_uint64("initial_vector.uint64_t");
    while (true) {
        printf("1. Encrypt\n");
        printf("2. Decrypt\n");
        printf("3. Exit\n");
        printf("Select: ");

        int choice;
        scanf("%d", &choice);
        if (choice == 0) break;

        char input_filename[256];
        printf("Input file: ");
        scanf("%255s", input_filename);

        char key_filename[256];
        printf("Key file: ");
        scanf("%255s", key_filename);

        char output_filename[256];
        printf("Output file: ");
        scanf("%255s", output_filename);

        switch (choice) {
            case 1:
                if (!ofb_encrypt(input_filename, key_filename, output_filename, initial_vector)) {
                    perror("Encryption error");
                }
                initial_vector++;
                write_uint64("initial_vector.uint64_t", initial_vector);
                break;
            case 2:
                if (!ofb_decrypt(input_filename, key_filename, output_filename)) {
                    perror("Decryption error");
                }
                break;
            default:
                printf("Unknown action\n");
        }
    }
    return 0;
}
