import pandas as pd
from IPython.display import display

def ml_feature_summary(df: pd.DataFrame):
    """
    Analyze a DataFrame and suggest features for ML preprocessing.
    
    Args:
        df: pandas DataFrame
    
    Prints:
        - Columns with missing values
        - Categorical and numeric columns
        - Suggested actions for ML preprocessing
    """
    # 1. Missing values
    print("=== Columns with Missing Values ===")
    missing = df.isnull().sum()
    display(missing[missing > 0])
    
    # 2. Categorical and numeric columns
    categorical = df.select_dtypes(include='object').columns.tolist()
    numeric = df.select_dtypes(include='number').columns.tolist()
    
    print("\n=== Categorical Columns ===")
    print(categorical if categorical else "None")
    
    print("\n=== Numeric Columns ===")
    print(numeric if numeric else "None")
    
    # 3. Suggested preprocessing actions
    print("\n=== Suggested Actions ===")
    for col in categorical:
        print(f"- {col}: Consider encoding (One-Hot / LabelEncoder)")
    for col in numeric:
        print(f"- {col}: Consider scaling (StandardScaler / MinMaxScaler)")
    
    # Optional: flag columns with high missing percentage
    high_missing = (df.isnull().sum() / len(df) > 0.3)
    if high_missing.any():
        print("\nColumns with >30% missing values (consider dropping or imputing):")
        print(high_missing[high_missing].index.tolist())
    else:
        print("\nNo columns with >30% missing values.")