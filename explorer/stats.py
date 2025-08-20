import pandas as pd

def show_summary(df: pd.DataFrame):
    """
    Print basic statistics, missing values, and shape of the DataFrame.
    """
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nStatistics:\n", df.describe(include='all'))
    print("\nData Types:\n", df.dtypes)
    print("\nFirst 5 Rows:\n", df.head())