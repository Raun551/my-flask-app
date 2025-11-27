from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Hello from CI/CD!",
            "status": "healthy",
            "version": os.getenv("APP_VERSION", "1.0.0"),
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/env")
def environment():
    return jsonify({"environment": os.getenv("ENVIRONMENT", "local")})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
