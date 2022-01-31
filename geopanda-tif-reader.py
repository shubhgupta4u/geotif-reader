
# import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
from rasterio.plot import show
from shapely.geometry import Point


# print(gdf.head())
import rasterio
src = rasterio.open('tif_files\whp2020_cnt_conus.tif')


fig, ax = plt.subplots()

# transform rasterio plot to real world coords
extent=[src.bounds[0], src.bounds[2], src.bounds[1], src.bounds[3]]
ax = rasterio.plot.show(src, extent=extent, ax=ax, cmap='pink')

import geopandas as gpd

# # Create sampling points
# points = [Point(625466, 5621289), Point(626082, 5621627), Point(627116, 5621680), Point(625095, 5622358)]
# gdf = gpd.GeoDataFrame([1, 2, 3, 4], geometry=points, crs=32630)
points=[Point(-955275,1475959),Point(-999904,1475729)]
gdf = gpd.GeoDataFrame([1, 2], geometry=points, crs=5070)
gdf.plot(ax=ax)


coord_list = [(x,y) for x,y in zip(gdf['geometry'].x , gdf['geometry'].y)]

gdf['value'] = [x for x in src.sample(coord_list)]
print(gdf.head())