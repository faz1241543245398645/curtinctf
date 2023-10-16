import random

p = 137
q = 11

alice_secret = random.randint(1, q - 1)
bob_secret = random.randint(1, q - 1)
alice_shared_key = pow(p, alice_secret, q)
bob_shared_key = pow(p, bob_secret, q)
def obfuscate_key(shared_key):
    obfuscated_key = shared_key.to_bytes((shared_key.bit_length() + 7) // 8, byteorder='big')
    return int.from_bytes([x ^ 0xFF for x in obfuscated_key], byteorder='big')

obfuscated_alice_key = obfuscate_key(alice_shared_key)
flag = "REDACTED"
flag_bytes = bytes(flag, 'utf-8')

encrypted_flag = int.from_bytes(flag_bytes, byteorder='big') ^ obfuscated_alice_key
print(f"Encrypted Flag (as Long Integer): {encrypted_flag}")
