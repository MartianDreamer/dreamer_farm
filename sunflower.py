from physical_utils import detect_h_dir, detect_v_dir, DIRECTION_VAL, do_action_on_every_cell, move_to, block_for
from computing_utils import sort
from farm_utils import plant_area, plant_watering_measure, harvest_and_replant

def sort_by_2nd_element(a, b):
	return b[2] - a[2]

def plant_sunflower(width, height, water_threshold = 0.75):
	plant_map = plant_area(width, height, Entities.Sunflower, Grounds.Soil, water_threshold)
	sort(plant_map, sort_by_2nd_element)

	def harvest_and_replant_sunflower():
		count = 0
		n = len(plant_map)
		for x, y, _ in plant_map:
			if n - count < 10:
				break
			else:
				move_to(x, y)
				if not can_harvest():
					block_for(200)
				harvest()
				count += 1
		for i in range(count):
			x, y, _ = plant_map[i]
			move_to(x, y)
			plant_map[i][2] = plant_watering_measure(Entities.Sunflower, Grounds.Soil, water_threshold)
		sort(plant_map, sort_by_2nd_element)

	return harvest_and_replant_sunflower

