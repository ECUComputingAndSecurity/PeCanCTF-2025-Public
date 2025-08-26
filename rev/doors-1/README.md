C# in the challenge description indicates that it's a .NET binary, so we need to pick an appropriate decompiler.

1. **Use ILSpy or similar .NET decompiler:**
   - Download ILSpy from <https://github.com/icsharpcode/ILSpy>
   - Open `Doors.exe` in the decompiler
   - Navigate to the main assembly

2. **Examine the Main() method:**
   - Look for string literals in the code
   - The flag will be visible as a plain string constant

3. **Alternative tools:**
   - dotPeek (JetBrains)
   - Reflexil
   - dnSpy

`strings` won't work because the string uses UTF-16LE encoding.
