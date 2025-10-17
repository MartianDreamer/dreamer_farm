from utils import do_action_on_every_cell
from basic_algorithm import init_2_dimensional_array

def plant_tree(width, height):
	start_x, start_y = get_pos_x(), get_pos_y()
	h_size, v_size = abs(width), abs(height)
	plantable_map = init_2_dimensional_array(h_size, v_size, True)
	def check_and_plant():
		cur_x, cur_y = get_pos_x() - start_x, get_pos_y() - start_y
		left = cur_x - 1
		right = cur_x + 1
		up = cur_y + 1
		down = cur_y - 1
		if (left < 0 or plantable_map[cur_y][left]) and (right >= h_size or plantable_map[cur_y][right]) and (down < 0 or plantable_map[down][cur_x]) and (up >= v_size or plantable_map[up][cur_x]):
			plant(Entities.Tree)
			plantable_map[cur_y][cur_x] = False
			return True
		return False
	do_action_on_every_cell(width, height, check_and_plant)
