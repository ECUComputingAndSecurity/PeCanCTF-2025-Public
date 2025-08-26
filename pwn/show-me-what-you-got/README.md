# Show Me What You GOT!
Show me what you GOT! I want to see what you GOT!

## Solution
1. Read the source code.
    1. Read `main`.
        - We are able to input two 64-bit unsigned integers `where_you_got` and `what_you_got`.
        - `where_you_got` is treated as a memory address and `what_you_got` is written to it.
        - Therefore, we have a write-what-where condition.

2. Understand what GOT means.
    - The challenge always capitalises *GOT*, maybe it's an acronym.
    - Realise that the Global Offset Table (GOT) is used as an indirection to access position independent executable (PIE) addresses.
    - Realise that the GOT plays a significant role in function address resolution, and changing a GOT entry can change which address a function resolves to.

3. Overwrite GOT entry.
    - Since we have a write-what-where condition we can overwrite a GOT function entry with an arbitrary address.
    - Realise `chall` isn't a PIE so we don't need an address leak.
    - Realise the GOT is writable so we can corrupt its entries.
    - Write the address of `win` to the `puts` GOT entry.
