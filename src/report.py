"""src/report.py - Generate structured diagnosis report."""

SUGGESTIONS = {
    "GPS Issue": "Check antenna placement and ensure clear sky view. Verify GPS module connection.",
    "Power Issue": "Inspect battery health and connections. Check ESC power draw and voltage regulators.",
    "Failsafe Triggered": "Review full log for failsafe cause. Check RC link, geofence, and battery failsafe settings.",
    "No significant issue detected": "No action required. Log appears nominal.",
}

def generate_report(result: dict) -> dict:
    root_cause = result.get("root_cause", "No significant issue detected")
    return {
        "root_cause": root_cause,
        "confidence": result.get("confidence", 0.0),
        "evidence": result.get("evidence", []),
        "suggestion": SUGGESTIONS.get(root_cause, SUGGESTIONS["No significant issue detected"]),
    }
