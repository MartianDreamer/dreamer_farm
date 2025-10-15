from utils import detect_h_dir, detect_v_dir, REVERSED_DIRECTION

def harvest_and_replant(water_threshold = 0.75):
	tree_type = get_entity_type()
	if can_harvest():
		harvest()
		plant(tree_type)
		watering(water_threshold)
		return True
	return False

def do_soil(soil_type):
	if get_ground_type() != soil_type:
		till()
		
def watering(threshold):
	if get_water() <= threshold:
		use_item(Items.Water)

def plant_area(width, height, tree_type, soil_type, water_threshold = 0.75):
	cur_h_dir, v_direction = detect_h_dir(width), detect_v_dir(height)
	for i in range(height):
		for j in range(width):
			do_soil(soil_type)
			if tree_type != None:
				plant(tree_type)
			watering(water_threshold)
			if j < width - 1:
				move(cur_h_dir)
		cur_h_dir = REVERSED_DIRECTION[cur_h_dir]
		if i < height - 1:
			move(v_direction)
		
		