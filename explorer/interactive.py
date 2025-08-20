import ipywidgets as widgets
from IPython.display import display
import pandas as pd
from explorer.visualizations import plot_histograms, plot_correlation_heatmap

def interactive_eda(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    cat_cols = df.select_dtypes(include='object').columns.tolist()

    col_dropdown = widgets.Dropdown(options=numeric_cols, description='Numeric Column:')
    
    def update_plot(col):
        plot_histograms(df[[col]])
        plot_correlation_heatmap(df[numeric_cols])
    
    widgets.interactive(update_plot, col=col_dropdown)
    display(col_dropdown)
