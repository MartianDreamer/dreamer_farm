from utils import calculate_empty_square_size, move_to, DIRECTION_VAL
from farm_task import plant_area, watering


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



	
	