from helpers import *

# --- Configuration (Set your preferred crops) ---
# Use Entities.Name for crops
CROP_A = Entities.Carrot
CROP_B = Entities.Grass # Companion crop (e.g., Hay)

# --- Drone Worker Function (Executed by SPAWNED drones) ---

# This function defines what a single drone does at a specific tile.
def polyculture_work():
    # 1. Tilling
    if get_ground_type() != Grounds.Soil:
        till()
        
    # 2. Watering (Adjust threshold as needed)
    if get_water() < 0.5:
        use_item(Items.Water)
        
    # 3. Harvest
    if can_harvest():
        harvest()
        
    # 4. Polyculture Planting (Checkerboard Pattern)
    # Get current position
    x = get_pos_x()
    y = get_pos_y()
    
    # Plant only if the tile is empty (after harvest or initially)
    if get_entity_type() == None:
        # Checkerboard logic: (x+y) is even or odd
        if (x + y) % 2 == 0:
            plant(CROP_A)
        else:
            plant(CROP_B)

# --- Main Drone Script (Continuously Spawns Workers) ---

# Get world size once (e.g., a 4x4 farm would be 4)
WORLD_SIZE = get_world_size()

# The main drone will iterate through the entire grid, spawning a worker 
# on each tile to do the actual work.
while True:
    # Iterate through all x and y coordinates (0 to WORLD_SIZE - 1)
    for y in range(WORLD_SIZE):
        for x in range(WORLD_SIZE):
            
            # 1. Move the main drone to the target tile (x, y)
            move_to(x, y)
            
            # 2. Spawn a worker drone at the current position
            # The worker drone will execute polyculture_work() on this tile, then disappear.
            # This is where your parallelization happens.
            spawn_drone(polyculture_work)
            
            # NOTE: We can't tell if spawn_drone returned None (max drones reached)
            # but that's okay. The script will just keep trying on the next tile.

# --- Helper Function Definitions ---

# Simplistic movement function (for the main drone)
def move_to(x, y):
    # This movement code should be placed outside the main loop/worker function
    # but inside the same file as the 'while True' loop for your game parser.
    
    # Move X
    current_x = get_pos_x()
    while current_x < x:
        move(East)
        current_x = current_x + 1
    while current_x > x:
        move(West)
        current_x = current_x - 1
        
    # Move Y
    current_y = get_pos_y()
    while current_y < y:
        move(North)
        current_y = current_y + 1
    while current_y > y:
        move(South)
        current_y = current_y - 1