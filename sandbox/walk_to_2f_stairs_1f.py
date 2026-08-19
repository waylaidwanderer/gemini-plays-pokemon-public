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

# We are at (10, 13) inside Mansion 1F.
# Walk to 2F stairs at (5, 10)
path = [
    ('Left', 9, 13), ('Left', 8, 13), ('Left', 7, 13), ('Left', 6, 13), ('Left', 5, 13),
    ('Up', 5, 12), ('Up', 5, 11), ('Up', 5, 10)
]

print("Walking to 2F stairs at (5, 10)...")
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
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

# Step onto (5, 10) is the warp to 2F. Once we are at (5, 10), it warps us to 2F at (5, 11)
time.sleep(2.0) # Wait for warp transition
print("Warped position inside Mansion 2F:", mgba.get_coordinates())
