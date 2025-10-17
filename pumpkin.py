from utils import move_to, DIRECTION_VAL, do_action_on_every_cell, wait_for
from farm_task import plant_area, watering
from basic_algorithm import reduce, map


def plant_pumpkin(width, height, wait_time = 100):
	start_x, start_y = get_pos_x(), get_pos_y()
	plant_area(width, height, Entities.Pumpkin, Grounds.Soil)
	def try_harvest():
		move_to(start_x, start_y)
		cell_count = do_action_on_every_cell(width, height, replant_dead_pumpkin)
		did_replant = reduce(map(cell_count, get_3rd_element), no_replant, False)
		if not did_replant:
			wait_for(wait_time)
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