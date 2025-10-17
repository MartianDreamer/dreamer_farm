from utils import move_to, WORLD_SIZE, do_action_on_every_cell, wait_for, do_n_times
from pumpkin import harvest_and_replant_pumpkin
from cactus import plant_cactus
from sunflower import plant_sunflower
from farm_task import do_soil, harvest_and_replant, watering, plant_area

GRASS_HARVEST_THRESHOLD = 10000


clear()

# set up pattern
# plan trees
move_to(6,3)
plant_area(6, 3, Entities.Tree, Grounds.Grassland)
# plant carrots
move_to(6, 6)
plant_area(4, 6, Entities.Carrot, Grounds.Soil)
def harvest_carrot():
	move_to(6, 6)
	do_action_on_every_cell(4, 6, harvest_and_replant)
	
# plant sunflowers
move_to(6, 0)
harvest_sunflower = plant_sunflower(6, 3)
# plant pumpkins
move_to(0, 0)
plant_area(6, 6, Entities.Pumpkin, Grounds.Soil)
# plant cactuses
move_to(0, 6)
harverst_cactus = plant_cactus(6, 6)
# harvest hay
def harvest_hay():
	move_to(10, 6)
	do_action_on_every_cell(2, 6, harvest)


while True:
	attempt = 0
	do_n_times(5, 250, harvest_carrot)
	do_n_times(15, 0, harvest_hay)
	
	# harvest pumpkin
	move_to(5, 5)
	do_action_on_every_cell(-6, -6, harvest_and_replant_pumpkin)
	
	while not harverst_cactus() and attempt < 3:
		wait_for(100)
		attempt += 3
	attempt = 0 
	
	do_n_times(2, 200, harvest_sunflower)
	
	# harvest tree
	move_to(6, 3)
	do_action_on_every_cell(6, 3, harvest_and_replant)