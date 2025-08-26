Challenge powershell_obfuscation
Evidence:
Obfuscated.ps1 --- MD5: 43BBAA2BA87BAF630A4CDCB1B7DBFF38
Encrypted_flag.txt ---- MD5: EB7D7E9CA07544001B1757345FFCC84B
Solution:
Looking at the code in Obfuscated.ps1, it is heavily obfuscated to evade detection and make analysis more difficult.

Here is what the code does:
• Downloads the encrypted_flag.txt file from 192.168.126.148
• Saves encrypted_flag.txt to the Downloads folder
• Decrypts encrypted_flag.txt using XOR with the key 73
• Saves the decrypted value to a variable and executes it
To solve this challenge: we can reuse the decrypt function to decrypt the flag. Follow the code below:

$ec27c22d9dfc41e2b8c1496ba437021c = ""
$f61e225cfe1d484981de4988b40df8b4 = G''et-Co''ntent -Path " encrypted_flag.txt" -Raw
$339a18cced14be6bc35c6e7df638925 = 73
foreach ($char in $f61e225cfe1d484981de4988b40df8b4.ToCharArray()) {
$7f1796cab4f94bd5a96ef19bf913ef66 = \[int]\[char]$char
$1add7cad15f14b6ca981d83ac36d224e = \[char]\($7f1796cab4f94bd5a96ef19bf913ef66 -bxor $339a18cced14be6bc35c6e7df638925)
$ec27c22d9dfc41e2b8c1496ba437021c +=      $1add7cad15f14b6ca981d83ac36d224e
}
echo $ec27c22d9dfc41e2b8c1496ba437021c

Paste the above code to powershell, run it and claim the flag:

If you execute the decrypted flag value, you will get the flag but also establish a reverse shell to the attacker’s IP address
Flag:  pecan{0bfusc4t3d_c0d3_st111_w0rks_682374}