import pandas as pd

# Load the datasets for each month
dec_2019 = pd.read_csv('data\\2019-Dec.csv')
nov_2019 = pd.read_csv('data\\2019-Nov.csv')
oct_2019 = pd.read_csv('data\\2019-Oct.csv')
jan_2020 = pd.read_csv('data\\2020-Jan.csv')
feb_2020 = pd.read_csv('data\\2020-Feb.csv')


# Concatenate the datasets
data = pd.concat([dec_2019, nov_2019, oct_2019, jan_2020, feb_2020], ignore_index=True)
data.to_csv('data\\raw_data.csv', index=False)

# convert time to datetime format
data["event_time"] = pd.to_datetime(data["event_time"])

# handle missing values
data = data.dropna(subset=["user_session"])
data["category_code"] = data["category_code"].fillna("Unknown")
data['brand'] = data['brand'].fillna("unknown")
data = data.sort_values(by="event_time")

# drop duplicates
data.duplicated().sum()
data = data.drop_duplicates()

data.isnull().sum()

clean_data = data.to_csv('data\\clean_data.csv', index=False)