import streamlit as st
# function used to plot graphs
import plotly.express as px
import functions as f

# Building webpage
st.title("Weather Canvas")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view:", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Plotting data
d, t = f.get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature in C"})
st.plotly_chart(figure)
