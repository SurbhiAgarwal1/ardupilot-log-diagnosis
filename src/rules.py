"""src/rules.py - Rule-based diagnostics for GPS, Power, and Failsafe issues."""

def evaluate_rules(features: dict) -> list:
    results = []

    # Rule 1: GPS issue
    hdop = features.get("hdop")
    nsats = features.get("nsats")
    gps_triggered = (hdop is not None and hdop > 2) or (nsats is not None and nsats < 12)
    gps_score = 0.0
    gps_evidence = []
    if hdop is not None and hdop > 2:
        gps_score = max(gps_score, min(1.0, (hdop - 2) / 3))
        gps_evidence.append(f"HDop={hdop:.2f} (threshold: 2)")
    if nsats is not None and nsats < 12:
        gps_score = max(gps_score, min(1.0, (12 - nsats) / 12))
        gps_evidence.append(f"NSats={nsats:.0f} (threshold: 12)")
    results.append({
        "rule": "GPS Issue",
        "triggered": gps_triggered,
        "reason": "Poor GPS signal quality",
        "score": round(gps_score, 2),
        "evidence": gps_evidence,
    })

    # Rule 2: Power issue
    voltage = features.get("voltage")
    voltage_drop = features.get("voltage_drop")
    power_triggered = (voltage is not None and voltage < 10.5) or (voltage_drop is not None and voltage_drop < -1.0)
    power_score = 0.0
    power_evidence = []
    if voltage is not None and voltage < 10.5:
        power_score = max(power_score, min(1.0, (10.5 - voltage) / 5))
        power_evidence.append(f"Min voltage={voltage:.2f}V (threshold: 10.5V)")
    if voltage_drop is not None and voltage_drop < -1.0:
        power_score = max(power_score, min(1.0, abs(voltage_drop) / 5))
        power_evidence.append(f"Voltage drop={voltage_drop:.2f}V")
    results.append({
        "rule": "Power Issue",
        "triggered": power_triggered,
        "reason": "Low or unstable battery voltage",
        "score": round(power_score, 2),
        "evidence": power_evidence,
    })

    # Rule 3: Failsafe
    err_flag = features.get("err_flag", False)
    results.append({
        "rule": "Failsafe Triggered",
        "triggered": err_flag,
        "reason": "ERR flag detected in log",
        "score": 0.9 if err_flag else 0.0,
        "evidence": ["ERR column contains non-zero value"] if err_flag else [],
    })

    return results
