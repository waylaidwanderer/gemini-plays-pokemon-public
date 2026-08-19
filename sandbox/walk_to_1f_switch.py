import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

path = [
    # Up to (10, 11)
    ('Up', 10, 25), ('Up', 10, 24), ('Up', 10, 23), ('Up', 10, 22),
    ('Up', 10, 21), ('Up', 10, 20), ('Up', 10, 19), ('Up', 10, 18),
    ('Up', 10, 17), ('Up', 10, 16), ('Up', 10, 15), ('Up', 10, 14),
    ('Up', 10, 13), ('Up', 10, 12), ('Up', 10, 11),
    # Right to (18, 11)
    ('Right', 11, 11), ('Right', 12, 11), ('Right', 13, 11), ('Right', 14, 11),
    ('Right', 15, 11), ('Right', 16, 11), ('Right', 17, 11), ('Right', 18, 11),
    # Up to (18, 7)
    ('Up', 18, 10), ('Up', 18, 9), ('Up', 18, 8), ('Up', 18, 7),
    # Right to (22, 7)
    ('Right', 19, 7), ('Right', 20, 7), ('Right', 21, 7), ('Right', 22, 7),
    # Up to (22, 1)
    ('Up', 22, 6), ('Up', 22, 5), ('Up', 22, 4), ('Up', 22, 3), ('Up', 22, 2), ('Up', 22, 1),
    # Right to (23, 1)
    ('Right', 23, 1)
]

print("Starting walk to 1F Mewtwo switch...")
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
