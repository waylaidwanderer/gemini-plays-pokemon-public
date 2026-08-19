import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# Path to exit from (28, 12)
path = [
    ('Left', 27, 12), ('Left', 26, 12), ('Left', 25, 12),
    ('Down', 25, 13), ('Down', 25, 14),
    ('Right', 26, 14),
    ('Down', 26, 15), ('Down', 26, 16), ('Down', 26, 17), ('Down', 26, 18),
    ('Down', 26, 19), ('Down', 26, 20), ('Down', 26, 21), ('Down', 26, 22),
    ('Down', 26, 23), ('Down', 26, 24), ('Down', 26, 25), ('Down', 26, 26),
    ('Down', 26, 27), ('Down', 26, 28) # step down to trigger exit warp
]

print("Starting walk to exit from (28, 12)...")
step_index = 0
button_count = 0

while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    mgba.press_buttons([btn])
    button_count += 1
    time.sleep(0.3)
    
    if button_count >= 80:
        print("Approaching execution limit, pausing script.")
        break
        
    new_pos = mgba.get_coordinates()
    
    # Check if we exited the Mansion (x coordinate will reset or y coordinate will go out of Mansion range)
    if new_pos['y'] > 27 or new_pos['x'] < 2:
        print("Warped out of Mansion! Position:", new_pos)
        break
        
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

print("Final position:", mgba.get_coordinates())
