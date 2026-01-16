def shortest_dir(old, new, size, forward, backward):
	if (new - old) % size <= (old - new) % size: # no ternar ;(
		return forward
	else:
		return backward


def goto(new_x, new_y):
	size = get_world_size()

	while get_pos_x() != new_x or get_pos_y() != new_y:
		x = get_pos_x()
		y = get_pos_y()

		if x != new_x:
			move(shortest_dir(x, new_x, size, East, West))
		elif y != new_y:
			move(shortest_dir(y, new_y, size, North, South))


			