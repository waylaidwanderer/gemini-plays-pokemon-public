import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

# 1. Walk on Cinnabar Island from (14, 13) to (5, 13)
path_outside1 = [
    ('Left', 13, 13), ('Left', 12, 13), ('Left', 11, 13), ('Left', 10, 13),
    ('Left', 9, 13), ('Left', 8, 13), ('Left', 7, 13), ('Left', 6, 13), ('Left', 5, 13)
]

print("Walking to column 5 outside...")
for btn, tx, ty in path_outside1:
    mgba.press_buttons([btn])
    time.sleep(0.3)

# 2. Walk Up column 5 to (5, 3), and Right to (6, 3) to enter Mansion
path_outside2 = [
    ('Up', 5, 12), ('Up', 5, 11), ('Up', 5, 10), ('Up', 5, 9),
    ('Up', 5, 8), ('Up', 5, 7), ('Up', 5, 6), ('Up', 5, 5),
    ('Up', 5, 4), ('Up', 5, 3),
    ('Right', 6, 3)
]

print("Walking to Mansion entrance...")
for btn, tx, ty in path_outside2:
    mgba.press_buttons([btn])
    time.sleep(0.3)

print("Entering Mansion...")
time.sleep(1.5) # Wait for transition

# 3. Walk from (5, 27) to (21, 24) on Mansion 1F
path_inside = [
    # Right to (21, 27)
    ('Right', 6, 27), ('Right', 7, 27), ('Right', 8, 27), ('Right', 9, 27),
    ('Right', 10, 27), ('Right', 11, 27), ('Right', 12, 27), ('Right', 13, 27),
    ('Right', 14, 27), ('Right', 15, 27), ('Right', 16, 27), ('Right', 17, 27),
    ('Right', 18, 27), ('Right', 19, 27), ('Right', 20, 27), ('Right', 21, 27),
    # Up to (21, 24)
    ('Up', 21, 26), ('Up', 21, 25), ('Up', 21, 24)
]

print("Walking to B1F stairs inside Mansion 1F...")
step_index = 0
while step_index < len(path_inside):
    btn, target_x, target_y = path_inside[step_index]
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

print("Reached B1F stairs!")
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
