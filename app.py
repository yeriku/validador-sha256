from flask import Flask, render_template, request
from dotenv import load_dotenv
from hashing import sha256_de_archivo
from virustotal import consultar_virustotal

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        archivo = request.files["archivo"]
        hash_calculado = sha256_de_archivo(archivo.stream)

        referencia = request.form.get("referencia", "").strip().lower()

        archivo2 = request.files.get("archivo2")
        if archivo2 and archivo2.filename:
            referencia = sha256_de_archivo(archivo2.stream)

        veredicto = None
        if referencia:
            veredicto = "ok" if hash_calculado == referencia else "modificado"

        resultado = {
            "nombre": archivo.filename,
            "hash": hash_calculado,
            "referencia": referencia,
            "veredicto": veredicto,
            "vt": consultar_virustotal(hash_calculado),
        }

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)