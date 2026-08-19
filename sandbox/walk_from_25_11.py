import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 500"])
    time.sleep(1)

# 1. Dismiss 'Got away safely!' text
print("Dismissing 'Got away safely!' text...")
mgba.press_buttons(["B", "sleep 500"])
time.sleep(1.0)

# Path to B1F stairs starting from (25, 11):
path = [
    ('Up', 25, 10), ('Up', 25, 9), ('Up', 25, 8), ('Up', 25, 7),
    ('Up', 25, 6), ('Up', 25, 5), ('Up', 25, 4), ('Up', 25, 3),
    ('Left', 24, 3), ('Left', 23, 3), ('Left', 22, 3), ('Left', 21, 3), ('Left', 20, 3), ('Left', 19, 3),
    ('Down', 19, 4), ('Down', 19, 5), ('Down', 19, 6), ('Down', 19, 7), ('Down', 19, 8),
    ('Down', 19, 9), ('Down', 19, 10), ('Down', 19, 11), ('Down', 19, 12), ('Down', 19, 13),
    ('Down', 19, 14), ('Down', 19, 15), ('Down', 19, 16), ('Down', 19, 17), ('Down', 19, 18),
    ('Down', 19, 19), ('Down', 19, 20), ('Down', 19, 21), ('Down', 19, 22), ('Down', 19, 23),
    ('Down', 19, 24),
    ('Right', 20, 24), ('Right', 21, 24)
]

print("Walking to B1F stairs...")
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

# Step onto (21, 24) is the stairs to B1F.
time.sleep(2.0)
print("Position after warp:", mgba.get_coordinates())
