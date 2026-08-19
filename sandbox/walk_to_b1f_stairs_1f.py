import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# Path from (21, 6) to 1F/2F stairs at (5, 10)
path = [
    ('Up', 21, 5), ('Up', 21, 4), ('Up', 21, 3),
    ('Left', 20, 3), ('Left', 19, 3), ('Left', 18, 3), ('Left', 17, 3),
    ('Left', 16, 3), ('Left', 15, 3), ('Left', 14, 3), ('Left', 13, 3),
    ('Left', 12, 3), ('Left', 11, 3), ('Left', 10, 3), ('Left', 9, 3),
    ('Left', 8, 3), ('Left', 7, 3), ('Left', 6, 3), ('Left', 5, 3),
    ('Down', 5, 4), ('Down', 5, 5), ('Down', 5, 6), ('Down', 5, 7),
    ('Down', 5, 8), ('Down', 5, 9), ('Down', 5, 10)
]

print("Walking to 1F/2F stairs...")
step_index = 0
stuck_counter = 0

while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    # Try to take the step
    mgba.press_buttons([btn])
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        print("Step succeeded.")
        step_index += 1
        stuck_counter = 0
    else:
        # Check if we transitioned to 2F (coordinates will jump or stay same but map change)
        # Note: stepping onto (5, 10) warps us to 2F.
        if target_x == 5 and target_y == 10:
            time.sleep(1.0) # wait for warp
            warp_pos = mgba.get_coordinates()
            print("Warped! Position:", warp_pos)
            break
            
        print("Failed to reach target. Checking for battle or blockage...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # Coordinates did not change, might be in a battle
            run_from_battle()
            time.sleep(1)
            # Re-check after battle
            new_pos_after = mgba.get_coordinates()
            # If coordinates are still the same but we are on the path, we can try to re-align
            # We can find the closest path index to new_pos_after
            found = False
            for idx, (b, tx, ty) in enumerate(path):
                if new_pos_after['x'] == tx and new_pos_after['y'] == ty:
                    print(f"Re-aligned to path index {idx}")
                    step_index = idx + 1
                    found = True
                    break
            if not found:
                print("Could not re-align, attempting current step again.")
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
