# Interactive Pandas Data Explorer


A **lightweight, interactive Python toolkit** for exploring and analyzing Pandas DataFrames. Designed to **help beginners and ML practitioners** understand their datasets quickly, while also providing **interactive, automated, and ML-prep ready insights**.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Folder Structure](#folder-structure)
3. [Installation](#installation)
4. [Usage](#usage)

   * Basic Usage
   * Automated EDA
   * Advanced Visualizations
   * ML Feature Suggestions
   * Interactive Widgets
5. [Module Explanation](#module-explanation)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Overview

This project provides a **complete Python package (`explorer`)** for analyzing Pandas DataFrames:

* **Explore datasets visually** with histograms, boxplots, violin plots, pairplots, and correlation heatmaps.
* **Automate EDA** to quickly see missing values, basic stats, outliers, and correlations.
* **Prepare data for ML** by suggesting preprocessing steps for categorical and numeric columns.
* **Interact with data** via widgets for filtering, column selection, and dynamic plotting in Jupyter.

It is perfect for:

* Students learning Pandas
* Data analysts exploring datasets
* ML practitioners preparing features

---

## Folder Structure

```
interactive-pandas-explorer/
│
├── explorer/                   # Main Python package
│   ├── __init__.py
│   ├── data_loader.py           # Load CSV/Excel/JSON datasets
│   ├── stats.py                 # Basic stats (optional, legacy)
│   ├── visualizations.py        # Advanced plots: boxplot, violin, pairplot
│   ├── filters.py               # Interactive filtering (legacy)
│   ├── eda.py                   # Automated EDA
│   ├── ml_prep.py               # ML preprocessing suggestions
│   └── interactive.py           # Interactive widgets for Jupyter
│
├── notebooks/                   # Demo notebooks
│   └── demo_upgraded.ipynb
│
├── tests/                       # Unit tests
│   └── test_stats.py
│
├── requirements.txt             # Dependencies
├── .gitignore                   # Ignore cache, pyc, notebook checkpoints
├── LICENSE                      # MIT License
└── README.md                    # Project overview & instructions
```

---

## Installation

1. **Clone the repo**

```bash
git clone https://github.com/AafaqueAnjum06/interactive-pandas-explorer.git
cd interactive-pandas-explorer
```

2. **Create a virtual environment** (optional but recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Basic Usage

You can use the legacy modules (`stats.py`, `visualizations.py`, `filters.py`) for simple analysis:

```python
from explorer.stats import show_summary
from explorer.visualizations import plot_histograms, plot_correlation_heatmap
from explorer.filters import filter_dataframe
```

---

### 2. Automated EDA

Use `automated_eda()` to get **rich summary reports**:

```python
from explorer.eda import automated_eda
import seaborn as sns

df = sns.load_dataset("titanic")
automated_eda(df)
```

It will print:

* Dataset info & shape
* Missing values
* Descriptive statistics
* Outlier detection (IQR method)
* Correlation matrix

---

### 3. Advanced Visualizations

Generate **boxplots, violin plots, and pairplots**:

```python
from explorer.visualizations import boxplot, violinplot, pairplot

numeric_cols = df.select_dtypes(include='number').columns.tolist()

for col in numeric_cols:
    boxplot(df, col)
    violinplot(df, col)

pairplot(df[numeric_cols])
```

* Shows distributions, outliers, and relationships between numeric columns.

---

### 4. ML Feature Suggestions

Automatically detect features that need **encoding, scaling, or imputation**:

```python
from explorer.ml_prep import ml_feature_summary

ml_feature_summary(df)
```

Outputs:

* Columns with missing values
* Categorical & numeric columns
* Suggested preprocessing steps
* Columns with >30% missing values flagged

---

### 5. Interactive Widgets

Use `interactive_eda()` in Jupyter to **explore your dataset dynamically**:

```python
from explorer.interactive import interactive_eda

interactive_eda(df)
```

* Select numeric columns from a dropdown
* Filter by min/max using sliders
* Plots update automatically
* Great for exploring large datasets without writing extra code

---

## Module Explanation

| Module              | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| `data_loader.py`    | Load CSV, Excel, JSON datasets                               |
| `stats.py`          | Legacy module for basic stats                                |
| `visualizations.py` | Advanced plotting: boxplot, violinplot, pairplot             |
| `filters.py`        | Legacy filtering functions                                   |
| `eda.py`            | Automated EDA: stats, missing values, outliers, correlations |
| `ml_prep.py`        | Suggest ML preprocessing steps                               |
| `interactive.py`    | Jupyter widgets for interactive exploration                  |

---

## Testing

Run unit tests to ensure all modules work:

```bash
python -m tests.test_stats
```

Expected output:

```
Running tests...
All tests passed!
```

---

## License

MIT License – see [LICENSE](LICENSE) for details.
