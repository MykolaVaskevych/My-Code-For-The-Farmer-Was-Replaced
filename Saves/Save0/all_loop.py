def loop(do_this):
	size = get_world_size()
	
	for x in range(size):
		for y in range(size):
			do_this()
			move(North)
		move(East)