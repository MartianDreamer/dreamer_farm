from utils import move_to, find_max_value
from farm_task import plant_area

clear()
plant_area(3, 6, Entities.Sunflower, Grounds.Soil)
move_to(0, 0)
x, y = find_max_value(3, 6, measure)
move_to(x, y)