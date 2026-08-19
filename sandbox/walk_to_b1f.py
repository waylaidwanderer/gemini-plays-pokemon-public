import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

path = [
    # Down along column 5 to row 27
    ('Down', 5, 12), ('Down', 5, 13), ('Down', 5, 14), ('Down', 5, 15),
    ('Down', 5, 16), ('Down', 5, 17), ('Down', 5, 18), ('Down', 5, 19),
    ('Down', 5, 20), ('Down', 5, 21), ('Down', 5, 22), ('Down', 5, 23),
    ('Down', 5, 24), ('Down', 5, 25), ('Down', 5, 26), ('Down', 5, 27),
    # Right along row 27 to column 21
    ('Right', 6, 27), ('Right', 7, 27), ('Right', 8, 27), ('Right', 9, 27),
    ('Right', 10, 27), ('Right', 11, 27), ('Right', 12, 27), ('Right', 13, 27),
    ('Right', 14, 27), ('Right', 15, 27), ('Right', 16, 27), ('Right', 17, 27),
    ('Right', 18, 27), ('Right', 19, 27), ('Right', 20, 27), ('Right', 21, 27),
    # Up along column 21 to row 24 (stairs to B1F)
    ('Up', 21, 26), ('Up', 21, 25), ('Up', 21, 24)
]

print("Starting walk to B1F stairs...")
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
            # We are definitely in a battle (or bumped)
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

print("Reached B1F stairs area!")
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
