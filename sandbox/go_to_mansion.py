import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# We are at (12, 13) outside on Cinnabar Island.
# Walk Left to column 6, then UP to (6, 9) (Mansion entrance)
path = [
    ('Left', 11, 13), ('Left', 10, 13), ('Left', 9, 13), ('Left', 8, 13),
    ('Left', 7, 13), ('Left', 6, 13),
    ('Up', 6, 12), ('Up', 6, 11), ('Up', 6, 10),
    ('Up', 6, 9) # step into the Mansion door!
]

print("Walking to Mansion entrance...")
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
    # Check if we warped inside Mansion (coordinates will jump or go out of range)
    if new_pos['y'] > 20 or new_pos['x'] > 20: # Mansion inside is larger
        time.sleep(1.5) # Wait for warp
        print("Warped into Pokémon Mansion! Position:", mgba.get_coordinates())
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
