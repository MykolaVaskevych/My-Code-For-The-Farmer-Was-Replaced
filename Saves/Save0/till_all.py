clear()
for x in range(get_world_size()):
	for y in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		move(North)
	move(East)