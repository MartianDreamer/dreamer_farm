from utils import calculate_empty_square_size, move_to, DIRECTION_VAL, do_action_on_every_cell
from farm_task import plant_area, watering
from basic_algorithm import reduce, map


def harvest_and_replant_pumpkin(water_threshold = 0.75):
	if get_entity_type() == Entities.Pumpkin and can_harvest():
		x, y = get_pos_x(), get_pos_y()
		harvest()
		size, h_dir, v_dir = calculate_empty_square_size()
		directed_h, directed_v = DIRECTION_VAL[h_dir], DIRECTION_VAL[v_dir]
		plant_area(size * directed_h, size * directed_v, Entities.Pumpkin, Grounds.Soil)
		move_to(x, y)
	elif get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		watering(water_threshold)

def plant_pumpkin(width, height):
	start_x, start_y = get_pos_x(), get_pos_y()
	plant_area(width, height, Entities.Pumpkin, Grounds.Soil)
	def try_harvest():
		move_to(start_x, start_y)
		cell_count = do_action_on_every_cell(width, height, replant_dead_pumpkin)
		did_replant = reduce(map(cell_count, get_3rd_element), no_replant, False)
		if not did_replant:
			harvest()
			move_to(start_x, start_y)
			plant_area(width, height, Entities.Pumpkin, Grounds.Soil)
			return True
		return False
	return try_harvest
		

def replant_dead_pumpkin():
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		return True
	return False

def no_replant(a, b):
	return a or b

def get_3rd_element(a):
	return a[2]