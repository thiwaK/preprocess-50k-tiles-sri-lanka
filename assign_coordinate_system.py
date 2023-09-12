import arcpy
import os

'''
  Require ArcGIS Pro - arcpy (python 3)
'''

#setup pathc
targetFC = r"E:\Spatial_Data\LK\50K\ALL_50K_Sheets\SHP\01\building\dxf.shp"
base = r"E:\Spatial_Data\LK\50K\ALL_50K_Sheets\SHP"


# get SR for targetFC
targetDescribe = arcpy.Describe(targetFC)
targetSR = targetDescribe.spatialReference
targetSRName = targetSR.Name


def get_all_shp_files(directory):
  """Gets all .shp files in the specified directory and its subdirectories.
  
  Args:
    directory: The path to the directory.

  Returns:
    A list of all .shp files in the directory and its subdirectories.
  """

  shp_files = []
  for root, directories, files in os.walk(directory):
    for file in files:
      if file.endswith(".shp"):
        shp_files.append(os.path.join(root, file))

  return shp_files

for shp in get_all_shp_files(base):
	print(shp)
	arcpy.DefineProjection_management(shp, targetSR)