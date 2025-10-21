from bush import harvest_and_replant_bush, plant_bush
from sunflower import plant_sunflower
from physical_utils import do_action_on_every_cell, move_to

clear()
do_action_on_every_cell(4, 22, plant_bush)
move_to(4, 0)
harvest_sunflower = plant_sunflower(4,22)
while True:
	move_to(0, 0)
	do_action_on_every_cell(4, 22, harvest_and_replant_bush)
	harvest_sunflower()
