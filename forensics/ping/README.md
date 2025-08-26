Challenge: Ping
Evidence:
Capture.pcapng --- MD5: ee116bff68604ed2e17df899f51552e4
Solution:
This pcap file captures a ping sequence from IP address 192.168.126.129 to 192.168.126.148. We can observe that the length of each packet is different

We will tshark to extract the data size of each packet from 192.168.126.129 and save the value to a file named ascii_value.txt
tshark -r capture.pcapng -Y "ip.src == 192.168.126.129" -T fields -e data.len > ascii_value.txt

Create a file named decode.py:

result = ""

with open("ascii_value.txt", "r") as file:
for line in file:
number = int(line.strip())
result += chr(number)

print("Decoded string:", result)

run the script and get the flag:

Flag: pecan{d4t4_3xf1ltr4t10n_thr0gh_p1ng_93485}