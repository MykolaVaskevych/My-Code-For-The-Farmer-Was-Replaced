import till_all
from all_loop import loop

def pumpkin_harvest():

	if can_harvest():
		if measure() == something:
			harvest()
			return True
	return False
	
def plant_mega_pumpkin():
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
	elif not get_entity_type():
		plant(Entities.Pumpkin)
	else:
		pumpkin_harvest()

while not pumpkin_harvest():
	loop(plant_mega_pumpkin)