import geopandas as gpd
import matplotlib.pyplot as plt
import pycountry_convert as pc
from shapely.geometry import box
import json

cfg_file = open('worldmapcreator-config.json', 'r', encoding="utf-8")
config = json.load(cfg_file)
cfg_file.close()

countries_file = open(config['selected_countries'], 'r', encoding='utf-8')
temp = countries_file.read()
countries_names = temp.split("\n")
countries_file.close()
# Convert country names to Alpha-3 codes
country_codes_alpha3 = [pc.country_name_to_country_alpha3(country) for country in countries_names]

# Load the world map
# Can be downloaded from https://www.geoboundaries.org/globalDownloads.html
# ADM Level: ADM0 (Countries) / Shapefile
world = gpd.read_file(config['shapefile'])

# Filter only the countries in the list
selected_countries = world[world['shapeGroup'].isin(country_codes_alpha3)]

# Create a polygon that covers the entire map area
bounds = world.total_bounds
background = gpd.GeoDataFrame(geometry=[box(bounds[0], bounds[1], bounds[2], bounds[3])], crs=world.crs)

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10), facecolor=config['background_color'])

# Plot the dark blue background
background.plot(ax=ax, color=config['background_color'])

world.plot(ax=ax, color=config['unselected_color'], edgecolor=config['edge_color'], linewidth=0.5)
selected_countries.plot(ax=ax, color=config['selected_color'], edgecolor=config['edge_color'], linewidth=0.5)

# Remove the ticks and labels on the map borders
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.savefig(config['output_svg_file'], format='svg')

plt.show()
