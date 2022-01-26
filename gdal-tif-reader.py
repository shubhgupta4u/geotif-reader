# script to get pixel values at a set of coordinate

# by reading in one pixel at a time
# Took 0.47 seconds on my machine
import os, sys, time 
from osgeo import gdal,osr
import pyproj
from pyproj import Transformer,CRS
# from gdalconst import *

# start timing
startTime = time.time()
# coordinates to get pixel values for
xValues = [-119.770163586]
yValues = [36.741997032]
# xValues = [-73.770163586]
# yValues = [36.741997032]
# set directory
os.chdir(r'E:\Python\raster-tif-reader\data\tif')
# register all of the drivers
gdal.AllRegister()

# open the image
# ds = gdal.Open('LC08_L1TP_042034_20170616_20170629_01_T1_B4.tif', GA_ReadOnly)
# ds = gdal.Open('LC08_L1TP_042034_20170616_20170629_01_T1_B4.tif')
# ds = gdal.Open('Hansen_GFC-2020-v1.8_last_40N_080W.tif')

ds = gdal.Open('LC08_L1TP_042034_20170616_20170629_01_T1_B4_EPSG4326.tif')
if ds is None:
    print('Could not open image')
    sys.exit(1)

proj = osr.SpatialReference(wkt=ds.GetProjection())
print("epsg:" +proj.GetAttrValue('AUTHORITY',1))
epsgValue = "epsg:" +proj.GetAttrValue('AUTHORITY',1)
# print(pyproj.datadir.get_data_dir())

# get image size
rows = ds.RasterYSize
cols = ds.RasterXSize
bands = ds.RasterCount
print(rows,cols,bands) #7951 7821 1
# get georeference info
transform = ds.GetGeoTransform()
xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = transform[5]
print(xOrigin,yOrigin,pixelWidth,pixelHeight)

# Use pyproj to convert point coordinates
utm = CRS(ds.GetProjection())
if epsgValue == 'epsg:4326':
    lonlat = utm
else:
    lonlat = CRS.from_string('GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]')
transformer = Transformer.from_crs(lonlat,utm)

# loop through the coordinates
for i in range(1):
    # get x,y
    x,y = transformer.transform(xValues[i], yValues[i])
    
    # compute pixel offset
    xOffset = int((x - xOrigin) / pixelWidth)
    yOffset = int((y - yOrigin) / pixelHeight)
    print(xOffset,yOffset)
    # create a string to print out
    s = str(x) + ' ' + str(y) + ' ' + str(xOffset) + ' ' + str(yOffset) + ' '
    if (xOffset >= 0 and xOffset < rows) and (yOffset>=0 and yOffset < cols):
        # loop through the bands
        for j in range(bands):
            band = ds.GetRasterBand(j+1) # 1-based index
            # read data and add the value to the string
            data = band.ReadAsArray(xOffset, yOffset, 1, 1)
            value = data[0,0]
            s = s + str(value) + ' '
        # print out the data string
    print(s)

# figure out how long the script took to run
endTime = time.time()
print('The script took ' + str(endTime - startTime) + ' seconds')