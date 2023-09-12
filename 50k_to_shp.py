import os
from subprocess import Popen, PIPE
import shutil

'''
  Require GDAL and ogr2ogr.py
'''

break_ = 0

base = r"E:\Spatial_Data\LK\50K\ALL_50K_Sheets\Digital_Data_For_Self_Study\Other_Digital_Data"
out = r"E:\Spatial_Data\LK\50K\ALL_50K_Sheets\250data"

# Iterae over tiles (1 to 92)
for tile in [x for x in os.walk(base)][0][1]:
	print("Tile", tile)

	# Iterae over feature classess (admin, water, building, road, ...)
	for feature in [x for x in os.walk(os.path.join(base, tile))][0][1]:
		
		if feature in ['info']:
			continue

		print("    ", feature,  end=' ')

		featureclass = os.path.join(base, tile, feature)

		tmp_path = os.path.join(out, tile)
		if not os.path.isdir(tmp_path):
			os.mkdir(tmp_path)

		tmp_path = os.path.join(tmp_path, feature)
		if not os.path.isdir(tmp_path):
			os.mkdir(tmp_path)

		p = Popen(['python', 'ogr2ogr.py', '-f', "ESRI Shapefile", '-overwrite', tmp_path, featureclass])
		output = p.communicate()
		rc = p.returncode

		if rc != 0:
			print(featureclass)
			break_ = 1
	if break_:
		shutil.rmtree(os.path.join(out, tile))
		break_ = 0

	print()
