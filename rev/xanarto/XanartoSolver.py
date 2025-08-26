enc_message = '〈䕒峔嚶冪䒪䗺𪂪婂➸偔嗬㐂䏤寚☰𴲐㠤'

def decrypt(enc: str):
	enc_list = list(enc)
	
	concat_enc = []
	for char in enc_list:
		concat_enc += [ord(char) // 2]
	print(concat_enc)

decrypt(enc_message)

def decrypt_unconcated(enc: list):
	print("".join([chr(x) for x in enc][::-1]))

decrypt_unconcated([61, 48, 88, 73, 118, 82, 110, 99, 104, 53, 87, 89, 89, 57, 86, 101, 115, 53, 50, 84, 102, 82, 109, 98, 66, 57, 86, 90, 117, 57, 48, 88, 108, 104, 71, 86])

