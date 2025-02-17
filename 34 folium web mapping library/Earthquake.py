import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium


st.title("Earthquake Global Map")
df = pd.read_csv('earthquakes_yesterday.csv')
mean_lat = df['Latitude'].mean()
mean_lon = df['Longitude'].mean()

m = folium.Map(location=[mean_lat,mean_lon],zoom_start=2)
for i ,row in df.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    (folium.CircleMarker(location=[lat,lon],radius=row['Magnitude']*2,
                         color = 'crimson',
                         fill = True,
                         fill_coor = 'crimson',
                         tootltip = f"Loc {row['Location']}")
     .add_to(m))


m.save('map.html')


