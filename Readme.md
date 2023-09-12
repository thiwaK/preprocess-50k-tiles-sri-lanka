# Automated script to pre-process LK 50K sheets

## Execution order
1. 50k_to_shp
2. assign_coordinate_system
3. merge_50k_tiles_by_feature

## Explanation

Metric map sheets of Sri Lanka, reliese from department of survey, need to do some pre-processes before they utilize for something. One is they are not shape files. They are in adf format, which is some old type of vector data representation. So the 1st script convert all those files into shape files, according to the data layer and vector type. Data layer can be building, grid, water, roads, etc, while vector type can be point, line, polygon. Then, the second script assign Kandawala Sri Lanka coordinate system to each feature class seperately. Then the third script merge all avilable layers of 92 tiles by vector type.  Becuase if we merge by only data layer, we will end up loosing some details. At the end, you will have nice data layers covering all the land area of Sri Lanka that can be use for your analysis directly.

Note: If you planed to do this process manually, you will require 1 or 2 days. But these script will do all those time consiuming works for you by within 10 minutes or less, according to your computer preformences.