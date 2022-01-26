import os
from subprocess import PIPE, run
import xml.etree.ElementTree as ET

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

fp='data/tif/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'
# fp='data/tif/LC08_L1TP_042034_20170616_20170629_01_T1_B4_EPSG4326.tif'
# fp = 'data/tif/Hansen_GFC-2020-v1.8_last_40N_080W.tif'

# lon,lat = (-119.770163586, 36.741997032)
lon,lat = (-73.770163586, 36.741997032)

# Generate the command
command = "gdallocationinfo -xml -wgs84 %s %s, %s" % (fp, lon, lat)
# print(command)
# Run the command. os.system() returns value zero if the command was executed succesfully
# my_output = os.system(command)
my_output = out(command)

print(my_output)

#parse xml string
root = ET.fromstring(my_output)
newsitems = []
  
# iterate news items
for item in root.findall('./'):
    # empty news dictionary
    news = {}
    if(item.tag == 'Alert'):
        news['col'] = root.attrib['pixel']
        news['row'] = root.attrib['line']
        news['error'] = item.text
    else:
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if item.tag == 'BandReport':
                news['col'] = root.attrib['pixel']
                news['row'] = root.attrib['line']
                news['band'] = item.attrib['band']
                news['value'] = float(child.text)
                
    # append news dictionary to news items list
    newsitems.append(news)

print(newsitems)