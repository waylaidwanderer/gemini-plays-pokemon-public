import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# Path to 2F/3F stairs from (3, 3) on 2F
path = [
    ('Down', 3, 4),
    ('Right', 4, 4), ('Right', 5, 4),
    ('Down', 5, 5), ('Down', 5, 6), ('Down', 5, 7), ('Down', 5, 8),
    ('Down', 5, 9), ('Down', 5, 10)
]

print("Walking to 2F/3F stairs...")
step_index = 0
button_count = 0

while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    mgba.press_buttons([btn])
    button_count += 1
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    # Check if we warped to 3F
    if abs(new_pos['x'] - target_x) > 1 or abs(new_pos['y'] - target_y) > 1:
        time.sleep(1.5) # Wait for warp
        warp_pos = mgba.get_coordinates()
        print("Warped to 3F! Position:", warp_pos)
        break
        
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        print("Step succeeded.")
        step_index += 1
    else:
        # Check if we warped on the last step
        if target_x == 5 and target_y == 10:
            time.sleep(1.5)
            warp_pos = mgba.get_coordinates()
            print("Warped to 3F! Position:", warp_pos)
            break
            
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
