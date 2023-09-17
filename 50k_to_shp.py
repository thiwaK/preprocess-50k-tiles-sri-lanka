import os
from subprocess import Popen, PIPE
import shutil

'''
  Require GDAL and ogr2ogr.py
'''

break_ = 0

base = r"D:\New folder (2)\50,000 shapefiles Digital"
out = r"D:\New folder (2)\250data"

if not os.path.isdir(out):
		os.mkdir(out)

log = open(r"D:\New folder (2)\250data\log.txt", "w")

# Iterae over tiles (1 to 92)
for tile in [x for x in os.walk(base)][0][1]:

	print("Tile", tile)

	# Iterae over feature classess (admin, water, building, road, ...)
	for feature in [x for x in os.walk(os.path.join(base, tile))][0][1]:
		
		# Skip unnecessary folders/files
		if feature in ['info']:
			continue

		# print("    ", feature,  end=' ')

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
			log.write(f"{tile}/{feature}")
			print(featureclass)
			shutil.rmtree(os.path.join(out, tile, feature))
			break_ = 1
			log.flush()
			os.fsync(log.fileno())


	print()
log.close()