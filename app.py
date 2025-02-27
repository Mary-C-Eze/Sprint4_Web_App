import pandas as pd
import scipy.stats
import streamlit as st
import time
import plotly.express as px
import numpy as np
import plotly.figure_factory as ff



st.header(":blue[US Vehecle Database Analysis and Visualization]")
       

st.write("*reading the csv into pandas df and viewing sample of the df.*")
df_vehicles = pd.read_csv('vehicles_us.csv')

df_vehicles ["is_4wd"] = df_vehicles['is_4wd'].fillna(0)
df_vehicles.paint_color = df_vehicles.paint_color.fillna('unknown')
df_vehicles = df_vehicles.dropna()

df_vehicles[['model_year', 'cylinders', 'odometer', 'is_4wd']] = df_vehicles[['model_year', 'cylinders', 'odometer', 'is_4wd']].astype(int)

df_vehicles['manufacturer'] = df_vehicles['model'].apply(lambda x: x.split()[0])


st.header("Disribution of the Day Listed")
fig_1 = px.histogram(df_vehicles, x="days_listed")
st.plotly_chart(fig_1)


st.header("Disribution of the Vehecle Price")
fig_2 = px.histogram(df_vehicles, x="price")
st.plotly_chart (fig_2)

st.header("Scatter plot Showing Correlation between Odometer and the Price")
fig_3 = px.scatter(df_vehicles, x=df_vehicles['odometer'], y=df_vehicles["price"])
st.plotly_chart (fig_3)

st.header("Scatter plot Showing Correlation between days_listr and the Price")
fig_4 = px.scatter(df_vehicles, x=df_vehicles['days_listed'], y=df_vehicles["price"])
st.plotly_chart (fig_4)



agree = st.checkbox("Acceped")

if agree:
    st.write("Great, moving on o next step!")
