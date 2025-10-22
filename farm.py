from helpers import move_to, soil_prep, harvest_now, ws, x, y, item_caps

def hay():
	for i in range(ws):
		harvest_now()
		if get_ground_type() == Grounds.Soil:
				till()
		harvest_now()
		move(North)
	move(East)

def bushes():
	for i in range(ws):
		soil_prep()
		plant(Entities.Bush)
		move(North)
	move(East)

def carrots():
	for i in range(ws):
		soil_prep()
		plant(Entities.Carrot)
		move(North)
	move(East)

def trees():	
	for x in range(ws):
		for y in range(ws):
			harvest_now()
			if (x + y) % 2 == 0:
				soil_prep()
				plant(Entities.Tree)
				move(North)
			else:
				plant(Entities.Bush)
				move(North)
		move(East)

def pumpkins():
	set_world_size(12)
	ws = get_world_size()    
	ready = []
	for _ in range(ws):
		col = []
		for _ in range(ws):
			col.append(False)
		ready.append(col)

	cur_x = get_pos_x()
	if cur_x != 0:
		left  = cur_x
		right = ws - cur_x
		if left <= right:
			for _ in range(left):
				move(West)
		else:
			for _ in range(right):
				move(East)

	cur_y = get_pos_y()
	if cur_y != 0:
		down = cur_y
		up   = ws - cur_y
		if down <= up:
			for _ in range(down):
				move(South)
		else:
			for _ in range(up):
				move(North)

	going_east = True

	while True:
		all_ready = True

		for row in range(ws):
			for step in range(ws):
				tile_ready = ready[x][y]

				if tile_ready:
					if get_entity_type() != Entities.Pumpkin or can_harvest() != True:
						tile_ready      = False
						ready[x][y]     = False

				if tile_ready != True:
					if get_ground_type() == Grounds.Grassland:
						till()

					if get_entity_type() != Entities.Pumpkin:
						plant(Entities.Pumpkin)
					if get_water() < 0.2:
						use_item(Items.Water)

					if can_harvest():
						tile_ready      = True
						ready[x][y]     = True

				if tile_ready != True:
					all_ready = False

				if step < ws - 1:
					if going_east:
						move(East)
					else:
						move(West)

			if row < ws - 1:
				move(North)
			going_east = not going_east

		if all_ready:
			harvest()
			for ix in range(ws):
				for iy in range(ws):
					ready[ix][iy] = False

		move(North)
		if get_pos_x() != 0:
			move(East)

def sunflower():
	set_world_size(12)
	ws = get_world_size()
	x, y = get_pos_x(), get_pos_y()    
	cur = {0:0, 1:0}

	def move_to(x, y):
		global cur
		dx, dy = x - cur[0], y - cur[1]
		cur = {0:x,1:y}
		while dx > 0:
			dx = dx - 1
			move(East)
		while dx < 0:
			dx = dx + 1
			move(West)
		while dy > 0:
			dy = dy - 1
			move(North)
		while dy < 0:
			dy = dy + 1
			move(South)

	order = {}
	while True:
		x, y = get_pos_x(), get_pos_y()
		if x == 0 and y == 0:
			for i in range(15, 6, -1):
				if i in order:
					for pos in order[i]:
						move_to(pos[0], pos[1])
						while not can_harvest():
							use_item(Items.Fertilizer)
						harvest()
			order = {}
			move_to(0,0)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		if get_water() < 0.3:
			use_item(Items.Water)
		if num_items(Items.Fertilizer) > item_caps[Items.Fertilizer]:
			use_item(Items.Fertilizer)
		if measure() not in order:
			order[measure()] = [{0:x,1:y}]
		else:
			order[measure()].append({0:x,1:y})
		if y == ws - 1:
			move(East)
		move(North)
		
		
def poly():    
	soil_prep()
	plant(Entities.Carrot)

	companion = get_companion()

	while companion != None:
		_, (x, y) = companion
		move_to(x, y)
		soil_prep()
		plant(companion[0])
		companion = get_companion()

def cactus():
	set_world_size(22)
	ws = get_world_size()

	for y in range(ws):
		for x in range(ws):
			move_to(x, y)
			harvest_now()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)

	cactus_sizes = []
	for y in range(ws):
		row = []
		for x in range(ws):
			row.append(0)
		cactus_sizes.append(row)

	for y in range(ws):
		for x in range(ws):
			move_to(x, y)
			cactus_sizes[y][x] = measure()

	changed = True
	while changed:
		changed = False
		for y in range(ws):
			for x in range(ws):
				move_to(x, y)
				if x < ws - 1 and cactus_sizes[y][x] > cactus_sizes[y][x + 1]:
					swap(East)
					cactus_sizes[y][x], cactus_sizes[y][x + 1] = cactus_sizes[y][x + 1], cactus_sizes[y][x]
					changed = True
				if y < ws - 1 and cactus_sizes[y][x] > cactus_sizes[y + 1][x]:
					swap(North)
					cactus_sizes[y][x], cactus_sizes[y + 1][x] = cactus_sizes[y + 1][x], cactus_sizes[y][x]
					changed = True

	move_to(0, 0)
	harvest()

def dino():	
	change_hat(Hats.Dinosaur_Hat)
	dir = North
	map = ws - 1

	def hat():
		change_hat(Hats.Dinosaur_Hat)
		change_hat(Hats.Dinosaur_Hat)

	while True:
		for i in range(map):
			if not move(dir):
				hat()
		
			if get_pos_y() == map:
				dir = South
				if not move(East):
					hat()
				
			if get_pos_y() == 1 and get_pos_x() == map:
				dir = West
				if not move(South):
					hat()
						
			if get_pos_y() == 1 and dir == South:
				dir = North
				if not move(East):
					hat()
				
			if get_pos_x() == 0 and dir == West:
				dir = North

# Create Maze Here
def create_maze():
	set_world_size(12)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	ws = get_world_size()

	while True:		
		if num_items(Items.Weird_Substance) >= substance:
			plant(Entities.Bush)
			use_item(Items.Weird_Substance, substance)
			return True
		
		if can_harvest():
			harvest()
		else:
			plant(Entities.Bush)

		if num_items(Items.Fertilizer) > item_caps[Items.Fertilizer]:
			use_item(Items.Fertilizer)

# Treasure Hunt Here
current_dir = West

def treasure_hunt():
	global current_dir

	if get_entity_type() == Entities.Treasure:
		harvest()
		return True

	x, y = get_pos_x(), get_pos_y()
	move(current_dir)
	x2, y2 = get_pos_x(), get_pos_y()

	if get_entity_type() == Entities.Treasure:
		harvest()
		return True

	if x == x2 and y == y2:
		if current_dir == West:
			current_dir = North
		elif current_dir == North:
			current_dir = East
		elif current_dir == East:
			current_dir = South
		elif current_dir == South:
			current_dir = West
	else:
		if current_dir == West:
			current_dir = South
		elif current_dir == South:
			current_dir = East
		elif current_dir == East:
			current_dir = North
		elif current_dir == North:
			current_dir = West