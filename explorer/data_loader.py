import pandas as pd

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load CSV file into a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return pd.DataFrame()
