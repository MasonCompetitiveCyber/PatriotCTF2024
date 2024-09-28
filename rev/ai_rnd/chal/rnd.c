#include "schedule.h"

typedef struct PRNG 
{
    unsigned char* seed;
    unsigned char* state;
    int count;
} PRNG;

unsigned char rand_char(PRNG* prng)
{
    unsigned char output = prng->state[prng->count];
    prng->count++;
    prng->count = prng->count % OUTPUT_LEN;

    return output;
}

unsigned char* scramble(char* seed)
{
    int i;
    unsigned char (*transformation)(unsigned char, unsigned char);
    unsigned char* output = (unsigned char*) malloc(sizeof(unsigned char) * OUTPUT_LEN);
    if (output == NULL)
    {
        printf("Failed to allocate memory\n");
        exit(1);
    }

    for (i = 0; i < SEED_LEN; i++)
    {
        transformation = schedule[seed[i]];
        output[i] = transformation((unsigned char)seed[i], (unsigned char)i);
    }

    return output;
}

void init(PRNG* prng, char* seed, int len)
{
    int original_len = len;
    int i;

    // Expand the str to 32 bytes of data by just repeating it until
    // it doesnt fit into a 32 byte buffer
    // Also we throw out the null byte
    // treating this as data not a string per-say
    prng->count = 0;
    prng->seed = (char*) malloc(sizeof(char) * SEED_LEN);
    if (prng->seed == NULL)
    {
        printf("Failed to allocate memory\n");
        exit(1);
    }
    strncpy(prng->seed, seed, len);

    i = 0;
    while (len < SEED_LEN)
    {
        prng->seed[len] = prng->seed[i];
        len++;
        i++;
        if (i == original_len)
            i = 0;
    }

    prng->state = scramble(prng->seed);
}

void dispose(PRNG* prng)
{
    free(prng->seed);
    free(prng->state);
}


int main(int argc, char** argv)
{
    // Prompt for the seed/flag
    char input[INPUT_LEN];
    char* output;
    int size;
    int i;

    fgets(input, INPUT_LEN, stdin);    
    size = strlen(input);

    PRNG prng;
    init(&prng, input, size);

    for(i = 0; i < OUTPUT_LEN; i++)
    {
        printf("%02x ", rand_char(&prng));
    }

    dispose(&prng);
    return 0;
}