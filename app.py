import pandas as pd
import scipy.stats
import streamlit as st
import time
import plotly.express as px
import numpy as np
import plotly.figure_factory as ff



st.header(":blue[US Vehecle Data Base Analysis and Visualization]")
       

st.write("*reading the csv into pandas df and viewing sample of the df.*")
st.write(df_vehicles = pd.read_csv('../vehicles_us.csv'))
st.write (df_vehicles.sample(3))


st.write (
   "*Exploring the df_vehicles.*"
df_vehicles.info()

 "*the price is in normal format and no missing value. Model_year, cylinders, omometer, is_4wkd have some missing values; and type float will be converted to integer since the zeros have no relevance. No missing value in model, condition, transmission, type; and their format type object is good. date_posted will be converted to datetime format.*"

df_vehicles['is_4wd'].unique()


"*The nan value in column is_4wd will be converted to 0 (assuming that it is bool where 1 is yes and 0 is not 4wd).*"


df_vehicles['is_4wd'] = df_vehicles['is_4wd'].fillna(0)
df_vehicles.paint_color = df_vehicles.paint_color.fillna('unknown')
df_vehicles = df_vehicles.dropna()


"*Converting the columns data type from float to int*"
df_vehicles[['model_year', 'cylinders', 'odometer', 'is_4wd']] = df_vehicles[['model_year', 'cylinders', 'odometer', 'is_4wd']].astype(int)

"*extracting manufacturer from the model name*"

df_vehicles['manufacturer'] = df_vehicles['model'].apply(lambda x: x.split()[0])

)


st.header("Disribution of the Day Listed")
fig_1 = px.histogram(df_vehicles, x="days_listed")
fig_1.show()
st.write(fig_1)


st.header("Disribution of the Vehecle Price")
fig_2 = px.histogram(df_vehicles, x="price")
fig_2.show()
st.write (fig_2)

st.header("Scatter plot Showing Correlation between Odometer and the Price")
fig_3 = px.scatter(df_vehicles, x=df_vehicles['odometer'], y=df_vehicles["price"])
fig_3.show()
st.write (fig_3)

st.header("Scatter plot Showing Correlation between days_listr and the Price")
fig_4 = px.scatter(df_vehicles, x=df_vehicles['days_listed'], y=df_vehicles["price"])
fig_4.show()
st.write (fig_4)



agree = st.checkbox("Acceped")

if agree:
    st.write("Great, moving on o next step!")
