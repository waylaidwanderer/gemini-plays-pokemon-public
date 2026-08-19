import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    # First press B/A to clear any "appeared" or "Go!" text
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])
    # Press Right, Down, A to flee
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 2000"])
    # Dismiss "Got away safely!" text
    mgba.press_buttons(["B", "sleep 500"])
    time.sleep(1)

# 1. Dismiss "Got away safely!" text box if it's currently on screen
print("Dismissing 'Got away safely!' text...")
mgba.press_buttons(["B", "sleep 500"])
time.sleep(1.0)

# 2. Walk from (5, 24) to (21, 24)
path = []
for col in range(6, 22):
    path.append(('Right', col, 24))

print("Walking Right to B1F stairs at (21, 24)...")
step_index = 0
while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    # Try to take the step
    mgba.press_buttons([btn])
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        print("Step succeeded.")
        step_index += 1
    else:
        print("Failed to reach target. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # Coordinates didn't change, we are stuck. Try to flee a battle.
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

# Step onto (21, 24) is the warp to B1F. Once we are at (21, 24), it warps us!
time.sleep(2.0) # Wait for warp transition
print("Warped position inside B1F:", mgba.get_coordinates())
