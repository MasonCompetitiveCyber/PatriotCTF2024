# Write Up for "AI? PRNG"

We get two files:
1. ai_rnd
2. random_numbers.txt

The first is a binary that *has symbols* and the second is a list of hex digits

## Reverse Engineering ai_rnd
When we open the binary up in Ghidra and go to `main`*` we can see that the program:

1. reads in 32 bytes to a buffer from `stdin`
2. calls `init()` on some pointer and then 
3. In a loop, calls `rand_char` on the pointer and prices out the result
4. calls a clean up function on that pointer

That pointer is probably a struct that keeps track of the internal PRNG state, so we'll call it `prng`. The input might be a seed to the PRNG.

*random_numbers.txt* makes more sense now, it's the output of the program, i.e. a bunch of randomly generated numbers.

### init()
`init()` appears to do these things:

1. allocate a buffer
2. copies into the allocated buffer and repeats the existing data until the buffer fills
3. calls `scramble` with the `prng` struct

### scramble()
`scramble` appears to do the follow

1. allocate a buffer
2. Indirect jump to some table of functions called `schedule` based on the values in an array inside of `prng`
3. sets the buffer to the return value of each indirectly called function
4. returns the buffer back up to `init` which assigns it to a member of `prng`

When we look at `schedule` there is a enormous number of functions, mostly the same function in that table


### Dynamic Analysis
Here, we need to start tracing what data is going where.

1. Run the program
2. Give it some string input
3. Break at the loop in `scramble()`
4. Notice that each byte in the parameter of `scramble` indexes `schedule` and the parameters to the functions are the byte in question, and the position in the loop

### rand_char
`rand_char` is cyclically returning values in the scrambled buffer

## Putting it all together
Broadly speaking, the binary is:

1. Taking in user input
2. Repeating it to fill a 32 byte buffer
3. Transformation each byte in the buffer by calling a function that is depending on the byte value and position
4. Returning those bytes when `rand_char` is called

This means:
1. Each Byte in the output is only dependent on itself and its position (i.e. Each value in the array can be treated individually)
2. All the ascii values (128) and positions in the array (32), there are only (4096) possible output values 

## Solution
The goal of the solve script is to calculate all possible 4096 input values and map them to each possible output byte.

1. Setup a Unicorn Emulator and map every function in schedule and all callee functions (`mat_mul` and `det_scalar_mod`)
2. Emulate each function for all possible values it may accept
3. Save all outputs in a dictionary, so we can do a reverse look up of the output to input
4. Iterate through all the values in *random_numbers.txt` and create a list of each possible input that could have generated each byte
5. Examine the list and either
  * Iterate through all possible combinations to find the flag
  * As a Human, look at it and find leet speek flag

The last part can be tricky, but there are ways to reduce the search space.
 * The first 5 bytes are always "pctf" and indicies that could have "}" would denote a possible end of the flag
 * filter out non-printable ascii

 As the Author, I purposly made it so there are 120 combinations.