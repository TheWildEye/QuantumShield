import json
import os
import datetime

BASE_DIR = os.path.dirname(__file__)
MODE_FILE = os.path.join(BASE_DIR, "mode.json")
LOG_FILE = os.path.join(BASE_DIR, "failures.log")

# Optional dashboard updater (FAIL-OPEN)
try:
    from dashboard.state_updater import update_state
except Exception:
    def update_state(**kwargs):
        pass


def _proof_mode_enabled():
    """
    Returns True if cryptographic failure proof mode is enabled.
    Fail-safe: returns False on any error.
    """
    try:
        with open(MODE_FILE, "r") as f:
            data = json.load(f)
            return bool(data.get("enabled", False))
    except Exception:
        return False


def log_failure(reason, context=None):
    """
    Logs a cryptographic failure event if proof mode is enabled.

    Parameters:
    - reason (str): short description of failure
    - context (dict): optional non-sensitive metadata

    This function MUST NEVER raise an exception.
    """

    # Proof mode disabled → do nothing
    if not _proof_mode_enabled():
        return

    try:
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "reason": reason,
            "context": context or {}
        }

        # Append to failure log
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")

        # Update dashboard state (observer-only)
        update_state(
            status="crypto_failure",
            last_failure=reason
        )

    except Exception:
        # Fail-open: never affect authentication
        pass
