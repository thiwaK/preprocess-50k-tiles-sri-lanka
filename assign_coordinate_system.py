import arcpy
import os

'''
	Require ArcGIS Pro - arcpy (python 3)
'''

class progress():
		def __init__(self, current, maximum):
				self.current = current
				self.maximum = maximum
				self.BAR_WIDTH = 15
				self.FILE_NAME_LEN = 30
				
				self.current -=1
				self.next("")
				
				
		def next(self, file_name):
				self.current += 1
				x = int((self.BAR_WIDTH + self.FILE_NAME_LEN)*self.current/self.maximum)
				y = round(self.current/self.maximum*100, 1)
				z = file_name[(self.FILE_NAME_LEN*-1):]
				text_pb = "{}[{}{}] {}/{} {}%".format("Processing", "#"*x, "."*(self.BAR_WIDTH+self.FILE_NAME_LEN-x), self.current, self.maximum, y)
				print(text_pb, end='\r', file=sys.stdout, flush=True)



#setup pathc
targetFC = r"E:\Spatial_Data\LK\50K\ALL_50K_Sheets\SHP\01\building\dxf.shp"
base = r"D:\New folder (2)\250data"


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

all_shp = get_all_shp_files(base)
p = progress(0, len(all_shp))
count = 0
for shp in all_shp:
	arcpy.DefineProjection_management(shp, targetSR)
	count += 1
	p.next(shp)