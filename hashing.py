import hashlib

def sha256_de_archivo(flujo):
    h = hashlib.sha256()
    for bloque in iter(lambda: flujo.read(8192), b""):
        h.update(bloque)
    return h.hexdigest()