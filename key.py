def xor_encrypt_decrypt(string, key):
    encrypted = ""
    for i in range(len(string)):
        encrypted += chr(ord(string[i]) ^ key)
    return encrypted

string = "aAhWVtB\ui|Ud`"
key = 31337

encrypted_string = xor_encrypt_decrypt(string, key)
print("Encrypted String:", encrypted_string)
