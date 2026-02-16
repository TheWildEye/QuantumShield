import json
import os

# Paths
BASE_DIR = os.path.dirname(__file__)
AUDIT_DIR = os.path.join(BASE_DIR, "..", "audit", "transcripts")
OUTPUT_FILE = os.path.join(BASE_DIR, "handshake_state.json")


def generate_handshake_state():
    """
    Reads audit transcripts and determines
    which KEMTLS handshake steps have occurred.
    """
    state = {
        "completed_steps": [],
        "last_updated": None
    }

    try:
        files = sorted(os.listdir(AUDIT_DIR))
    except Exception:
        files = []

    for filename in files:
        if not filename.endswith(".json"):
            continue

        try:
            with open(os.path.join(AUDIT_DIR, filename), "r") as f:
                record = json.load(f)

            if record.get("event_type") == "kem_handshake":
                state["completed_steps"] = [1, 2, 3, 4]
                state["last_updated"] = record.get("timestamp")

        except Exception:
            continue

    try:
        with open(OUTPUT_FILE, "w") as f:
            json.dump(state, f, indent=2)
    except Exception:
        pass


if __name__ == "__main__":
    generate_handshake_state()
