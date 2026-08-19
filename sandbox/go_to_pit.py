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

# We are at (12, 12) on Mansion 3F.
# Path to pit at (24, 5):
# Down to (12, 13)
# Right to (14, 13)
# Up to (14, 7)
# Right to (21, 7)
# Up to (21, 5)
# Right to (24, 5) (this steps into the pit and drops us)

path = [
    ('Down', 12, 13),
    ('Right', 13, 13), ('Right', 14, 13),
    ('Up', 14, 12), ('Up', 14, 11), ('Up', 14, 10), ('Up', 14, 9), ('Up', 14, 8), ('Up', 14, 7),
    ('Right', 15, 7), ('Right', 16, 7), ('Right', 17, 7), ('Right', 18, 7), ('Right', 19, 7), ('Right', 20, 7), ('Right', 21, 7),
    ('Up', 21, 6), ('Up', 21, 5),
    ('Right', 22, 5), ('Right', 23, 5), ('Right', 24, 5)
]

print("Walking to the 3F pit at (24, 5)...")
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

# Step onto (24, 5) is the pit. It should drop us to 1F southeast at (22, 7) (via 2F).
time.sleep(2.0) # Wait for drop transitions
print("Position after drop:", mgba.get_coordinates())
