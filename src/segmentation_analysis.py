import pandas as pd
import plotly.express as px
import os


df = pd.read_csv("data\\clean_data.csv")


df['view'] = (df['event_type'] == 'view').astype(int)
df['cart'] = (df['event_type'] == 'cart').astype(int)
df['purchase'] = (df['event_type'] == 'purchase').astype(int)


category_funnel = df.groupby('category_code')[['view','cart','purchase']].sum().reset_index()

category_funnel['view_to_cart'] = category_funnel['cart'] / category_funnel['view']
category_funnel['cart_to_purchase'] = category_funnel['purchase'] / category_funnel['cart']
category_funnel['overall_conversion'] = category_funnel['purchase'] / category_funnel['view']

category_funnel = category_funnel.sort_values('overall_conversion', ascending=False)

category_funnel.head(10)


brand_funnel = df.groupby('brand')[['view','cart','purchase']].sum().reset_index()
brand_funnel['view_to_cart'] = brand_funnel['cart'] / brand_funnel['view']
brand_funnel['cart_to_purchase'] = brand_funnel['purchase'] / brand_funnel['cart']
brand_funnel['overall_conversion'] = brand_funnel['purchase'] / brand_funnel['view']

brand_funnel = brand_funnel.sort_values('overall_conversion', ascending=False)


first_event = df.groupby('user_id')['event_time'].min().reset_index()
first_event.columns = ['user_id','first_event_time']
df = df.merge(first_event, on='user_id')

df['user_type'] = df.apply(
    lambda row: 'new' if row['event_time'] == row['first_event_time'] else 'returning',
    axis=1
)


user_funnel = df.groupby('user_type')[['view','cart','purchase']].sum().reset_index()
user_funnel['view_to_cart'] = user_funnel['cart'] / user_funnel['view']
user_funnel['cart_to_purchase'] = user_funnel['purchase'] / user_funnel['cart']
user_funnel['overall_conversion'] = user_funnel['purchase'] / user_funnel['view']


fig_1 = px.bar(
    category_funnel.head(10),
    x='category_code',
    y='overall_conversion',
    title='Top Categories by Conversion Rate'
)


fig_2 = px.bar(
    brand_funnel.head(10),
    x='brand',
    y='overall_conversion',
    title='Top Brands by Conversion Rate'
)

if not os.path.exists("output\\images"):
   os.mkdir("output\\images")
   
fig_1.write_image("output\\images/category_funnel_summary.png")
fig_2.write_image("output\\images/brand_funnel_summary.png")