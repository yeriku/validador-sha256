import os
import requests

def consultar_virustotal(hash_hex):
    enlace = f"https://www.virustotal.com/gui/file/{hash_hex}"
    clave = os.getenv("VT_API_KEY")

    if not clave:
        return {"estado": "sin_clave", "enlace": enlace}

    respuesta = requests.get(
        f"https://www.virustotal.com/api/v3/files/{hash_hex}",
        headers={"x-apikey": clave},
        timeout=15
    )

    if respuesta.status_code == 404:
        return {"estado": "no_existe", "enlace": enlace}

    if respuesta.status_code == 200:
        datos = respuesta.json()["data"]["attributes"]["last_analysis_stats"]
        return {"estado": "encontrado", "stats": datos, "enlace": enlace}

    return {"estado": "error", "codigo": respuesta.status_code, "enlace": enlace}