import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # Converts data into a format Python can work with: in this case, a giant dictionary.

# Make file readable
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
# json.dump(all_eq_data, f, indent=4) # indent=4 tells dump() to format the data using indentation that matches the data's structure

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts)) # Verifies that we are dealing with 158 Earthquakes

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]  # Longitude comes first in this data set
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    # Text gives us a value whenever you hover over a data point
    'text': hover_texts,
    # We use marker to specify size of marker and attached is dictionary because we can specify lots of detaisl
    # We multiply each mag by 5 so it's more visible. This list will give size for each marker individually
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
    },
    # ^ Add a color scale for magnitude
    # Color tells Plotly what values it should use to determine where each marker falls on the color scale
    # Colorscale tells which range of colors to use: 'Viridis' ranges from dark blue to bright yellow
    # We set reversescale to true because we want lowest values yellow
    # Colorbar settings allows us to control appearance of colorscale on side of map and we title it 'Magnitude'
}]
# Using new way to specify data since it's easier for customization.  Below is the old way:
# [Scattergeo(lon=lons, lat=lats)] # List because you can plot more than one data set on any visualization you make
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes30.html')
