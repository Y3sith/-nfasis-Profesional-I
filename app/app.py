import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppass"),
    )

@app.route("/")
def index():
    return jsonify(mensaje="Contenedor web funcionando")

@app.route("/db")
def db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify(mensaje="Conexion exitosa con el contenedor de base de datos", version=version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)