#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>

#define MEMORY_SIZE 16384 // 16KB of memory
#define STACK_SIZE 1024   // Stack size
#define NUM_REGISTERS 4   // Number of registers
#define INSTRUCTION_SIZE 4 // Each instruction is 4 bytes

typedef enum {
    NOP = 0,   // No operation
    PUSH = 1,      // Push value to stack
    POP = 2,       // Pop value from stack
    ADD = 3 ,       // Add top two values
    SUB =4,       // Subtract top two values
    MUL=5,       // Multiply top two values
    DIV=6,       // Divide top two values
    MOV=7,       // Move value to register
    PRINT=8,     // Print string
    READ=9,      // Read input to memory
    HALT=11,      // Stop the virtual machine
    COMPARE=12    // Compare top two values on stack
} Instruction;

typedef struct {
    uint8_t memory[MEMORY_SIZE];  // Memory for the VM
    int32_t registers[NUM_REGISTERS]; // Registers
    int32_t stack[STACK_SIZE];    // Stack
    int stack_pointer;            // Stack pointer
    int instruction_pointer;      // Instruction pointer
    int running;                  // VM running status
} VM;

// Push value to the stack
void push(VM *vm, int32_t value) {
    if (vm->stack_pointer >= STACK_SIZE) {
        printf("Stack overflow\n");
        vm->running = 0;
        return;
    }
    vm->stack[vm->stack_pointer++] = value;
}

// Pop value from the stack
int32_t pop(VM *vm) {
    if (vm->stack_pointer <= 0) {
        printf("Stack underflow\n");
        vm->running = 0;
        return 0;
    }
    return vm->stack[--vm->stack_pointer];
}

// Execute an instruction
void execute(VM *vm, uint32_t instruction) {
    uint8_t opcode = instruction >> 24;
    uint8_t reg = (instruction >> 16) & 0xFF;
    int32_t value = instruction & 0xFFFF;

    switch (opcode) {
        case NOP:
            break;
        case PUSH:
            push(vm, value);
            break;
        case POP:
            vm->registers[reg] = pop(vm);
            break;
        case ADD: {
            int32_t a = pop(vm);
            int32_t b = pop(vm);
            push(vm, a + b);
            break;
        }
        case SUB: {
            int32_t a = pop(vm);
            int32_t b = pop(vm);
            push(vm, a - b);
            break;
        }
        case MUL: {
            int32_t a = pop(vm);
            int32_t b = pop(vm);
            push(vm, a * b);
            break;
        }
        case DIV: {
            int32_t a = pop(vm);
            int32_t b = pop(vm);
            if (b == 0) {
                printf("Division by zero\n");
                vm->running = 0;
            } else {
                push(vm, a / b);
            }
            break;
        }
        case MOV:
            vm->registers[reg] = value;
            break;
        case PRINT: {
            printf("%s\n", &vm->memory[value]);
            break;
        }
        case READ: {
            unsigned char buf[4];
            read(0,buf,1);
            push(vm, buf[0]);
            break;
        }
        case COMPARE: {
            int32_t a = pop(vm);
            int32_t b = pop(vm);
            if (a != b) {
                vm->running = 0; // Stop the VM if comparison fails
            }
            break;
        }
        case HALT:
            vm->running = 0;
            break;
        default:
            printf("Unknown instruction: %d\n", opcode);
            vm->running = 0;
            break;
    }
}

// Load a program into the VM's memory
void load_program(VM *vm, uint32_t *program, size_t size) {
    memcpy(vm->memory, program, size * sizeof(uint32_t));
}

// Run the virtual machine
void run(VM *vm) {
    while (vm->running) {
        uint32_t instruction = *(uint32_t*)&vm->memory[vm->instruction_pointer];
        vm->instruction_pointer += INSTRUCTION_SIZE;
        execute(vm, instruction);
    }
}

// Initialize the virtual machine
void init_vm(VM *vm) {
    memset(vm, 0, sizeof(VM));
    vm->stack_pointer = 0;
    vm->instruction_pointer = 0;
    vm->running = 1;
}

int main() {
    VM vm;
    init_vm(&vm);
    
    // Secret string to compare against
    char secret[] = "Correct!";
    memcpy(&vm.memory[1000], secret, sizeof(secret));
    
    // Load the program from a binary file
    FILE *program_file = fopen("not_another_vm.prog", "rb");
    if (!program_file) {
        printf("Failed to open the program file\n");
        return 1;
    }
    
    fseek(program_file, 0, SEEK_END);
    size_t program_size = ftell(program_file);
    rewind(program_file);
    fread(vm.memory, 1, program_size, program_file);
    fclose(program_file);
    
    // Run the VM
    run(&vm);

    printf("VM terminated.\n");
    
    return 0;
}
