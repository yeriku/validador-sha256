# Validador de integridad de archivos (SHA-256)

Aplicación web que permite verificar si un archivo conserva su integridad, calculando su hash SHA-256 y comparándolo contra un valor de referencia o contra otro archivo. Además consulta el hash en VirusTotal.

## Problema que resuelve

Permite comprobar de manera confiable si un archivo fue modificado después de ser almacenado, copiado o transmitido, usando una función hash criptográfica (SHA-256).

## Arquitectura

- `app.py`: lógica de la aplicación web (Flask). Recibe el archivo, calcula el hash, compara y consulta VirusTotal.
- `hashing.py`: módulo criptográfico. Calcula el SHA-256 de un archivo leyéndolo en bloques.
- `virustotal.py`: consulta la API de VirusTotal usando el hash calculado.
- `templates/index.html`: interfaz del usuario.

## Tecnologías utilizadas

- Python 3
- Flask
- hashlib (librería estándar de Python)
- API de VirusTotal (v3)
- python-dotenv

## Instrucciones para ejecutar

1. Clonar el repositorio y entrar a la carpeta.
2. Crear un entorno virtual e instalar dependencias:

\`\`\`
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
\`\`\`

3. Copiar `.env.example` a `.env` y colocar una clave de API de VirusTotal (gratuita en virustotal.com):

\`\`\`
VT_API_KEY=tu_clave_aqui
\`\`\`

4. Ejecutar la aplicación:

\`\`\`
python app.py
\`\`\`

5. Abrir `http://127.0.0.1:5000` en el navegador.

## Pruebas realizadas

1. Cálculo de hash de un archivo original.
2. Verificación con el mismo archivo: hashes idénticos, integridad verificada.
3. Verificación con archivo modificado (un carácter cambiado): hash diferente, se detecta la modificación.
4. Consulta del hash en VirusTotal: se muestra si el hash existe o no en su base de datos.

## Nota de seguridad

La clave de API de VirusTotal se lee desde una variable de entorno (`.env`, excluido del repositorio) y nunca queda expuesta en el código fuente.