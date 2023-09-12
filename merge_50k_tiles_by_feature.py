import os
import geopandas as gpd

base = r"E:\Spatial_Data\LK\50K\ALL_50K_Sheets\SHP"


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

def merge_shp(shp_collection, feature, subfeatures):

	print("  Splitting collection to sub-features")
	splited_collection = {item:[] for item in subfeatures}

	for subfeature in subfeatures:
		for shp in shp_collection:
			if subfeature in str(os.path.splitext(os.path.split(shp)[1])[0]):
				splited_collection[subfeature].append(shp)

	total_items = 0
	for key, value in splited_collection.items():
		print("   ", key, "has", len(value), "items")
		total_items += len(value)
	print("   ", total_items, "total items")

	print("  Merging splitted collections seperately")
	for sub_f in splited_collection.keys():
		f_count = len(splited_collection[sub_f])
		print(f"    {feature} > {sub_f}")

		# temp_ = [x[-30:]for x in splited_collection[sub_f]]
		# for temp__ in temp_:
		# 	print("..." + temp__)

		out_shp = os.path.join(base, feature + "_" + sub_f + '.shp')

		shapefiles = [gpd.read_file(path) for path in splited_collection[sub_f]]
		merged_shapefile = gpd.pd.concat(shapefiles)
		merged_shapefile.to_file(out_shp)

def filter_tiles(feature, tiles):

	filtered_tiles = []

	for tile in tiles:
		if os.path.isdir(os.path.join(base, tile, feature)):
			filtered_tiles.append(os.path.join(base, tile, feature))
	print(" ", len(filtered_tiles),"tiles out of", len(tiles), "qualified")
	return filtered_tiles

def get_subclasses_of_feature(tiles_filtered):

	subfeatures = []
	files = []

	for tile in tiles_filtered:
		shp = get_all_shp_files(tile)
		files += shp

	print(" ", len(files), "shapefiles avilable for merging")
	for file in files:
		feature_name = str(os.path.splitext(os.path.split(file)[1])[0])
		if feature_name not in subfeatures:
			subfeatures.append(feature_name)
	print(" ", len(subfeatures), "sub-features found", subfeatures)
	return subfeatures, files

print("Initiating...")
# collect avilable tiles (1 to 92)
tiles = [x for x in os.walk(base)][0][1]

# collect avilable features
feature_list = []
for tile in tiles:
	for feature in [x for x in os.walk(os.path.join(base, tile))][0][1]:
		if feature in feature_list:
			continue
		else:
			feature_list.append(feature)
print(len(feature_list), "features found.", feature_list)

for feature in feature_list:
	print("Start merging...", feature)
	if feature in ["info"]:
		continue

	tiles_filtered = filter_tiles(feature, tiles)
	subfeatures, mergable_shp = get_subclasses_of_feature(tiles_filtered)
	merge_shp(mergable_shp, feature, subfeatures)

