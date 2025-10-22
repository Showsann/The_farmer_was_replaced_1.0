from helpers import *
from farm import *
# Just used to keep the farm simple
#set_world_size(12)

# A shared function that all drones can use
# You can create these kind of functions to help you share
# functiona;lity easily
def HarvestColumn(forever = True):
	if forever:
		while True:
			cactus()
	else:
		for i in range(ws):
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			move(North)

while True:
	if spawn_drone(HarvestColumn):
		move(East)