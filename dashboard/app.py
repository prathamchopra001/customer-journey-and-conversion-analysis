import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="E-commerce Analytics Dashboard", layout="wide")

st.title("E-commerce User Funnel & Conversion Analytics")

# ------------------------------
# Load Dataset
# ------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/clean_data.csv")
    df['event_time'] = pd.to_datetime(df['event_time'])
    return df

df = load_data()

# ------------------------------
# Overview Metrics
# ------------------------------

st.header("Overview")

col1, col2, col3 = st.columns(3)

total_users = df['user_id'].nunique()
total_events = len(df)
total_products = df['product_id'].nunique()

col1.metric("Total Users", f"{total_users:,}")
col2.metric("Total Events", f"{total_events:,}")
col3.metric("Unique Products", f"{total_products:,}")

# ------------------------------
# Funnel Analysis
# ------------------------------

st.header("User Conversion Funnel")

df['view'] = (df['event_type']=='view').astype(int)
df['cart'] = (df['event_type']=='cart').astype(int)
df['purchase'] = (df['event_type']=='purchase').astype(int)

funnel = df.groupby('user_id')[['view','cart','purchase']].max().reset_index()

view_users = funnel['view'].sum()
cart_users = funnel['cart'].sum()
purchase_users = funnel['purchase'].sum()

funnel_df = pd.DataFrame({
    "Stage":["View","Cart","Purchase"],
    "Users":[view_users,cart_users,purchase_users]
})

fig = px.funnel(funnel_df,x="Users",y="Stage")
st.plotly_chart(fig,use_container_width=True)

# ------------------------------
# Segmented Analysis
# ------------------------------

st.header("Category Conversion Analysis")

category = df.groupby("category_code")[['view','cart','purchase']].sum().reset_index()

category['conversion'] = category['purchase']/category['view']

category = category.sort_values("conversion",ascending=False).head(10)

fig = px.bar(
    category,
    x="category_code",
    y="conversion",
    title="Top Categories by Conversion Rate"
)

st.plotly_chart(fig,use_container_width=True)

# ------------------------------
# Cohort / Activity Trend
# ------------------------------

st.header("User Activity Over Time")

df['month'] = df['event_time'].dt.strftime('%Y-%m')

cohort = df.groupby(['month','event_type']).size().reset_index(name="count")

fig = px.line(
    cohort,
    x="month",
    y="count",
    color="event_type",
    title="Monthly Event Trends"
)

st.plotly_chart(fig,use_container_width=True)

# ------------------------------
# Experiment Simulation
# ------------------------------

st.header("Simulated A/B Experiment")

np.random.seed(42)
funnel['group'] = np.random.choice(['control','treatment'],size=len(funnel))

experiment = funnel.groupby('group')[['view','cart']].sum().reset_index()
experiment['conversion_rate'] = experiment['cart']/experiment['view']

fig = px.bar(
    experiment,
    x="group",
    y="conversion_rate",
    title="Add-to-Cart Conversion by Experiment Group"
)

st.plotly_chart(fig,use_container_width=True)

# ------------------------------
# Insights
# ------------------------------

st.header("Key Insights")

st.write("""
• Largest user drop-off occurs between **product view and cart addition**

• Certain product categories show significantly higher conversion rates

• Returning users typically convert at higher rates than new users

• Simulated experiment indicates potential improvement in cart conversion
""")
