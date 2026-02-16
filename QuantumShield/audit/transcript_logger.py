import json
import os
import datetime
import uuid

# Directory where audit transcripts are stored
BASE_DIR = os.path.dirname(__file__)
TRANSCRIPT_DIR = os.path.join(BASE_DIR, "transcripts")


def _ensure_dir():
    """
    Ensure transcript directory exists.
    Fail silently if it cannot be created.
    """
    try:
        os.makedirs(TRANSCRIPT_DIR, exist_ok=True)
    except Exception:
        pass


def log_event(event_type, metadata):
    """
    Logs a security-relevant event.

    Parameters:
    - event_type (str): e.g. 'kem_handshake', 'token_issued'
    - metadata (dict): non-sensitive contextual information

    This function MUST NOT raise exceptions.
    """
    try:
        _ensure_dir()

        record = {
            "id": str(uuid.uuid4()),
            "event_type": event_type,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "metadata": metadata
        }

        filename = f"{record['timestamp']}_{event_type}.json"
        path = os.path.join(TRANSCRIPT_DIR, filename)

        with open(path, "w") as f:
            json.dump(record, f, indent=2)

    except Exception:
        # Fail-open: auditing must never affect core logic
        pass
