from wood import plant_wood_y
from all_loop import loop
from wattering import water_it
from mega_p import plant_mega_pumpkin

L = [Entities.Grass, Entities.Carrot]
clear()
import till_all
change_hat(Hats.Wizard_Hat)




hay = 10000
wood = 10000
carrot = 10000
def super_plant():
	if num_items(Items.Hay) < hay:
		plant(Entities.Grass)
	elif num_items(Items.Wood) < wood:
		plant_wood_y()
	elif num_items(Items.Carrot) < carrot:
		plant(Entities.Carrot)
	else:
		goto(0,0)
		plant_mega_pumpkin()
	
	
		

def main():
	if can_harvest():
		harvest()
		super_plant()
	else:
		if not get_entity_type() or get_entity_type() == Entities.Dead_Pumpkin:
			super_plant()
	water_it()
		
	


while True:
	loop(main)
	
	
	