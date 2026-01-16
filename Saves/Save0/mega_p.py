from all_loop import loop
from movement import goto
def pumpkin_harvest():
	goto(0,0)
	a = measure()
	b = get_world_size() - 1
	goto(b,b)
	if a == measure() and can_harvest():
		harvest()
		return True
	else:
		return False
	
def plant_mega_pumpkin():
	plant(Entities.Pumpkin)
	if ( get_pos_y() == get_world_size() - 1 and get_pos_x() == get_world_size() - 1):
		pumpkin_harvest()
