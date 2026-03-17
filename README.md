https://github.com/prathamchopra001/customer-journey-and-conversion-analysis.githttps://github.com/prathamchopra001/customer-journey-and-conversion-analysis.git

# Customer Journey & Conversion Analytics

A comprehensive e-commerce user behavior analysis project using event-level data from a cosmetics shop. This project tracks the user journey from initial product discovery to final purchase, identifying critical drop-off points and high-converting segments.

## 🚀 Project Overview

This project provides an end-to-end data pipeline to:

1. **Download and Preprocess:** Automates the retrieval of large-scale e-commerce datasets from Kaggle.
2. **Analyze Funnels:** Measures conversion rates across multiple stages (View → Cart → Purchase).
3. **Segment Behavior:** Identifies top-performing categories and brands.
4. **Visualize Trends:** Monitors user activity over time.
5. **Interactive Dashboard:** A Streamlit-based application for real-time data exploration.

## 📊 Dataset

The project utilizes the [e-commerce-events-history-in-cosmetics-shop](https://www.kaggle.com/mkechinov/ecommerce-events-history-in-cosmetics-shop) dataset, which includes millions of user actions (view, cart, purchase, remove_from_cart).

## 📁 Directory Structure

```text
├── dashboard/
│   └── app.py                  # Streamlit Dashboard application
├── data/                       # Raw and cleaned datasets (generated)
├── notebooks/
│   └── exploration.ipynb       # Exploratory Data Analysis (EDA)
├── output/
│   └── images/                 # Exported visualizations and insights
├── src/
│   ├── download_data.py        # Dataset downloader using kagglehub
│   ├── data_cleaning.py        # Data preprocessing and cleaning pipeline
│   ├── funnel_analysis.py      # Core conversion funnel logic
│   ├── segmentation_analysis.py # Conversion by category and brand
│   ├── cohort_analysis.py       # (Placeholder) Cohort analysis
│   └── statistical_tests.py     # A/B testing and statistical analysis
└── requirements.txt            # Project dependencies
```

## 🛠️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/prathamchopra001/customer-journey-and-conversion-analysis.git
cd customer-journey-conversion-analytics
```

### 2. Install dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Initialize Data

Run the following scripts in order to download and prepare the data:

```bash
python src/download_data.py
python src/data_cleaning.py
```

## 📈 Running the Analysis

### Conversion Funnel

To generate the overall funnel analysis and save visualizations:

```bash
python src/funnel_analysis.py
```

### Segmentation Analysis

To analyze conversion rates by brand and category:

```bash
python src/segmentation_analysis.py
```

### Launch Interactive Dashboard

Run the Streamlit app to explore data interactively:

```bash
streamlit run dashboard/app.py
```

## 💡 Key Features & Insights

- **Multi-Stage Funnel:** Identifies the largest user drop-offs (e.g., View to Cart).
- **Segment Insights:** Highlights which product categories (e.g., body care, makeup) have the highest "purchase intent."
- **Trend Analysis:** Tracks monthly user activity fluctuations.
- **Experimental Simulation:** Includes logic for simulating and analyzing A/B experiments on conversion rates.

## 🔧 Technologies Used

- **Python** (Pandas, NumPy)
- **Visualization:** Plotly, Seaborn
- **Dashboard:** Streamlit
- **Data Source:** Kaggle Hub
- **Export:** Kaleido (for image generation)
