ws = get_world_size()

x = get_pos_x()
y = get_pos_y()

def harvest_now():
	if can_harvest():
		harvest()

def soil_prep():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if get_water() < 0.3:
		use_item(Items.Water)

def move_to(target_x, target_y):    
	while get_pos_x() != target_x:
		x = get_pos_x()
		# distance going east vs west
		east_dist = (target_x - x) % ws
		west_dist = (x - target_x) % ws
		if east_dist <= west_dist:
			move(East)
		else:
			move(West)

	while get_pos_y() != target_y:
		y = get_pos_y()
		# distance going north vs south
		north_dist = (target_y - y) % ws
		south_dist = (y - target_y) % ws
		if north_dist <= south_dist:
			move(North)
		else:
			move(South)

			
item_caps = {
	Items.Hay : 1000000,
	Items.Wood : 1000000,
	Items.Carrot : 1000000,
	Items.Pumpkin : 26000000,    
	Items.Bone : 100000000,
	Items.Cactus : 20000000,
	Items.Power : 100000,
	Items.Weird_Substance : 50000,
	Items.Gold : 10000000,
	Items.Fertilizer : 50000,
	}