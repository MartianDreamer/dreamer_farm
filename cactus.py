from physical_utils import DIRECTION_VAL, REVERSED_DIRECTION, move_to, detect_h_dir, detect_v_dir, do_action_on_every_cell
from computing_utils import reverse_bifunction, desc, asc
from farm_utils import plant_area

def bubble_sort(size, dir, comparator):
	for i in range(size):
		did_swap = False
		for j in range(size - i - 1):
			cur_val = measure()
			next_val = measure(dir)
			if comparator(cur_val, next_val) > 0:
				swap(dir)
				did_swap = True
			if j < size - i - 2:
				move(dir)
		if not did_swap:
			break
		dir = REVERSED_DIRECTION[dir]
		comparator = reverse_bifunction(comparator)

def bubble_sort_cactus(width, height):
	start_x, start_y = get_pos_x(), get_pos_y()
	h_size = abs(width)
	v_size = abs(height)
	
	v_dir = detect_v_dir(height)
	
	# sort rows
	h_dir = detect_h_dir(width)
	comparator = asc
	if h_dir == West:
		comparator = desc
	for i in range(v_size):
		bubble_sort(h_size, h_dir, comparator)
		if i < v_size - 1:
			start_y += DIRECTION_VAL[v_dir]
			move_to(start_x, start_y)

	move_to(start_x, start_y)
	# sort columns
	v_dir = REVERSED_DIRECTION[v_dir]
	comparator = asc
	if v_dir == South:
		comparator = desc
	for i in range(h_size):
		bubble_sort(v_size, v_dir, comparator)
		if i < h_size - 1:
			start_x += DIRECTION_VAL[h_dir]
			move_to(start_x, start_y)
	
def plant_cactus(width, height, water_threshold = 0.75):
	start_x, start_y = get_pos_x(), get_pos_y()
	sorted_cactus = False
	def replant():
		move_to(start_x, start_y)
		plant_area(width, height, Entities.Cactus, Grounds.Soil, water_threshold)
	replant()
	def harvest_and_replant_cactus():
		move_to(start_x, start_y)
		if not sorted_cactus:
            bubble_sort_cactus(width, height)
            sorted_cactus = True
		move_to(start_x, start_y)
		harvestables = do_action_on_every_cell(width, height, can_harvest, False)
		if len(harvestables) != width * height:
			return False
		harvest()
		replant()
        sorted_cactus = False
		return True
	return harvest_and_replant_cactus