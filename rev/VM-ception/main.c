#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>

#define MEMORY_SIZE 16384
#define LINKED_LIST_SIZE 256

typedef enum {
    OP_PUSH = 0x01,
    OP_POP,
    OP_ADD,
    OP_SUB,
    OP_CMP,
    OP_JMP,
    OP_PRINT,
    OP_HALT,
    OP_READ,
    OP_FUNKY,
    OP_WIN,
} OpCode;

typedef struct Node {
    int64_t value;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
    int flag;
} LinkedList;

// Function prototypes
void execute_secondary_vm(uint8_t* code, size_t code_size, LinkedList* list);
void execute_primary_vm(uint8_t* code, size_t code_size);

void init_linked_list(LinkedList* list) {
    list->head = NULL;
    list->flag = 0;
}

void push(LinkedList* list, int64_t value) {
    // printf("push : 0x%lx\n",value);
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->value = value;
    new_node->next = list->head;
    list->head = new_node;
}

void l_read(LinkedList* list) {
    int64_t value = 0;
    read(0, (unsigned char *)&value, 1);
    // printf("l_read : %c\n",value);
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->value = value;
    new_node->next = list->head;
    list->head = new_node;
}

int64_t pop(LinkedList* list) {
    if (list->head == NULL) {
        return 0;
    }
    Node* temp = list->head;
    int64_t value = temp->value;
    list->head = list->head->next;
    free(temp);
    // printf("pop : %lx\n",value);
    return value;
}

void add(LinkedList* list) {
    int64_t a = pop(list);
    int64_t b = pop(list);
    // printf("ADD : %lu + %lu = %lu\n",a,b,a+b);
    push(list, a + b);
}

void sub(LinkedList* list) {
    int64_t a = pop(list);
    int64_t b = pop(list);
    // printf("SUB : %lu - %lu = %lu\n",a,b,a-b);
    push(list, a - b);
}

void cmp(LinkedList* list) {
    int64_t a = pop(list);
    int64_t b = pop(list);
    // printf("cmp : %lu == %lu = %d\n",a,b,a==b);
    list->flag = (a == b) ? 1 : 0;
}

void FUNKY(LinkedList* list) {
    int64_t b = pop(list); // input val
    int64_t a = pop(list); // CMP val
    unsigned char byte0 = (a >> 0) & 0xFF;
    unsigned char byte7 = (a >> 56) & 0xFF;

    unsigned char byte1 = (a >> 8) & 0xFF;
    unsigned char byte6 = (a >> 48) & 0xFF;

    unsigned char byte2 = (a >> 0x10) & 0xFF;
    unsigned char byte5 = (a >> 40) & 0xFF;

    unsigned char byte3 = (a >> 0x18) & 0xFF;
    unsigned char byte4 = (a >> 32) & 0xFF;

    // printf("byte0: 0x%02X\n", byte0);
    // printf("byte7: 0x%02X\n", byte7);

    // printf("byte1: 0x%02X\n", byte1);
    // printf("byte6: 0x%02X\n", byte6);

    // printf("byte2: 0x%02X\n", byte2);
    // printf("byte5: 0x%02X\n", byte5);

    // printf("byte3: 0x%02X\n", byte3);
    // printf("byte4: 0x%02X\n", byte4);

    uint64_t value = (byte3 + byte4) + (byte0+byte7) + (byte1+byte6) + (byte2+byte5);
    // printf("value: %c\n", value);


    // printf("[f] FUNK : %lu == %lu = %d\n",value,b,value==b);
    // list->flag = (a == b) ? 1 : 0;
    list->flag = (value == b) ? 1 : 0;
}

void jmp(uint8_t** pc, int64_t address) {
    *pc = (uint8_t*)address;
}

void execute_secondary_vm(uint8_t* code, size_t code_size, LinkedList* list) {
    uint8_t* pc = code;
    while (pc < code + code_size) {
        OpCode op = *pc++;
        // printf("op %u\n",op);
        switch (op) {
            case OP_PUSH: {
                int64_t value = *(int64_t*)pc;
                pc += sizeof(int64_t);
                push(list, value);
                break;
            }
            case OP_POP:
                pop(list);
                break;
            case OP_ADD:
                add(list);
                break;
            case OP_SUB:
                sub(list);
                break;
            case OP_READ:
                l_read(list);
                break;
            case OP_CMP:
                cmp(list);
                if (list->flag == 1)
                {
                    printf("Fail\n");
                    return;
                }
                break;
            case OP_FUNKY:
                FUNKY(list);
                if (list->flag != 1)
                {
                    printf("Fail\n");
                    return;
                }
                break;
            case OP_JMP: {
                int64_t address = *(int64_t*)pc;
                pc += sizeof(int64_t);
                jmp(&pc, address);
                break;
            }
            case OP_PRINT:
                printf("%ld\n", pop(list));
                break;
            case OP_WIN:
                printf("Correct!\n");
                break;
            case OP_HALT:
                return;
        }
    }
}

void execute_primary_vm(uint8_t* code, size_t code_size) {
    LinkedList list;
    init_linked_list(&list);
    execute_secondary_vm(code, code_size, &list);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    // Read input file
    FILE* file = fopen(argv[1], "rb");
    if (!file) {
        perror("fopen");
        return 1;
    }

    fseek(file, 0, SEEK_END);
    size_t code_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    uint8_t* code = (uint8_t*)malloc(code_size);
    fread(code, 1, code_size, file);
    fclose(file);

    // Execute the primary VM
    execute_primary_vm(code, code_size);

    free(code);
    return 0;
}
