import geopandas as gpd
import matplotlib.pyplot as plt
import pycountry_convert as pc
from shapely.geometry import box

file = open('wosm-countries-202408.txt', 'r', encoding='utf-8')
temp = file.read()
countries_names = temp.split("\n")
file.close()
# Convert country names to Alpha-3 codes
country_codes_alpha3 = [pc.country_name_to_country_alpha3(country) for country in countries_names]

# Load the world map
# Can be downloaded from https://www.geoboundaries.org/globalDownloads.html
# ADM Level: ADM0 (Countries) / Shapefile
world = gpd.read_file("geoBoundariesCGAZ_ADM0.shp")

# Filter only the countries in the list
selected_countries = world[world['shapeGroup'].isin(country_codes_alpha3)]

# Create a polygon that covers the entire map area
bounds = world.total_bounds
background = gpd.GeoDataFrame(geometry=[box(bounds[0], bounds[1], bounds[2], bounds[3])], crs=world.crs)

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10), facecolor='darkblue')

# Plot the dark blue background
background.plot(ax=ax, color='darkblue')

world.plot(ax=ax, color='lightgrey', edgecolor='white', linewidth=0.5)
selected_countries.plot(ax=ax, color='#602497', edgecolor='white', linewidth=0.5)

# Remove the ticks and labels on the map borders
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.savefig('wosm_countries_map.svg', format='svg')

plt.show()
