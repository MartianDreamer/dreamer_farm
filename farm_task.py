from utils import detect_h_dir, detect_v_dir, REVERSED_DIRECTION, do_action_on_every_cell

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
	def action():
		return plant_watering_measure(tree_type, soil_type, water_threshold)
	return do_action_on_every_cell(width, height, action)

def plant_watering_measure(tree_type, soil_type, water_threshold = 75):
	do_soil(soil_type)
	if tree_type != None:
		plant(tree_type)
		watering(water_threshold)
		return measure()
	return -1
			
		