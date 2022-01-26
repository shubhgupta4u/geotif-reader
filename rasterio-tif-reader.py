import rasterio
import matplotlib.pyplot as plt
import numpy as np
from rasterio.plot import show
import os
import pyproj
from pyproj import Transformer,CRS
from osgeo import osr

# Specify the path for Landsat TIF on AWS
# fp = os.path.join(data_dir, "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")
# fp = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'
# fp='data/tif/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'
fp='data/tif/LC08_L1TP_042034_20170616_20170629_01_T1_B4_EPSG4326.tif'
# fp = 'data/tif/Hansen_GFC-2020-v1.8_last_40N_080W.tif'

# See the profile
with rasterio.open(fp) as src:
    proj = osr.SpatialReference(wkt=src.crs.to_wkt())
    print("epsg:" +proj.GetAttrValue('AUTHORITY',1))
    epsgValue = "epsg:" +proj.GetAttrValue('AUTHORITY',1)
    # print(src.crs.to_dict())
    # print(src.width, src.height)
    # print(src.profile)
    # print(src.transform)
    # print(src.count)
    # print(src.indexes)
    # window = src.window(*src.bounds)
    # print(window)
    # print(src.read(window=window).shape)
    # print(src.bounds)
    # print(src.driver)
    # print(src.meta)
    # print(src.nodatavals)

    
    # # Read all bands
    array = src.read()
    bandCount,rowCount,ColCount = array.shape
    print(array.shape)

    # Use pyproj to convert point coordinates
    utm = CRS(src.crs)
    if epsgValue == 'epsg:4326':
        lonlat = utm
    else:
        lonlat = CRS.from_string('GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]')
    
    transformer = Transformer.from_crs(lonlat,utm)

    lon,lat = (-119.770163586, 36.741997032)
    # lon,lat = (-73.770163586, 36.741997032)    
    east,north = transformer.transform(lon, lat)

    print('Fresno NDVI\n-------')
    print(f'lon,lat=\t\t({lon:.2f},{lat:.2f})')
    print(f'easting,northing=\t({east:g},{north:g})')

    # What is the corresponding row and column in our image?
    row, col = src.index(east, north) # spatial --> image coordinates #
    print(f'row,col=\t\t({row},{col})') #(6582,1873)

    # What is the band?
    band = src.read(1)
    if (row >= 0 and row < rowCount) and (col>=0 and col < ColCount):
        value = band[row, col] #12956.00
        print(f'value at lat/lng=\t\t\t{value:.2f}')


    
    # Calculate statistics for each band
    # stats = []
    # for band in array:
    #     stats.append({
    #         'min': band.min(),
    #         'mean': band.mean(),
    #         'median': np.median(band),
    #         'max': band.max()})

    # # Show stats for each channel
    # print(stats)
    
    # Plot band 1
    # show((src, 1))



    