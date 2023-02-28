from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

# The json.load() function converts the data into a format Python
# a giant dictionary
eq_data = json.load(infile)

# The json.dump() function takes a JSON data object and a file object file
# The indent=4 argument tells dump() to format the data using the data's structure.

# readable file is just to visualize the data
json.dump(eq_data, outfile, indent=5)

list_of_eqs = eq_data['features']  # Takes us to features section
print(len(list_of_eqs))

mags, lats, lons = [], [], []

for eq in list_of_eqs:  # at this point eq is a string that represents each dictionary
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)
print(mags[:10])
print(lats[:10])
print(lons[:10])


# Worldmap layout to put lats and lons on
data = Scattergeo(lon=lons, lat=lats)
# Feeding the list, creating a title (plotly, not necessarily Python)
my_layout = Layout(title="Global Earthquakes")

fig = {'data': data, 'layout': my_layout}  # show dictionary and layout

offline.plot(fig, filename='global_earthquakes.html')
