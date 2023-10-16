from Crypto.Cipher import AES
import base64

def pkcs7_unpad(data):
    return data[:-data[-1]]

def b_p_inv(data):
    l = [4, 1, 3, 0, 2, 7, 6, 5, 10, 9, 8, 11, 15, 14, 13, 12, 19, 18, 17, 16, 23, 22, 21, 20, 27, 26, 25, 24, 31, 30, 29, 28]
    y = bytearray(32)
    for i, index in enumerate(l):
        if i < len(data):
            y[i] = data[index]
    return bytes(y)

encrypted_data = base64.b64decode(open('challenge_file.txt', 'r').read().encode('utf-8'))

iv = b'\x00' * 16

cn = AES.new(iv, AES.MODE_CBC, iv)
decrypted_k = cn.decrypt(encrypted_data)
k = pkcs7_unpad(decrypted_k)

c = AES.new(iv, AES.MODE_ECB)
decrypted_fp = c.decrypt(k)
flag = b_p_inv(pkcs7_unpad(decrypted_fp))

print(flag.decode('utf-8'))
