from computing_utils import dfs, filter
from physical_utils import REVERSED_DIRECTION

def init_maze(size):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
def get_neighbours(root):
	candidates = [North, South, East, West]
	def filter_neighbour(candidate):
		return can_move(candidate) and (root == None or candidate != REVERSED_DIRECTION[root])
	candidates = filter(candidates, filter_neighbour)
	return candidates

def is_arrival(_):
	return get_entity_type() == Entities.Treasure

def trackback(root):
	move(REVERSED_DIRECTION[root])

def generate_random_comparator():
	mem = {}
	def random_comparator(a, b):
		aval, bval = random(), random()
		if a in mem:
			aval = mem[a]
		else:
			mem[a] = aval
		if b in mem:
			bval = mem[b]
		else:
			mem[b] = bval
		return aval - bval
	return random_comparator
	

def solve():
	dfs(None, get_neighbours, is_arrival, move, trackback, generate_random_comparator())
	harvest()
	
