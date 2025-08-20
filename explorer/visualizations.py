import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df: pd.DataFrame):
    """
    Plot histograms for numeric columns of the DataFrame.
    """
    if df.empty:
        print("DataFrame is empty, cannot plot histograms.")
        return
    df.hist(figsize=(12, 8))
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df: pd.DataFrame):
    """
    Plot correlation heatmap for numeric columns.
    """
    if df.empty:
        print("DataFrame is empty, cannot plot correlation heatmap.")
        return
    corr = df.corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.show()
