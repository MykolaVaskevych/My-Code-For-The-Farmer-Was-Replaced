def plant_wood_y():
	y = get_pos_y()
	if y % 2 == 0 :
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
		
		