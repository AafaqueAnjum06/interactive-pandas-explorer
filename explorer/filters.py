import pandas as pd

def filter_dataframe(df: pd.DataFrame, column: str, min_value=None, max_value=None) -> pd.DataFrame:
    """
    Filter DataFrame rows based on a column range.
    
    Args:
        df: Input DataFrame
        column: Column name to filter
        min_value: Minimum value (inclusive)
        max_value: Maximum value (inclusive)
    
    Returns:
        Filtered DataFrame
    """
    if column not in df.columns:
        print(f"Column '{column}' not found in DataFrame.")
        return df
    
    filtered = df.copy()
    if min_value is not None:
        filtered = filtered[filtered[column] >= min_value]
    if max_value is not None:
        filtered = filtered[filtered[column] <= max_value]
    
    print(f"Filtered DataFrame: {filtered.shape[0]} rows, {filtered.shape[1]} columns.")
    return filtered
