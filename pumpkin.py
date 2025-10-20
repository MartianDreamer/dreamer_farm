from physical_utils import move_to, wait_for, do_action_on_list_of_cell
from farm_utils import plant_area
from computing_utils import filter


def plant_pumpkin(width, height, wait_time = 200):
	start_x, start_y = get_pos_x(), get_pos_y()
	planted_cells = plant_area(width, height, Entities.Pumpkin, Grounds.Soil)
	def try_harvest():
		global planted_cells
		dead_pumpkins = do_action_on_list_of_cell(planted_cells, replant_dead_pumpkin)
		planted_cells = filter(dead_pumpkins, did_replant)
		total_wait_time = len(dead_pumpkins) * wait_time
		if total_wait_time < 500:
			total_wait_time = 500
		if len(planted_cells) == 0 or len(planted_cells) == width * height:
			wait_for(total_wait_time)
			move_to(start_x, start_y)
			harvest()
			planted_cells = plant_area(width, height, Entities.Pumpkin, Grounds.Soil)
			return True
		return False
	return try_harvest

def replant_dead_pumpkin():
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		return True
	return False

def did_replant(cell):
	return cell[2]
