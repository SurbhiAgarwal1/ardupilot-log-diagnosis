"""app.py - CLI entry point for AI-Assisted Log Diagnosis."""
import sys
import json
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from parser import load_log
from features import extract_features
from rules import evaluate_rules
from scorer import compute_score
from report import generate_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_csv>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        df = load_log(file_path)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    features = extract_features(df)
    rule_results = evaluate_rules(features)
    score_result = compute_score(rule_results)
    report = generate_report(score_result)

    print(json.dumps(report, indent=2))

    os.makedirs("outputs/reports", exist_ok=True)
    with open("outputs/reports/diagnosis.json", "w") as f:
        json.dump(report, f, indent=2)

    print("\n[Saved to outputs/reports/diagnosis.json]")

if __name__ == "__main__":
    main()
