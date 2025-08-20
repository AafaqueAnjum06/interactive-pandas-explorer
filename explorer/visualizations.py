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

import seaborn as sns
import matplotlib.pyplot as plt

def boxplot(df, col):
    """
    Plot a boxplot for a numeric column.
    """
    if col not in df.columns:
        print(f"Column {col} not found in DataFrame.")
        return
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

def violinplot(df, col):
    """
    Plot a violin plot for a numeric column.
    """
    if col not in df.columns:
        print(f"Column {col} not found in DataFrame.")
        return
    sns.violinplot(y=df[col])
    plt.title(f'Violin plot of {col}')
    plt.show()

def pairplot(df):
    """
    Plot pairplot for the DataFrame.
    """
    if df.empty:
        print("DataFrame is empty, cannot plot pairplot.")
        return
    sns.pairplot(df)
    plt.show()

def scatter_plot(df, x_col, y_col):
    """
    Plot a scatter plot for two numeric columns.
    """
    if x_col not in df.columns or y_col not in df.columns:
        print(f"Columns {x_col} or {y_col} not found in DataFrame.")
        return
    sns.scatterplot(data=df, x=x_col, y=y_col)
    plt.title(f'Scatter plot of {x_col} vs {y_col}')
    plt.show()