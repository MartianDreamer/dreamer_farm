from utils import calculate_empty_square_size
from farm_task import plant_area, watering


def harvest_and_replant_pumpkin(water_threshold = 0.75):
	if get_entity_type() == Entities.Pumpkin and can_harvest():
		harvest()
		size, h_dir, v_dir = calculate_empty_square_size() 
		plant_area(size, size, h_dir, v_dir, Entities.Pumpkin, Grounds.Soil)
	elif get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		watering(water_threshold)



	
	