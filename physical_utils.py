REVERSED_DIRECTION = {North: South, South: North, East: West, West: East}
DIRECTION_VAL = {North: 1, South: -1, East: 1, West: -1}
# REVERSED_ORD = {asc_ord: desc_ord, desc_ord: asc_ord}
WORLD_SIZE = get_world_size()
CORNER_DIRECTION = [(East, North), (East, South), (East, North), (East, North), (West, North), (East, South), (West, South), (East, North), (West, North)]

CORNER_MID_MID = 0
CORNER_UP_MID = 1
CORNER_DOWN_MID = 2
CORNER_MID_LEFT = 3
CORNER_MID_RIGHT = 4
CORNER_UP_LEFT = 5
CORNER_UP_RIGHT = 6
CORNER_DOWN_LEFT = 7
CORNER_DOWN_RIGHT = 8

def directed_move(step, dir):
	for _ in range(step):
		move(dir)

def move_to(x, y):
	cur_x = get_pos_x()
	cur_y = get_pos_y()
	if cur_x == x and cur_y == y:
		return
	x = x % WORLD_SIZE
	y = y % WORLD_SIZE
	
	x_underflow_dist = x - cur_x
	x_overflow_dist = WORLD_SIZE - max(cur_x, x) + min(cur_x, x)
	x_dist = 0
	h_direction = East
	
	y_underflow_dist = y - cur_y
	y_overflow_dist = WORLD_SIZE - max(cur_y, y) + min(cur_y, y)
	y_dist = 0
	v_direction = North
	
	# find shortest way and direction
	if abs(x_underflow_dist) < x_overflow_dist:
		h_direction = detect_h_dir(x_underflow_dist)
		x_dist = abs(x_underflow_dist)
	else:
		h_direction = REVERSED_DIRECTION[detect_h_dir(x_underflow_dist)]
		x_dist = x_overflow_dist
	
	if abs(y_underflow_dist) < y_overflow_dist:
		v_direction = detect_v_dir(y_underflow_dist)
		y_dist = abs(y_underflow_dist)
	else:
		v_direction = REVERSED_DIRECTION[detect_v_dir(y_underflow_dist)]
		y_dist = y_overflow_dist
	
	for _ in range(x_dist):
		move(h_direction)
	for _ in range(y_dist):
		move(v_direction)

def in_map_move_to(x, y):
	cur_x, cur_y = get_pos_x(), get_pos_y()
	dist_x, dist_y = x - cur_x, y - cur_y
	h_dir, v_dir = detect_h_dir(dist_x), detect_v_dir(dist_y)
	for _ in range(abs(dist_x)):
		move(h_dir)
	for _ in range(abs(dist_y)):
		move(v_dir)
				

def detect_h_dir(dist):
	if dist < 0:
		return West
	return East

def detect_v_dir(dist):
	if dist < 0:
		return South
	return North

def do_action_on_every_cell(width, height, action, break_condition = None):
	h_dir, v_dir = detect_h_dir(width), detect_v_dir(height)
	cur_x, cur_y = get_pos_x(), get_pos_y()
	abs_width = abs(width)
	abs_height = abs(height)
	result = []
	for i in range(abs_width):
		for j in range(abs_height):
			action_result = action()
			result.append([cur_x, cur_y, action_result])
			if break_condition != None and action_result == break_condition:
				return result
			if j < abs_height - 1:
				move(v_dir)
				cur_y += DIRECTION_VAL[v_dir]
		v_dir = REVERSED_DIRECTION[v_dir]
		if i < abs_width - 1:
			move(h_dir)
			cur_x += DIRECTION_VAL[h_dir]							
	return result

def block_for(milisecond):
	if milisecond == 0:
		return
	start = get_time()
	while True:
		if get_time() - start >= milisecond/1000:
			return
	
def do_n_times(n, cooldown, action):
	for i in range(n):
		action()
		if i < n - 1:
			block_for(cooldown)
			
def do_action_on_list_of_cell(list_of_cells, action, break_condition = None):
	rs = []
	for cell in list_of_cells:
		x, y = cell[0], cell[1]
		move_to(x, y)
		action_rs = action()
		rs.append([x, y, action_rs])
		if break_condition != None and action_rs == break_condition:
			return rs
	return rs
