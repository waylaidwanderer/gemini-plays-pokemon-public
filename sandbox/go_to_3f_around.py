import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

path = [
    ('Right', 6, 7),
    ('Right', 7, 7),
    ('Right', 8, 7),
    ('Up', 8, 6),
    ('Right', 9, 6),
    ('Right', 10, 6),
    ('Right', 11, 6),
    ('Right', 12, 6),
    ('Right', 13, 6),
    ('Up', 13, 5),
    ('Up', 13, 4),
    ('Up', 13, 3),
    ('Right', 14, 3),
    ('Right', 15, 3),
    ('Right', 16, 3),
    ('Right', 17, 3),
    ('Right', 18, 3),
    ('Down', 18, 4),
    ('Right', 19, 4),
    ('Down', 19, 5),
    ('Down', 19, 6),
    ('Down', 19, 7),
    ('Right', 20, 7),
    ('Right', 21, 7),
    ('Right', 22, 7),
    ('Right', 23, 7),
    ('Right', 24, 7),
    ('Down', 24, 8),
    ('Down', 24, 9),
    ('Down', 24, 10),
    ('Left', 23, 10),
    ('Left', 22, 10),
    ('Left', 21, 10),
    ('Left', 20, 10),
    ('Left', 19, 10),
    ('Left', 18, 10),
    ('Left', 17, 10),
    ('Left', 16, 10),
    ('Left', 15, 10),
    ('Left', 14, 10),
    ('Left', 13, 10),
    ('Left', 12, 10),
    ('Left', 11, 10),
    ('Left', 10, 10),
    ('Left', 9, 10),
    ('Left', 8, 10),
    ('Left', 7, 10),
    ('Left', 6, 10),
    ('Left', 5, 10)
]

print("Starting walk around 2F to stairs at (5, 10)...")
step_index = 0
button_count = 0

while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    # If we are already at the target coordinate, skip it
    if pos['x'] == target_x and pos['y'] == target_y:
        print("Already at target coordinate, skipping step.")
        step_index += 1
        continue
        
    mgba.press_buttons([btn])
    button_count += 1
    
    # Wait for movement
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    
    # Check if we transitioned to 3F (or anywhere else)
    if target_x == 5 and target_y == 10 and new_pos['y'] != 10:
        time.sleep(1.5) # Wait for warp
        warp_pos = mgba.get_coordinates()
        print("Warped to 3F! Position:", warp_pos)
        break
        
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        print("Step succeeded.")
        step_index += 1
    else:
        print("Failed step. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # Let's verify if we are in a battle by seeing if position matches a battle screen or we are truly stuck.
            # In battle, coordinates might be static. We'll run the escape sequence.
            # But wait, let's check if the button we just pressed is the same, meaning we were blocked.
            # If we were blocked, the escape sequence will move us off-path. 
            # So, let's check if we actually stepped or if there's a battle.
            # To be safe, let's take a screenshot to see if there's a battle.
            run_from_battle()
            time.sleep(1)
            # Re-align position
            new_pos_after = mgba.get_coordinates()
            print("Position after battle recovery:", new_pos_after)
            found = False
            for idx, (b, tx, ty) in enumerate(path):
                if new_pos_after['x'] == tx and new_pos_after['y'] == ty:
                    print(f"Re-aligned to index {idx}")
                    step_index = idx + 1
                    found = True
                    break
            if not found:
                print("Could not re-align! We might be blocked. Stopping.")
                break
        else:
            print("Position changed, continuing...")
            
    if button_count >= 90:
        print("Reached button limit of 90. Pausing.")
        break

print("Final position:", mgba.get_coordinates())
