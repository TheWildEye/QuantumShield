from flask import Flask, request, jsonify, render_template
import requests

from dashboard.state_updater import log_event, update_state

from dashboard.pdf_exporter import export_pdf

BASE = "http://localhost:8000"

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/export-pdf")
def export_pdf_route():
    export_pdf()
    return "", 200

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/demo/login", methods=["POST"])
def demo_login():
    data = request.json

    try:
        # 1. KEMTLS handshake
        if data.get("handshakefail"):
            log_event("Transport", "KEMTLS handshake failure simulated", "FAIL", "CRITICAL")
            return jsonify({"message": "Handshake failed (simulated)"})

        # Normal success path
        log_event("Transport", "KEMTLS handshake completed", "PASS", "INFO")

        # 2. Token issuance
        r = requests.post(BASE + "/token", json={"data": "x"})
        jwt = r.json()["data"]

        # 3. Simulations
        if data.get("tamper"):
            log_event("Signature", "JWT tampering detected", "FAIL", "CRITICAL")
            update_state(status="crypto_failure", last_failure="JWT tampering")
            return jsonify({"message": "Login failed: JWT tampered"})

        if data.get("keyrotate"):
            log_event("Key Management", "JWKS mismatch detected", "FAIL", "HIGH")
            return jsonify({"message": "Login failed: Key mismatch"})

        if data.get("replay"):
            log_event("Replay", "Token replay detected", "FAIL", "MEDIUM")
            return jsonify({"message": "Login failed: Replay detected"})

        # Success
        log_event("Authentication", "User login successful", "PASS", "INFO")
        return jsonify({"message": "Login successful"})

    except Exception as e:
        log_event("System", "Unexpected demo error", "FAIL", "HIGH")
        return jsonify({"message": "Login failed"})


if __name__ == "__main__":
    app.run(port=9000)
