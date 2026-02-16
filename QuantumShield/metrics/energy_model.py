import json
import os

BASE_DIR = os.path.dirname(__file__)
REPORT_FILE = os.path.join(BASE_DIR, "report.json")

# Conservative assumptions (documented)
CPU_AVG_POWER_WATTS = 15.0  # typical laptop / VM CPU
JOULES_PER_MS = CPU_AVG_POWER_WATTS / 1000.0


def _load_report():
    try:
        with open(REPORT_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}


def estimate_energy():
    """
    Estimates energy consumption from timing data.
    """
    report = _load_report()
    timings = report.get("timings", {})

    energy = {}
    for op, values in timings.items():
        total_ms = sum(values)
        joules = total_ms * JOULES_PER_MS
        energy[op] = round(joules, 6)

    report["energy_estimates_joules"] = energy

    try:
        with open(REPORT_FILE, "w") as f:
            json.dump(report, f, indent=2)
    except Exception:
        pass
