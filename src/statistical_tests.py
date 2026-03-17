import pandas as pd
from statsmodels.stats.proportion import proportions_ztest


df = pd.read_csv("data\\clean_data.csv")
df["view"] = (df["event_type"] == "view").astype(int)
df['cart'] = (df['event_type'] == 'cart').astype(int)
df['purchase'] = (df['event_type'] == 'purchase').astype(int)
