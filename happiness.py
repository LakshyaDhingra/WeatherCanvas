import streamlit as st
import plotly.express as px
import pandas as pd

# Webpage design
st.title("Happiness Quotient")
x = st.selectbox("Select data for X-axis", ("GDP", "Happiness", "Generosity"))
y = st.selectbox("Select data for Y-axis", ("GDP", "Happiness", "Generosity"))
st.subheader(f"{x} and {y}")

# csv file read
df = pd.read_csv("happy.csv")

# match cases to display data for each column from csv
match x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]
match y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

# scatter plot used
figure = px.scatter(x=x_array, y=y_array, labels={"x": x, "y": y})

st.plotly_chart(figure)
