import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # Converts data into a format Python can work with: in this case, a giant dictionary.

# Make file readable
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
# json.dump(all_eq_data, f, indent=4) # indent=4 tells dump() to format the data using indentation that matches the data's structure

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts)) # Verifies that we are dealing with 158 Earthquakes

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]  # Longitude comes first in this data set
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
	# We use marker to specify size of marker and attached is dictionary because we can specify lots of detaisl
	# We multiply each mag by 5 so it's more visible otherwise they're too small to see.  This list will give size for each marker individually
    'marker': {
        'size': [5 * mag for mag in mags],
    }
}]
# Using new way to specify data since it's easier for customization.  Below is the old way:
# [Scattergeo(lon=lons, lat=lats)] # List because you can plot more than one data set on any visualization you make
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
