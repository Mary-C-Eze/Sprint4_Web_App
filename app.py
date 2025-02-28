import pandas as pd
import streamlit as st
import plotly.express as px



st.header(":blue[US Vehecle Database Analysis and Visualization]")
       

"reading the csv into pandas df and viewing sample of the df."
df_vehicles = pd.read_csv('vehicles_us.csv')

df_vehicles ["is_4wd"] = df_vehicles['is_4wd'].fillna(0)
df_vehicles.paint_color = df_vehicles.paint_color.fillna('unknown')
df_vehicles = df_vehicles.dropna()

df_vehicles[['model_year', 'cylinders', 'odometer', 'is_4wd']] = df_vehicles[['model_year', 'cylinders', 'odometer', 'is_4wd']].astype(int)

df_vehicles['manufacturer'] = df_vehicles['model'].apply(lambda x: x.split()[0])

options = st.multiselect(
    "What are your choice of manufacturers",
    df_vehicles.manufacturer.unique().tolist(),
    df_vehicles.manufacturer.unique().tolist()

)

st.write("You selected:", options)

df_vehicles = df_vehicles.loc[df_vehicles.manufacturer.isin(options)]

max_price_selected = st.slider("Range of Price",
                        min_value=df_vehicles.price.min(),
                        max_value = df_vehicles.price.max(),
                        value=df_vehicles.price.max())
st.write("Maximum Price Selected", max_price_selected)

df_vehicles = df_vehicles.loc[df_vehicles.price <= max_price_selected]


st.header("Distribution of the Day Listed")
fig_1 = px.histogram(df_vehicles, x="days_listed", labels={"x": "days_listed", "y": "frequency"}, 
                     color="manufacturer")
st.plotly_chart(fig_1)


st.header("Distribution of the Vehecle Price")
fig_2 = px.histogram(df_vehicles, x="price", labels={'x':'Price','y':'Frequency'}, color="manufacturer")
st.plotly_chart (fig_2)

st.header("Scatter plot Showing Correlation between Odometer and the Price")
fig_3 = px.scatter(df_vehicles, x=df_vehicles['odometer'], 
                   y=df_vehicles["price"], color="manufacturer", trendline="ols")
st.plotly_chart (fig_3)

st.header("Scatter plot Showing Correlation between days_listr and the Price")
fig_4 = px.scatter(df_vehicles, x=df_vehicles['days_listed'], 
                   y=df_vehicles["price"], color="manufacturer", trendline="ols" )
st.plotly_chart (fig_4)


agree = st.checkbox("Acceped")

if agree:
    st.write("Great, moving on o next step!")
