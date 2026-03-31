"""src/features.py - Extract key diagnostic features from log dataframe."""
import pandas as pd

def extract_features(df: pd.DataFrame) -> dict:
    """Extract hdop, nsats, voltage, err_flag from dataframe."""
    def col(name):
        return df[name] if name in df.columns else None

    hdop_s = col("hdop")
    nsats_s = col("nsats")
    voltage_s = col("voltage")
    err_s = col("err")

    voltage_drop = None
    if voltage_s is not None and len(voltage_s) > 1:
        voltage_drop = float((voltage_s.diff().dropna()).min())

    return {
        "hdop": float(hdop_s.mean()) if hdop_s is not None else None,
        "nsats": float(nsats_s.mean()) if nsats_s is not None else None,
        "voltage": float(voltage_s.min()) if voltage_s is not None else None,
        "voltage_drop": voltage_drop,
        "err_flag": bool((err_s > 0).any()) if err_s is not None else False,
    }
