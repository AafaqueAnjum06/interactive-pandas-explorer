import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(".."))

from explorer.stats import show_summary
from explorer.filters import filter_dataframe
from explorer.visualizations import plot_histograms, plot_correlation_heatmap


def test_show_summary():
    """Test show_summary with a small DataFrame."""
    df = pd.DataFrame({
        "A": [1, 2, 3, None],
        "B": [4, 5, 6, 7]
    })
    show_summary(df)  # Should print stats without errors

def test_filter_dataframe():
    """Test filtering on numeric column."""
    df = pd.DataFrame({
        "Age": [10, 20, 30, 40],
        "Score": [50, 60, 70, 80]
    })
    filtered = filter_dataframe(df, "Age", min_value=20, max_value=30)
    assert filtered.shape[0] == 2  # Only 20 and 30 should remain
    assert filtered["Age"].min() >= 20
    assert filtered["Age"].max() <= 30

def test_visualizations():
    """Test plotting functions (ensure they run without error)."""
    df = pd.DataFrame({
        "X": [1, 2, 3, 4],
        "Y": [4, 3, 2, 1]
    })
    plot_histograms(df)
    plot_correlation_heatmap(df)

if __name__ == "__main__":
    print("Running tests...")
    test_show_summary()
    test_filter_dataframe()
    test_visualizations()
    print("All tests passed!")
# This file contains tests for the core explorer modules.
# It includes tests for data loading, statistics display, filtering, and visualizations.