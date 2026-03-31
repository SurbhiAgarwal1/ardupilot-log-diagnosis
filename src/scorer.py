"""src/scorer.py - Pick most likely issue and compute confidence."""

def compute_score(rule_results: list) -> dict:
    triggered = [r for r in rule_results if r["triggered"]]

    if not triggered:
        return {"root_cause": "No significant issue detected", "confidence": 0.0, "evidence": []}

    best = max(triggered, key=lambda r: r["score"])

    return {
        "root_cause": best["rule"],
        "confidence": best["score"],
        "evidence": best["evidence"],
        "reason": best["reason"],
    }
