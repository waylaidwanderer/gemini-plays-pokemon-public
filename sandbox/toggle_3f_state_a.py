import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

path1 = [
    # Walk to (5, 11) on 1F
    ('Left', 21, 7), ('Left', 20, 7), ('Left', 19, 7), ('Left', 18, 7),
    ('Left', 17, 7), ('Left', 16, 7), ('Left', 15, 7), ('Left', 14, 7),
    ('Left', 13, 7), ('Left', 12, 7), ('Left', 11, 7), ('Left', 10, 7),
    ('Down', 10, 8), ('Down', 10, 9), ('Down', 10, 10), ('Down', 10, 11),
    ('Left', 9, 11), ('Left', 8, 11), ('Left', 7, 11), ('Left', 6, 11), ('Left', 5, 11)
]

print("Walking to 1F stairs...")
step_index = 0
while step_index < len(path1):
    btn, target_x, target_y = path1[step_index]
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

# Now we are at (5, 11) on 1F. Let's go Up to 2F.
print("Climbing to 2F...")
mgba.press_buttons(["Up", "sleep 1500"])
time.sleep(1.5)

# Now we are on 2F at (5, 11). Let's go Up to 3F.
print("Climbing to 3F...")
mgba.press_buttons(["Up", "sleep 1500"])
time.sleep(1.5)

# Now we are on 3F at (5, 11). Let's walk to (2, 12).
path2 = [
    ('Down', 5, 12),
    ('Left', 4, 12), ('Left', 3, 12), ('Left', 2, 12)
]

print("Walking to Mewtwo statue on 3F...")
step_index = 0
while step_index < len(path2):
    btn, target_x, target_y = path2[step_index]
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

# Turn Up to face the statue and toggle switch
print("Facing statue...")
mgba.press_buttons(["Up", "sleep 500"])
time.sleep(0.5)

print("Toggling switch to State A...")
mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "A", "sleep 500", "A", "sleep 500"])
time.sleep(2)

print("Done!")
pos = mgba.get_coordinates()
print("Final Position:", pos)
