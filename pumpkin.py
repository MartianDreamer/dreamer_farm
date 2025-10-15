from utils import REVERSED_DIRECTION, plant_area, watering, go_to_unplanted_corner

def calculate_pumpkin_size():
	h_dir, v_dir = go_to_unplanted_corner()
	size = 0
	while get_entity_type() == None:
		size += 1
		move(h_dir)
	move(REVERSED_DIRECTION[h_dir])
	return (size, REVERSED_DIRECTION[h_dir], v_dir)

def harvest_and_replant_pumpkin(water_threshold = 0.75):
	if get_entity_type() == Entities.Pumpkin and can_harvest():
		harvest()
		size, h_dir, v_dir = calculate_pumpkin_size() 
		plant_area(size, size, h_dir, v_dir, Entities.Pumpkin, Grounds.Soil)
	elif get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		watering(water_threshold)

def get_h_dir_from_value(val):
	if val < 0:
		return East	
	else:
		return West	
	
	