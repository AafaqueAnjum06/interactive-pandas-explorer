import pandas as pd
from explorer.stats import show_summary

def test_show_summary():
    df = pd.DataFrame({
        "A": [1, 2, 3, None],
        "B": [4, 5, 6, 7]
    })
    show_summary(df)

if __name__ == "__main__":
    test_show_summary()
