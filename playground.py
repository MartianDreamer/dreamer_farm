from farm_task import plant_area
from cactus import bubble_sort_cactus
from basic_algorithm import desc
from utils import move_to

clear()
move_to(0, 0)
plant_area(8, 8, Entities.Cactus, Grounds.Soil)
bubble_sort_cactus(-8, 8)
if can_harvest():
	harvest()
