clear()
while True:
	if can_harvest():
		harvest()
	else:
		move(East)
	move(North)