# World Map Creator

This is a simple Python script to generate a world map with a list of countries painted.

It save the map as SVG and also shows it.

It uses these libraries:
- geopandas
- matplotlib
- pycountry_convert
- shapely

For it to work you need to download a shapefile from geoBoundaries:

It can be downloaded from https://www.geoboundaries.org/globalDownloads.html

The file have ADM Level "ADM0 (Countries)" and should be of the type "Shapefile".

There is also a Jupyter Lab (https://jupyter.org/) file with the code, step by step, that I used to refine the code.

As an example I got the list of countries with organizations linked with the World Organization of the Scout Movement (http://scout.org).
