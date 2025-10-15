from utils import move_to, WORLD_SIZE
from pumpkin import harvest_and_replant_pumpkin
from farm_task import do_soil, harvest_and_replant, watering, plant_area

GRASS_HARVEST_THRESHOLD = 10000


clear()

# set up pattern
plant_area(12, 6, North, East, Entities.Pumpkin, Grounds.Soil)
move(East)
plant_area(12, 3, North, East, Entities.Carrot,  Grounds.Soil)
move(East)
plant_area(12, 2, North, East, Entities.Tree,  Grounds.Grassland)

while True:
	if get_entity_type() == Entities.Pumpkin or get_entity_type() == Entities.Dead_Pumpkin:
		harvest_and_replant_pumpkin()
	else:
		harvest_and_replant()
	if random() < 0.3:
		move(North)
	else:
		move(East)
	watering(0.75)
	