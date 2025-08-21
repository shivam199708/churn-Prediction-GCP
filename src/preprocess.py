import pandas as pd
import os

# ----------------------------
# Parameters
INPUT_PATH = "data/expanded/expanded_ga_sessions.csv"
OUTPUT_PATH = "data/processed/processed_ga_sessions.csv"
NA_THRESHOLD = 0.7

def main():
    # ----------------------------
    # 1. Load Data
    df = pd.read_csv(INPUT_PATH)
    print(f"Data loaded. Shape: {df.shape}")

    # ----------------------------
    # 2. Drop columns with >70% nulls
    na_frac = df.isna().mean()
    drop_na_cols = na_frac[na_frac > NA_THRESHOLD].index.tolist()
    df.drop(columns=drop_na_cols, inplace=True)
    print(f"Dropped {len(drop_na_cols)} columns with >{int(NA_THRESHOLD*100)}% nulls")

    # ----------------------------
    # 3. Define churn target
    # churn = 1 if totals_transactions == 0 else 0
    if 'totals_transactions' in df.columns:
        df['churn'] = df['totals_transactions'].apply(lambda x: 1 if x == 0 else 0)
    else:
        df['churn'] = 1  # fallback if column is missing

    # ----------------------------
    # 4. Save processed data
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Preprocessed data saved at: {OUTPUT_PATH}")
    print(f"Shape after preprocessing: {df.shape}")

if __name__ == "__main__":
    main()
