from computing_utils import dfs, filter
from physical_utils import REVERSED_DIRECTION

def init_maze(size):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
def get_neighbours(root):
	candidates = [North, South, East, West]
	if root in candidates:
		candidates.remove(REVERSED_DIRECTION[root])
	candidates = filter(candidates, can_move)
	return candidates

def is_arrival(_):
	return get_entity_type() == Entities.Treasure
	
def solve():
	dfs(None, get_neighbours, is_arrival, move, trackback)
	harvest()

def trackback(root):
	move(REVERSED_DIRECTION[root])

