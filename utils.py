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
	x = x % WORLD_SIZE
	y = y % WORLD_SIZE
	cur_x = get_pos_x()
	cur_y = get_pos_y()
	
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
				

def sort_on_field(l, direction, ord):
	for i in range(l):
		did_swap = False
		for _ in range(l - i):
			cur_val = measure()
			next_val = measure(direction)
			if ord(cur_val, next_val) > 0:
				did_swap = swap(direction)	
			move(direction)
		if not did_swap:
			break
		for _ in range(l - i):
			move(REVERSED_DIRECTION[direction])

def go_to_unplanted_corner():
	pos = where_is_in_unplanted_rectangle()
	rs_h_dir, rs_v_dir = CORNER_DIRECTION[pos]
	h_dir, v_dir = REVERSED_DIRECTION[rs_h_dir], REVERSED_DIRECTION[rs_v_dir]
	while pos <= CORNER_DOWN_MID and get_entity_type() == None:
		move(h_dir)
	if get_entity_type() != None:
		move(rs_h_dir)
	while pos in [CORNER_MID_MID, CORNER_MID_LEFT, CORNER_MID_RIGHT] and get_entity_type() == None:
		move(v_dir)
	if get_entity_type() != None:
		move(rs_v_dir)	
	return rs_h_dir, rs_v_dir


def where_is_in_unplanted_rectangle():
	if get_entity_type() != None:
		return None
	north_type, east_type, west_type, south_type = check_and_back(North), check_and_back(East), None, None # don't check too early if it is at CORNER_UP_RIGHT we can save some checks
	if north_type != None:
		if east_type != None:
			return CORNER_UP_RIGHT
		west_type = check_and_back(West) # if it is not CORNER_UP_RIGHT check left to know if it is CORNER_UP_LEFT
		if west_type != None:
			return CORNER_UP_LEFT
		return CORNER_UP_MID
		
	south_type = check_and_back(South)
	if south_type != None:
		if east_type != None:
			return CORNER_DOWN_RIGHT
		west_type = check_and_back(West)
		if west_type != None:
			return CORNER_DOWN_LEFT
		return CORNER_DOWN_MID
		
	if east_type != None:
		return CORNER_MID_RIGHT
	west_type = check_and_back(West)
	if west_type != None:
		return CORNER_MID_LEFT
	return CORNER_MID_MID
	
def check_and_back(dir):
	move(dir)
	entity_type = get_entity_type()
	move(REVERSED_DIRECTION[dir])
	return entity_type


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
			if break_condition != None and action_result == break_condition:
				return result
			result.append([cur_x, cur_y, action_result])
			if j < abs_height - 1:
				move(v_dir)
				cur_y += DIRECTION_VAL[v_dir]
		v_dir = REVERSED_DIRECTION[v_dir]
		if i < abs_width - 1:
			move(h_dir)
			cur_x += DIRECTION_VAL[h_dir]							
	return result

def wait_for(milisecond):
	start = get_time()
	while True:
		if get_time() - start >= milisecond/1000:
			return

def calculate_empty_square_size():
	h_dir, v_dir = go_to_unplanted_corner()
	size = 0
	while get_entity_type() == None:
		size += 1
		move(h_dir)
	move(REVERSED_DIRECTION[h_dir])
	return (size, REVERSED_DIRECTION[h_dir], v_dir)