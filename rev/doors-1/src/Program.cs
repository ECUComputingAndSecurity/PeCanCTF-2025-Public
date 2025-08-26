using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json;


namespace pecanCTF_Rev_Chals
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach (var name in Assembly.GetExecutingAssembly().GetManifestResourceNames())
            {
                Console.WriteLine("Found embedded resource: " + name);
            }

            //TODO:: Put a flag in string that has no obfuscation
            string plainFlag = "pecan{strings_arent_secure}";
            if (System.Diagnostics.Debugger.IsAttached)
            {
                DetectedDebugger();
                Console.WriteLine(plainFlag);
            }
            Console.WriteLine("Welcome to the Keygen Challenge!");
            Console.Write("Enter your username: ");
            string username = Console.ReadLine();

            Console.Write("Enter your license key: ");
            string inputKey = Console.ReadLine();

            string salt = GetObfuscatedSalt();
            bool validKeyInput = IsValidKey(username, inputKey, salt);
            if (validKeyInput)
            {
                Console.WriteLine("Activation successful!");
                Console.WriteLine($"Here is your flag: {FlagLoader.GetFlag("valid_keygen")}");
                Console.WriteLine("Press Enter to continue");
                Console.ReadLine();
                if (!validKeyInput)
                {
                    Console.WriteLine("You shouldn't be in here!");
                    Console.WriteLine("It's dangerous to go alone, take this:");
                    Console.WriteLine(FlagLoader.GetFlag("bypass_detected"));
                    Console.WriteLine("Press Enter to continue");
                    Console.ReadLine();
                }
            }
            else
            {

                Console.WriteLine("Activation failed.");
                Console.ReadKey();
            }
        }

        // Obfuscated salt using XOR encoding
        static string GetObfuscatedSalt()
        {
            byte[] xored = new byte[] { 0x50, 0x10, 0x40, 0x51, 0x10, 0x57, 0x7C, 0x50, 0x63, 0x4F, 0x57 };
            byte key = 0x23;
            byte[] result = new byte[xored.Length];
            for (int i = 0; i < xored.Length; i++)
            {
                result[i] = (byte)(xored[i] ^ key);
            }
            return Encoding.ASCII.GetString(result); // => "s3cr3t_s@lt"
        }

        static bool IsValidKey(string username, string inputKey, string salt)
        {

            byte[] decoded = Convert.FromBase64String(inputKey);
            string result = Encoding.UTF8.GetString(decoded);
            return result == username + salt;

        }

        static void DetectedDebugger()
        {
            Console.WriteLine("Got To Try Harder Than That!");
            throw new Exception("Debugger not allowed!");
        }
    }

    public static class FlagLoader
    {
        private static Dictionary<string, string> encryptedFlags;

        static FlagLoader()
        {
            {
                LoadEncryptedFlags();
            }
        }

        private static void LoadEncryptedFlags()
        {
            {
                var asm = Assembly.GetExecutingAssembly();
                using (var stream = asm.GetManifestResourceStream("pecanCTF_Rev_Chals.flags.dat"))
                using (var reader = new StreamReader(stream))
                {
                    {
                        string json = reader.ReadToEnd();
                        encryptedFlags = JsonSerializer.Deserialize<Dictionary<string, string>>(json);
                    }
                }
            }
        }

        public static string GetFlag(string key)
        {
            {
                if (!encryptedFlags.ContainsKey(key))
                    return "Invalid flag key";

                byte[] encrypted = Convert.FromBase64String(encryptedFlags[key]);
                byte[] aesKey = Encoding.UTF8.GetBytes("SixteenByteKey!!");

                using (Aes aes = Aes.Create())
                {
                    {
                        aes.Mode = CipherMode.ECB;
                        aes.Key = aesKey;
                        aes.Padding = PaddingMode.PKCS7;

                        using (ICryptoTransform decryptor = aes.CreateDecryptor())
                        {
                            {
                                byte[] decrypted = decryptor.TransformFinalBlock(encrypted, 0, encrypted.Length);
                                return Encoding.UTF8.GetString(decrypted);
                            }
                        }
                    }
                }
            }
        }
    }
}
