from utils import move_to, WORLD_SIZE, do_action_on_every_cell, wait_for, do_n_times
from pumpkin import plant_pumpkin
from cactus import plant_cactus
from sunflower import plant_sunflower
from farm_task import do_soil, harvest_and_replant, watering, plant_area
from tree import plant_tree

GRASS_HARVEST_THRESHOLD = 10000


clear()

# set up pattern
# plan trees
move_to(6, 3)
plant_tree(6, 5)

def harvest_tree():
	move_to(6, 3)
	do_action_on_every_cell(6, 5, harvest_and_replant)
	
# plant carrots
move_to(6, 8)
plant_area(6, 4, Entities.Carrot, Grounds.Soil)
def harvest_carrot():
	move_to(6, 8)
	do_action_on_every_cell(6, 4, harvest_and_replant)
	
# plant sunflowers
move_to(6, 0)
harvest_sunflower = plant_sunflower(6, 3)
# plant pumpkins
move_to(0, 0)
harvest_pumpkin = plant_pumpkin(6, 6)
# plant cactuses
move_to(0, 6)
harverst_cactus = plant_cactus(6, 6)
# harvest hay
def harvest_hay():
	move_to(10, 6)
	do_action_on_every_cell(2, 6, harvest)


while True:
	attempt = 0
	do_n_times(4, 200, harvest_carrot)
	do_n_times(4, 300, harvest_tree)
	
	# harvest pumpkin
	while not harvest_pumpkin() and attempt < 3:
		attempt += 1
	attempt = 0
	
	while not harverst_cactus() and attempt < 3:
		wait_for(100)
		attempt += 1
	attempt = 0 
	
	do_n_times(2, 200, harvest_sunflower)
