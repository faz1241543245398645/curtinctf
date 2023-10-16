from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long
import random
import hashlib
enc_folder = "32411595437849678646243211671030544758585858507474463678322444828159706619638328084506795350455714014545653039715173"

def pkcs7_unpad(data):
    pad = data[-1]
    return data[:-pad]

g = 7
x = 11109871761272186707313749920559391609314864049943716089329850308739848274981163174574586779728080951298251641374993669445207041118824097375920261081696413
B = 11
a = x - 1
key = hashlib.md5(long_to_bytes(pow(B, a, x))).digest()
cipher = AES.new(key, AES.MODE_ECB)
enc_data = int(enc_folder)
enc_bytes = long_to_bytes(enc_data)
decrypted_data = cipher.decrypt(enc_bytes)
unpadded_data = pkcs7_unpad(decrypted_data)

print("Decrypted data: ", unpadded_data)
