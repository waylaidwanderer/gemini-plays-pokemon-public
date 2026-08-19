import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

path = [
    # Left to (10, 12)
    ('Left', 12, 12), ('Left', 11, 12), ('Left', 10, 12),
    # Up to (10, 7)
    ('Up', 10, 11), ('Up', 10, 10), ('Up', 10, 9), ('Up', 10, 8), ('Up', 10, 7),
    # Right to (22, 7)
    ('Right', 11, 7), ('Right', 12, 7), ('Right', 13, 7), ('Right', 14, 7),
    ('Right', 15, 7), ('Right', 16, 7), ('Right', 17, 7), ('Right', 18, 7),
    ('Right', 19, 7), ('Right', 20, 7), ('Right', 21, 7), ('Right', 22, 7),
    # Up to (22, 1)
    ('Up', 22, 6), ('Up', 22, 5), ('Up', 22, 4), ('Up', 22, 3), ('Up', 22, 2), ('Up', 22, 1),
    # Right to (23, 1)
    ('Right', 23, 1)
]

print("Starting walk to 1F Mewtwo switch (Route 3)...")
step_index = 0
while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    # Try to take the step
    mgba.press_buttons([btn])
    time.sleep(0.3)  # wait for movement to complete
    
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

print("Reached 1F switch!")
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
