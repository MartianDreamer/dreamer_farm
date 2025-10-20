from physical_utils import move_to, WORLD_SIZE, do_action_on_every_cell, wait_for, do_n_times
from pumpkin import plant_pumpkin
from cactus import plant_cactus
from sunflower import plant_sunflower
from farm_utils import do_soil, harvest_and_replant, watering, plant_area
from tree import plant_tree

GRASS_HARVEST_THRESHOLD = 10000


clear()
# set up pattern
# plan trees
move_to(6, 3)
plant_tree(6, 3)
move_to(0, 12)
plant_tree(16, 4)


def harvest_tree1():
	move_to(6, 3)
	do_action_on_every_cell(6, 3, harvest_and_replant)



def harvest_tree2():
	move_to(0, 12)
	do_action_on_every_cell(16, 4, harvest_and_replant)
	
# plant carrots
move_to(12, 0)
plant_area(4, 8, Entities.Carrot, Grounds.Soil)
def harvest_carrot():
	move_to(12, 0)
	do_action_on_every_cell(4, 12, harvest_and_replant)
	
# plant sunflowers
move_to(6, 0)
harvest_sunflower = plant_sunflower(6, 3)
# plant pumpkins
move_to(0, 0)
harvest_pumpkin1 = plant_pumpkin(6, 6)
move_to(6, 6)
harvest_pumpkin2 = plant_pumpkin(6, 6)
# plant cactuses
move_to(0, 6)
harverst_cactus = plant_cactus(6, 6)


while True:
	attempt = 0
	harvest_carrot()
	harvest_tree1()
	harvest_tree2()
	
	# harvest pumpkin
	while not harvest_pumpkin1() and attempt < 3:
		attempt += 1
	attempt = 0
	
	# harvest pumpkin
	while not harvest_pumpkin2() and attempt < 3:
		attempt += 1
	attempt = 0
	
	
	while not harverst_cactus() and attempt < 3:
		wait_for(100)
		attempt += 1
	attempt = 0 
	
	do_n_times(2, 200, harvest_sunflower)
	