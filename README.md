# AI-Assisted Log Diagnosis

Minimal prototype for automated ArduPilot-style flight log diagnosis.
Detects GPS, Power, and Failsafe issues using rule-based analysis with confidence scoring.

## How to Run

```bash
pip install -r requirements.txt
python app.py data/raw/sample.csv
```

## Example Output

```json
{
  "root_cause": "Failsafe Triggered",
  "confidence": 0.9,
  "evidence": ["ERR column contains non-zero value"],
  "suggestion": "Review full log for failsafe cause. Check RC link, geofence, and battery failsafe settings."
}
```
