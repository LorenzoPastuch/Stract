import pandas as pd
from io import StringIO

def generate_report(data):
    if not data:
        return ""
    df = pd.DataFrame(data)
    df.drop(columns=["id"], errors="ignore", inplace=True)
    csv_output = StringIO()
    df.to_csv(csv_output, index=False)
    return csv_output.getvalue()

def generate_summary(data, group_by):
    if not data:
        return ""
    df = pd.DataFrame(data)
    df.drop(columns=["id", "Ad Name"], errors="ignore", inplace=True)
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df_summary = df.groupby(group_by)[numeric_cols].sum().reset_index()
    csv_output = StringIO()
    df_summary.to_csv(csv_output, index=False)
    return csv_output.getvalue()
