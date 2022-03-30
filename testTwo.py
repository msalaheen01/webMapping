import pandas
import folium

parks_data = pandas.read_csv("parks.csv")
parks_lat = parks_data["latitude"]
parks_lon = parks_data["longitude"]
park_name = parks_data["details"]

bridges_data = pandas.read_csv("bridges.txt")
bridges_lat = bridges_data["Latitude"]
bridges_lon = bridges_data["Longitude"]
bridges_name = bridges_data["Place Name"]

lakes_data = pandas.read_csv("lakes.txt")
lakes_lat = lakes_data["Latitude"]
lakes_lon = lakes_data["Longitude"]
lakes_name = lakes_data["Place Name"]



# creates an html link tag to google
html = """
<h4><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a></h4>
"""

lg = folium.FeatureGroup(name="U.S Lakes")

for lt,ln,name in zip(lakes_lat,lakes_lon,lakes_name):
    iframe = folium.IFrame(html = html % (name,name), width=80, height=80)
    lg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon= folium.Icon(color="blue")))



bg = folium.FeatureGroup(name="Popular U.S Bridges")

for lt,ln,name in zip(bridges_lat,bridges_lon,bridges_name):
    iframe = folium.IFrame(html=html % (name,name), width=80, height=80)
    bg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon= folium.Icon(color="red")))



# initializes a map with given coordinates, zoom and map background type
mapOne = folium.Map(location=[37.0902, -95.7129],  # center of USA
                    zoom_start=3, tiles="cartodb positron")

# creates a container for the markers
fg = folium.FeatureGroup(name="U.S Parks")

# iterates over latitude,longitude and park names to create a marker each
# creates an iframe
# adds these markers to the feature group above
for lt,ln,name in zip(parks_lat, parks_lon, park_name):
    iframe = folium.IFrame(html=html % (name,name), width=100, height=100)
    fg.add_child(folium.Marker(location=[lt,ln], popup= folium.Popup(iframe), icon= folium.Icon(color="darkpurple")))


# adds the feature group of markers to the map
mapOne.add_child(lg)
mapOne.add_child(bg)
mapOne.add_child(fg)
mapOne.add_child(folium.LayerControl())

# creates an html file with the above attributes
mapOne.save("U.S Parks, Bridges and Lakes.html")




