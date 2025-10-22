from helpers import item_caps
from farm import hay, bushes, carrots, trees, pumpkins, sunflower, poly, cactus, dino, create_maze, treasure_hunt

while True:
	if num_items(Items.Hay) < item_caps[Items.Hay]:
		hay()
	elif num_items(Items.Wood) < item_caps[Items.Wood]:
		change_hat(Hats.Brown_Hat)
		poly()
	elif num_items(Items.Carrot) < item_caps[Items.Carrot]:
		change_hat(Hats.Carrot_Hat)
		poly()
	elif num_items(Items.Power) < item_caps[Items.Power] and num_items(Items.Fertilizer) > item_caps[Items.Fertilizer]:
		clear()
		change_hat(Hats.Traffic_Cone)
		sunflower()
	elif num_items(Items.Pumpkin) < item_caps[Items.Pumpkin]:
		clear()
		change_hat(Hats.Purple_Hat)
		pumpkins()
	elif num_items(Items.Cactus) < item_caps[Items.Cactus]:
		change_hat(Hats.Green_Hat)
		cactus()
	elif num_items(Items.Bone) < item_caps[Items.Bone]:
		dino()
	elif num_items(Items.Gold) < item_caps[Items.Gold]:
		if not create_maze():
			continue
		treasure_hunt()
	else:
		do_a_flip()
