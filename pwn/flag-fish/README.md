# Flag Fish
Bjarne is hunting for the coveted flag fish. His first `try` was unsuccessful, can you help him `catch` it this time?

## Solution
1. Read the source code and disassemble the binary.
    1. Open `main.cpp` in your favourite editor and disassemble `chall` with your favourite disassembler.

    2. Read `main`.
        - There are two exception handlers which both handle exceptions of type `fish`.
        - If an exception of type `fish` is thrown in the first try block, then the first exception handler is called which calls `win`.
        - If an exception of type `fish` is thrown in the second try block, then the second exception handler is called which does nothing useful.

    3. Read `first_try`.
        - No exceptions are thrown, meaning that no exception is ever handled and `win` is never called.

    4. Read `second_try`.
        - There is a 32 byte stack buffer `buf`.
        - `buf` can be overflowed through a call to `getline` which reads 512 bytes into it.
        - Finally, an exception of type `fish` is thrown.
        - Even though the return address can be overwritten, the function never actually executes a `ret` instruction and returns.

2. Understand the significance of the return address in the exception handling mechanism.
    - The comments in `second_try` suggest that the return address is significant in exception handling. Research why this is the case.
    - When an exception is thrown, the return address is one of the things used to determine which exception handler to call.
    - At a high level, each function has an associated exception handler. If we can overwrite the return address, then we can confuse the exception handling mechanism and call a different exception handler.

3. Confuse the exception handling mechanism.
    - Concretely, if we overwrite the return address to any address within the first try block, then we can confuse the exception handling mechanism to call the first exception handler.
    - Use the disassembly to find the addresses of these instructions. Since the binary isn't position independent, these addresses will always be the same.
    - Overflow the buffer to overwrite the return addresses with one of the addresses found before.
