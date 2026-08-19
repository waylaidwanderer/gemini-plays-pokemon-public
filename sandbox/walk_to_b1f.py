import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

path = [
    # Up to (5, 11)
    ('Up', 5, 14), ('Up', 5, 13), ('Up', 5, 12), ('Up', 5, 11),
    # Right to (10, 11)
    ('Right', 6, 11), ('Right', 7, 11), ('Right', 8, 11), ('Right', 9, 11), ('Right', 10, 11),
    # Down to (10, 27)
    ('Down', 10, 12), ('Down', 10, 13), ('Down', 10, 14), ('Down', 10, 15),
    ('Down', 10, 16), ('Down', 10, 17), ('Down', 10, 18), ('Down', 10, 19),
    ('Down', 10, 20), ('Down', 10, 21), ('Down', 10, 22), ('Down', 10, 23),
    ('Down', 10, 24), ('Down', 10, 25), ('Down', 10, 26), ('Down', 10, 27),
    # Right to (21, 27)
    ('Right', 11, 27), ('Right', 12, 27), ('Right', 13, 27), ('Right', 14, 27),
    ('Right', 15, 27), ('Right', 16, 27), ('Right', 17, 27), ('Right', 18, 27),
    ('Right', 19, 27), ('Right', 20, 27), ('Right', 21, 27),
    # Up to (21, 24)
    ('Up', 21, 26), ('Up', 21, 25), ('Up', 21, 24)
]

print("Starting walk to B1F stairs (Route 2)...")
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

print("Reached B1F stairs!")
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
