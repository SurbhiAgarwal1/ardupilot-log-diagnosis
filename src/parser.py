"""src/parser.py - Load and normalize ArduPilot-style CSV logs."""
import pandas as pd

TIMESTAMP_COLS = ["time", "timestamp", "timeus", "time_boot_ms"]

def load_log(file_path: str) -> pd.DataFrame:
    """Read CSV, normalize column names, parse timestamp if present."""
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Failed to read log file: {e}")

    df.columns = [c.strip().lower() for c in df.columns]

    for col in TIMESTAMP_COLS:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
            break

    return df
