import pandas as pd

NUM_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]

def preprocess_input(input_data: dict, encoders: dict, scalers: dict) -> pd.DataFrame:
    df = pd.DataFrame([input_data])

    # TotalCharges kadang string/blank
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)

    # label encode categorical
    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = df[col].astype(str)
            df[col] = df[col].apply(lambda x: encoder.transform([x])[0] if x in encoder.classes_ else 0)

    # scale numeric
    df[NUM_COLS] = scalers["StandardScaler"].transform(df[NUM_COLS])

    return df
