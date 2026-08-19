import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# We are at (16, 6) on 1F. Let's find all walkable adjacent tiles by trying to step onto them and recording coordinates.
pos = mgba.get_coordinates()
print("Starting coordinate:", pos)

walkable_neighbors = []

for dir_name, dx, dy in [('Up', 0, -1), ('Down', 0, 1), ('Left', -1, 0), ('Right', 1, 0)]:
    curr = mgba.get_coordinates()
    # Try to move
    print(f"Testing direction {dir_name}...")
    mgba.press_buttons([dir_name])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    
    if new_pos['x'] == curr['x'] + dx and new_pos['y'] == curr['y'] + dy:
        print(f"Success! Neighbor at ({new_pos['x']}, {new_pos['y']}) is walkable.")
        walkable_neighbors.append((dir_name, new_pos['x'], new_pos['y']))
        # Move back
        opposite_dir = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}[dir_name]
        mgba.press_buttons([opposite_dir])
        time.sleep(0.3)
    else:
        print(f"Failed to move {dir_name}. Coordinates remained at {curr} (or changed unexpectedly to {new_pos}).")
        # If we got into a battle, we must flee
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # Check if we actually changed floors or did something else
            pass
            
print("Probed walkable neighbors from current position:", walkable_neighbors)
