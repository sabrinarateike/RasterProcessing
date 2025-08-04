from osgeo import gdal
from osgeo import ogr

##Open up the input raster

##Select the first band of the raster

##Print the metadata of the raster

##Print the minimum value of the raster

##Print the maximum value of the raster

##Print the no data value of the raster

##Convert the raster to an array

##Print the minimum of the array

##Update the data values of the array that
##are < than 0 to 0

##Print the updated minimum of the array.

##Write the updated raster from the array to a new .tif file

##Create a polygon version of the input raster with a DN field
##to hold the raster value


print(band.GetNoDataValue())

drv = ogr.GetDriverByName('ESRI Shapefile')
outfile = drv.CreateDataSource('polygonRast.shp') 
outlayer = outfile.CreateLayer('polygonized raster', srs = None )

newField = ogr.FieldDefn('DN', ogr.OFTReal)
outlayer.CreateField(newField)
gdal.Polygonize(band, None, outlayer, 0, [])
outfile = None

raster = gdal.Open(r'E:\GIS_2075\W9\GIS_DATA\wcbio_10m.tif')

band = raster.GetRasterBand(1)

for i in range(1, raster.RasterCount + 1):
    b = raster.GetRasterBand(i)
    print(b.GetMetadata())

data [ data < 0 ] = 0

print(band.GetMinimum())

print(data.min())

print(data.min())

drv = gdal.GetDriverByName('GTiff') 
outRaster = drv.CreateCopy('newRaster.tif', raster , 0 )

newBand = outRaster.GetRasterBand(1)                               
newBand.WriteArray(data)
outRaster = None

print(band.GetMaximum())

data = band.ReadAsArray()

print(band.GetScale())
