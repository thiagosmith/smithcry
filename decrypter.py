import os
import pyaes

## abrir o arquivo criptografado
file_name = "smith.txt.5m1thcry"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"5m1thcryransonwr"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "smith.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
