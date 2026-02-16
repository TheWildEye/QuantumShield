import time
import json
import os

BASE_DIR = os.path.dirname(__file__)
REPORT_FILE = os.path.join(BASE_DIR, "report.json")


def _load_report():
    try:
        with open(REPORT_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_report(data):
    try:
        with open(REPORT_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass


def measure(operation_name, func, *args, **kwargs):
    """
    Measures execution time of a function.
    Returns the original function result unchanged.
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000.0

    report = _load_report()
    timings = report.get("timings", {})
    timings.setdefault(operation_name, []).append(round(elapsed_ms, 3))
    report["timings"] = timings

    _save_report(report)
    return result
