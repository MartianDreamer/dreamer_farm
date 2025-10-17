from utils import calculate_empty_square_size, DIRECTION_VAL, REVERSED_DIRECTION, directed_move, move_to, detect_h_dir, detect_v_dir
from basic_algorithm import reverse_bifunction, desc, asc

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
	
			
	
			
	