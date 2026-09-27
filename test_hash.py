from hashing import sha256_de_archivo

with open("prueba.txt", "rb") as f:
    print(sha256_de_archivo(f))