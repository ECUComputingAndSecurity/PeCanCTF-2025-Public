# Too Many Flags

## Author
Chelsea Pritchard (`dotefekts`)

## Flag
`pecan{r3d_h3rr1ng_h4sh3s}`

## Participant Description
We've found this file full of flags but we don't know which one is the right one! Can you figure out how these flags were generated and find the right one?

## Private Description
Particpants will be provided with a file full of fakes flags and a python script used to generate them. The hashes are ultimately red herrings, only used to hide a character from the flag within each one. Participants must reverse the function from the `flag_gen.py` script to obtain the original flag.

## Files for Participants
Participants should be provided with the `flags.txt` file containing the obfuscated flag, and the `flag_gen.py` file containing the generation code.

## Solution
Examining the generation function reveals that the seed of the random number generator can be obtained from the number of flags in the provided file. Reversing the function only requires seeding the random number generator with this length and then from each fake flag, obtaining the modified bit and setting this in the result. An example python script to complete this is included in `solution.py`.