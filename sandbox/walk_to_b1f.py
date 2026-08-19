import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

# 1. Exit Pokemon Center
print("Exiting Pokemon Center...")
mgba.press_buttons(["Down", "Down"])
time.sleep(1.5)

# 2. Walk to Mansion entrance outside on Cinnabar Island
# We land outside around (11, 13). Walk Left 5 steps to (6, 13), Up 10 steps to (6, 3).
print("Walking to Mansion entrance...")
mgba.press_buttons(["Left", "Left", "Left", "Left", "Left", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up"])
time.sleep(3.0)

# Now we should be inside Mansion 1F at (5, 27). Let's verify coordinates.
pos = mgba.get_coordinates()
print("Entered Mansion, current pos:", pos)

# 3. Walk from (5, 27) to (21, 24) on Mansion 1F
path = [
    # Right to (21, 27)
    ('Right', 6, 27), ('Right', 7, 27), ('Right', 8, 27), ('Right', 9, 27),
    ('Right', 10, 27), ('Right', 11, 27), ('Right', 12, 27), ('Right', 13, 27),
    ('Right', 14, 27), ('Right', 15, 27), ('Right', 16, 27), ('Right', 17, 27),
    ('Right', 18, 27), ('Right', 19, 27), ('Right', 20, 27), ('Right', 21, 27),
    # Up to (21, 24)
    ('Up', 21, 26), ('Up', 21, 25), ('Up', 21, 24)
]

print("Walking to B1F stairs on Mansion 1F...")
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

print("Reached B1F stairs!")
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
