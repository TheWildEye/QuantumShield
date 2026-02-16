import json
import csv
import os

BASE_DIR = os.path.dirname(__file__)
STATE_FILE = os.path.join(BASE_DIR, "runtime_state.json")
EVENTS_FILE = os.path.join(BASE_DIR, "events.json")


def export_json(path="security_report.json"):
    report = {
        "runtime_state": {},
        "events": []
    }

    try:
        with open(STATE_FILE) as f:
            report["runtime_state"] = json.load(f)
        with open(EVENTS_FILE) as f:
            report["events"] = json.load(f)

        with open(path, "w") as f:
            json.dump(report, f, indent=2)
    except Exception:
        pass


def export_csv(path="security_report.csv"):
    try:
        with open(EVENTS_FILE) as f:
            events = json.load(f)

        with open(path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Time", "Category", "Event", "Result", "Severity"])
            for e in events:
                writer.writerow([
                    e["time"],
                    e["category"],
                    e["event"],
                    e["result"],
                    e.get("severity", "")
                ])
    except Exception:
        pass
