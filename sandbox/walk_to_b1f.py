import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

# 1. Walk from (1, 5) to (3, 8) to warp to main Mansion 1F
print("Warping to main Mansion 1F...")
path1 = [
    ('Right', 2, 5), ('Right', 3, 5),
    ('Down', 3, 6), ('Down', 3, 7), ('Down', 3, 8)
]
step_index = 0
while step_index < len(path1):
    btn, target_x, target_y = path1[step_index]
    mgba.press_buttons([btn])
    time.sleep(0.3)
    step_index += 1

time.sleep(1.5) # Wait for warp transition
pos = mgba.get_coordinates()
print("Warped inside Mansion 1F, current pos:", pos)

# 2. Walk to northeast stairs at (22, 2) on Mansion 1F
path2 = [
    # Up to row 2
    ('Up', 12, 4), ('Up', 12, 3), ('Up', 12, 2),
    # Right to (22, 2)
    ('Right', 13, 2), ('Right', 14, 2), ('Right', 15, 2), ('Right', 16, 2),
    ('Right', 17, 2), ('Right', 18, 2), ('Right', 19, 2), ('Right', 20, 2),
    ('Right', 21, 2), ('Right', 22, 2)
]

print("Walking to northeast stairs at (22, 2)...")
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

print("Reached northeast stairs!")
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
