import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# We are at (17, 7) on 2F.
# Let's walk to (5, 4) and try to interact with the Mewtwo statue at (5, 3)
path = [
    ('Left', 16, 7), ('Left', 15, 7), ('Left', 14, 7), ('Left', 13, 7),
    ('Left', 12, 7), ('Left', 11, 7), ('Left', 10, 7), ('Left', 9, 7),
    ('Left', 8, 7), ('Left', 7, 7), ('Left', 6, 7), ('Left', 5, 7),
    ('Up', 5, 6), ('Up', 5, 5), ('Up', 5, 4)
]

print("Walking to (5, 4) on 2F...")
step_index = 0
button_count = 0

while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"At {pos}, pressing {btn} to reach ({target_x}, {target_y})")
    
    mgba.press_buttons([btn])
    button_count += 1
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        print("Step succeeded.")
        step_index += 1
    else:
        print("Failed step. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

# At (5, 4), face UP towards the statue at (5, 3) and press A
if mgba.get_coordinates() == {'x': 5, 'y': 4}:
    print("Facing UP towards Mewtwo statue at (5, 3)...")
    mgba.press_buttons(["Up", "sleep 300"])
    print("Pressing A...")
    mgba.press_buttons(["A", "sleep 1000"])
    # If a text box appeared, take a screenshot
    scr = mgba.take_screenshot()
    print("Interacted screenshot:", scr)
    # Dismiss any text box
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])

print("Final position:", mgba.get_coordinates())
