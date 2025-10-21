def sort(arr, comparator):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, comparator, n, i)
	
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, comparator, i, 0)


def heapify(arr, comparator, n, i):
	largest = i
	left = largest * 2 + 1
	right = largest * 2 + 2

	if left < n and comparator(arr[left], arr[largest]) > 0:
		largest = left
	
	if right < n and comparator(arr[right], arr[largest]) > 0:
		largest = right
	
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, comparator, n, largest)

def asc(a, b):
	return a - b
def desc(a, b):
	return b - a

CALL_BACK_MEM = {}

def reverse_bifunction(callback):
	if callback in CALL_BACK_MEM:
		return CALL_BACK_MEM[callback]
	def reverse_callback(a, b):
		return 0 - callback(a, b)
	CALL_BACK_MEM[callback] = reverse_callback
	CALL_BACK_MEM[reverse_callback] = callback
	return reverse_callback

def init_2_dimensional_array(x, y, init_value = 0):
	arr = []
	for _ in range(y):
		element = []
		for _ in range(x):
			element.append(init_value)
		arr.append(element)
	return arr

def reduce(arr, bifunction, initial_value = None):
	if len(arr) == 0:
		return None
	elif len(arr) == 1:
		if initial_value != None:
			return bifunction(initial_value, arr[0])
		else:
			return arr[0]
	elif initial_value != None:
		rs = initial_value
		for e in arr:
			rs = bifunction(rs, e)
		return rs
	else:
		rs = None
		for e in arr:
			if rs == None:
				rs = e
			else:
				rs = bifunction(rs, e)
		return rs

def map(arr, mapper):
	rs = []
	for e in arr:
		rs.append(mapper(e))
	return rs
	
def filter(arr, predicate):
	rs = []
	for e in arr:
		if predicate(e):
			rs.append(e)
	return rs

def dfs(root, get_neighbours, is_arrival, move_to_neighbour = None, trackback = None):
	# callback is meant to return to the previous node
	if is_arrival(root):
		return [root]
	neighbours = get_neighbours(root)
	quick_print(neighbours)
	for neighbour in neighbours:
		if move_to_neighbour != None:
			move_to_neighbour(neighbour)
		path = dfs(neighbour, get_neighbours, is_arrival, move_to_neighbour, trackback)
		if len(path) != 0:
			path.insert(0, root)
			return path
	if trackback != None:
		trackback(root)
	return []
