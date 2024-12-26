import streamlit as st
# function used to plot graphs
import plotly.express as px
from backend import get_data

# Building webpage
st.title("WeatherCanvas")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view:", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    try:
        # Get filtered temp/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            celsius_temperatures = [i/10 for i in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Plotting graph data
            figure = px.line(x=dates, y=celsius_temperatures, labels={"x": "Date", "y": "Temperature in C"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            print_images = [images[condition] for condition in sky_conditions]
            st.image(print_images, width=115)
    except:
        st.error("Invalid place entered, Try again")
