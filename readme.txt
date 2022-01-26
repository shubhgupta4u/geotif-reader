Installing with Anaconda
C:\Users\shubh\.conda\envs\gisenv

(base) PS E:\Python\raster-tif-reader> conda create --name gisenv python=3.8
(base) PS E:\Python\raster-tif-reader> conda activate gisenv
(gisenv) PS E:\Python\raster-tif-reader> conda config --add channels conda-forge
(gisenv) PS E:\Python\raster-tif-reader> conda config --set channel_priority strict
(gisenv) PS E:\Python\raster-tif-reader> conda install rasterio
(gisenv) PS E:\Python\raster-tif-reader> conda install matplotlib
(gisenv) PS E:\Python\raster-tif-reader> conda install pyproj

Navigate to
https://download.gisinternals.com/query.html?content=filelist&file=release-1916-x64-gdal-3-4-1-mapserver-7-6-4.zip

Download and install:
gdal-304-1916-x64-core.msi
GDAL-3.4.1.win-amd64-py3.8.msi
Set Environments:

setx /m path "%path%;C:\Program Files\GDAL;
:: Create new variables in the system environment for GDAL.
setx /m GDAL_DATA "C:\Program Files\GDAL\gdal-data"
setx /m GDAL_DRIVER_PATH "C:\Program Files\GDAL\gdalplugins"
setx PROJ_LIB "C:\Program Files\GDAL\projlib"
setx /m GDAL_VERSION "3.1.1"

conda install gdal

Test gdal installation:
gdallocationinfo -xml -wgs84 "E:\Python\raster-tif-reader\data\tif\LC08_L1TP_042034_20170616_20170629_01_T1_B4.tif" -119.770163586, 36.741997032
