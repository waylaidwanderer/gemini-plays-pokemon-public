import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Starting walk from (8, 13) on 2F to 3F stairs at (5, 10)...")
path = [
    ('Up', 8, 12),
    ('Up', 8, 11),
    ('Left', 7, 11),
    ('Left', 6, 11),
    ('Left', 5, 11),
    ('Up', 5, 10)
]

step_index = 0
button_count = 0

while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    # Check if we warped to 3F
    if target_x == 5 and target_y == 10 and (pos['x'] != 5 or pos['y'] != 10) and step_index > 4:
        print("Warp detected! We warped to 3F.")
        break
        
    mgba.press_buttons([btn])
    button_count += 1
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    
    # If we reached the final step, wait for warp to complete
    if target_x == 5 and target_y == 10 and (new_pos['x'] != 5 or new_pos['y'] != 10):
        time.sleep(1.5) # Wait for warp
        print("Warped to 3F! Position:", mgba.get_coordinates())
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
            
    if button_count >= 80:
        print("Reached button limit of 80.")
        break

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
