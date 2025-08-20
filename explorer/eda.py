from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt

def automated_eda(df: pd.DataFrame):
    print("=== Basic Info ===")
    print(df.info())
    print("\n=== Missing Values ===")
    print(df.isnull().sum())
    print("\n=== Descriptive Statistics ===")
    display(df.describe(include='all'))
    
    print("\n=== Outliers Detection (IQR) ===")
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
        print(f"{col}: {len(outliers)} outliers")
    
    print("\n=== Correlation Matrix ===")
    display(df[numeric_cols].corr())
    print("\n=== Histograms ===")
    for col in numeric_cols:    
        df[col].hist(bins=30, alpha=0.5)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()