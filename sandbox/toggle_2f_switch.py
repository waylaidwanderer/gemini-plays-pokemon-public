import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking UP column 5 to (5, 4) to check Mewtwo statue at (5, 3)...")
path = [
    ('Up', 5, 9),
    ('Up', 5, 8),
    ('Up', 5, 7),
    ('Up', 5, 6),
    ('Up', 5, 5),
    ('Up', 5, 4)
]

step_index = 0
button_count = 0

while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
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
            # Re-align
            new_pos_after = mgba.get_coordinates()
            found = False
            for idx, (b, tx, ty) in enumerate(path):
                if new_pos_after['x'] == tx and new_pos_after['y'] == ty:
                    print(f"Re-aligned to index {idx}")
                    step_index = idx + 1
                    found = True
                    break
            if not found:
                print("Could not re-align, retrying step.")
        else:
            print("Position changed, continuing...")

# Once at (5, 4), face UP and interact
pos = mgba.get_coordinates()
if pos['x'] == 5 and pos['y'] == 4:
    print("Facing UP towards the Mewtwo statue at (5, 3)...")
    mgba.press_buttons(["Up", "sleep 300"])
    print("Pressing A to see if there is a switch...")
    mgba.press_buttons(["A", "sleep 1000"])
    
    # Take a screenshot to verify what happened
    img = mgba.take_screenshot()
    print("Screenshot taken:", img)
else:
    print("Failed to reach (5, 4)!")
