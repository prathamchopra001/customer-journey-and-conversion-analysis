import pandas as pd
import plotly.express as px
import os


df = pd.read_csv("data\\clean_data.csv")


df["view"] = (df["event_type"] == "view").astype(int)
df['cart'] = (df['event_type'] == 'cart').astype(int)
df['purchase'] = (df['event_type'] == 'purchase').astype(int)

funnel = df.groupby("user_id")[['view', 'cart', 'purchase']].max().reset_index()


view_users = funnel['view'].sum()
cart_users = funnel['cart'].sum()
purchase_users = funnel['purchase'].sum()
print("Users who viewed:", view_users)
print("Users who added to cart:", cart_users)
print("Users who purchased:", purchase_users)

cart_conversion = cart_users / view_users * 100
purchase_conversion = purchase_users / cart_users * 100
overall_conversion = purchase_users / view_users * 100
print("View → Cart Conversion:", round(cart_conversion,2), "%")
print("Cart → Purchase Conversion:", round(purchase_conversion,2), "%")
print("Overall Conversion:", round(overall_conversion,2), "%")

funnel_summary = pd.DataFrame({
    "stage": [ "view", "cart", "purchase" ],
    "users": [ view_users, cart_users, purchase_users ]
})


fig = px.funnel(
    funnel_summary,
    x='users',
    y='stage',
    color='stage',
    hover_data=['users'],
)


if not os.path.exists("output\\images"):
   os.mkdir("output\\images")
   
fig.write_image("output\\images/funnel_summary.png")

view_to_cart_dropoff = (1 - cart_users / view_users) * 100
cart_to_purchase_dropoff = (1 - purchase_users / cart_users) * 100
print(f"insight: {round(cart_conversion,2)}% of users who viewed the product added it to their cart, and {round(purchase_conversion,2)}% of those who added to cart completed the purchase. The overall conversion rate from view to purchase is {round(overall_conversion,2)}%.")
print((f"A {round(view_to_cart_dropoff,2)}% drop-off from view to cart indicates potential issues with product appeal or pricing, while a {round(cart_to_purchase_dropoff,2)}% drop-off from cart to purchase suggests possible friction in the checkout process."))
