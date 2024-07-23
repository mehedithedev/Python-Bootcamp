import streamlit
import plotly.express as pe
from backend import fetch
import pandas as pd




streamlit.title("Weather forecast")
place = streamlit.text_input("City")
days = streamlit.slider("Number of days to see forecast: ",
                        min_value=1,
                        max_value=10,
                        help="Select between 1 to 10")
streamlit.subheader(f"Showing forecast of {place} for next {days} days ")

if place:

    final_data = fetch(place, days)
    weather_data_list  = []

    for data in final_data:
        weather_data = data['main']['temp']
        weather_data_celsius = weather_data / 10
        weather_date = data['dt_txt']
        print(weather_date, weather_data_celsius)
        condition = data['weather'][0]['main']
        print(condition)

        weather_data_list.append({
            'date': weather_date,
            'temerature': weather_data_celsius,
            'condition': condition
        })

        print(weather_data_list)


    data_frame = pd.DataFrame(weather_data_list)

    print(data_frame)

    # Draw the line graph using the dataframe

    graph = pe.line(data_frame,
                    x = 'date',
                    y = 'temerature',
                    labels={
                       'date' : 'Days',
                       'temerature': 'Temp(C)'
                    })
    streamlit.plotly_chart(graph)