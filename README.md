# AI-Assisted Log Diagnosis System (Prototype)

This project implements a modular, explainable log diagnosis system for ArduPilot-style logs. It analyzes telemetry data and automatically identifies potential root causes of issues along with confidence scores, supporting evidence, and actionable suggestions.
This project moves beyond traditional log inspection by providing structured, explainable diagnosis with confidence scoring and actionable recommendations.
## Overview

The system follows a structured pipeline:

Log Input → Feature Extraction → Rule-Based Detection → Confidence Scoring → Explanation Report

It is designed as a proof-of-concept for an AI-assisted diagnosis system, forming the baseline for future ML-based extensions.

## Features

- Log parsing from structured CSV files
- Feature extraction (HDop, satellite count, voltage, error flags)
- Rule-based detection for:
  - GPS degradation
  - Power anomalies
  - Failsafe events
- Confidence scoring for predicted root cause
- Explainable output with evidence and suggestions
- CLI-based execution with JSON output

## Project Structure

```
log_diagnosis/
├── data/
│   └── raw/sample.csv
├── outputs/
│   └── reports/diagnosis.json
├── src/
│   ├── parser.py
│   ├── features.py
│   ├── rules.py
│   ├── scorer.py
│   └── report.py
├── app.py
├── requirements.txt
└── README.md
```

## Installation

```
pip install -r requirements.txt
```

## Usage

```
python app.py data/raw/sample.csv
```

## Example Output

```
{
  "root_cause": "Failsafe Triggered",
  "confidence": 0.9,
  "evidence": [
    "ERR column contains non-zero value"
  ],
  "suggestion": "Review full log for failsafe cause. Check RC link, geofence, and battery failsafe settings."
}
```

## Future Work

- Machine learning-based classification
- Retrieval of similar historical failures
- SITL-based validation
- API interface for integration

## Purpose

This project serves as a foundation for building an intelligent, explainable log analysis system to reduce debugging effort and improve reliability in autonomous systems.
