import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x_axis} and {y_axis}")
df = pd.read_csv("happy.csv")

match x_axis:
    case "GDP":
        x = df['gdp']
    case "Happiness":
        x = df['happiness']
    case "Generosity":
        x = df['generosity']
match y_axis:
    case "Happiness":
        y = df['happiness']
    case "GDP":
        y = df["gdp"]
    case "Generosity":
        y = df['generosity']

figure = px.scatter(
    x=x, y=y,
    labels={
        "x": x_axis,
        "y": y_axis
    }
)




st.plotly_chart(figure)
