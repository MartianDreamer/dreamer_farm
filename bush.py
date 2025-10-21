from farm_utils import watering

def harvest_and_replant_bush(water_threshold = 1):
	if can_harvest():
		harvest()
		plant_bush(water_threshold)
		return True
	return False
	
def plant_bush(water_threshold = 1):
	plant(Entities.Bush)
	use_item(Items.Fertilizer)
	watering(water_threshold)
	return True
	