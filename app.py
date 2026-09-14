import os
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.envoron.get("DB_HOST", "not-set")
DB_NAME = os.envoron.get("DB_NAME", "not-set")
DB_USER = os.envoron.get("DB_USER", "not-set")

@app.route("/")
def index():
    return jsonify({
        "message": "Hello from Task in Kubernetes!",
        "db_host": DB_HOST,
        "db_name": DB_NAME,
        "db_user": DB_USER
    })
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=8000)