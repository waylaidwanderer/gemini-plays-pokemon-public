import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# We are at (12, 12)
# Walk to column 10, then walk DOWN to row 27 (the exit corridor)
path = [
    ('Left', 11, 12), ('Left', 10, 12),
    ('Down', 10, 13), ('Down', 10, 14), ('Down', 10, 15), ('Down', 10, 16),
    ('Down', 10, 17), ('Down', 10, 18), ('Down', 10, 19), ('Down', 10, 20),
    ('Down', 10, 21), ('Down', 10, 22), ('Down', 10, 23), ('Down', 10, 24),
    ('Down', 10, 25), ('Down', 10, 26), ('Down', 10, 27)
]

print("Walking south via column 10...")
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
        print("Approaching execution limit, stopping.")
        break
        
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
                print("Could not re-align, retrying current step.")
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
