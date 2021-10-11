from typing import List
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
# import numpy as np
# import pandas as pd
import requests as rq

from streamlit_folium import folium_static
import folium

from heartquake import Heartquake

DATA_URL: str = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

response = rq.get(DATA_URL)
data = response.json()

st.title("titolo")

heartquakes: List[Heartquake] = []
for feature in data["features"]:
    heartquakes.append(Heartquake.from_feature(feature))

st.write(heartquakes)

m = folium.Map(location=[39.949610, -75.150282], zoom_start=3)

# add marker for heartwuakes

for heartquake in heartquakes:
    tooltip = heartquake.place
    # folium.Marker(
    #     [heartquake.lat, heartquake.lon], popup=heartquake.place, tooltip=tooltip
    # ).add_to(m)
    folium.CircleMarker(
        location=[heartquake.lat, heartquake.lon],
        radius=3 * heartquake.magnitude,
        popup=f"{heartquake.place} ({heartquake.magnitude})",
        color="#3186cc",
        fill=True,
        fill_color="#3186cc",
    ).add_to(m)

# call to render Folium map in Streamlit
folium_static(m)