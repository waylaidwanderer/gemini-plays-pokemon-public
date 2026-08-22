import mgba
import time

def walk_to_with_flee(tx, ty):
    pos = mgba.get_coordinates()
    print(f"Walking from {pos} to ({tx}, {ty})...")
    
    step_count = 0
    while (pos['x'] != tx or pos['y'] != ty) and step_count < 80:
        dx = tx - pos['x']
        dy = ty - pos['y']
        
        if dx < 0:
            direction = "Left"
        elif dx > 0:
            direction = "Right"
        elif dy < 0:
            direction = "Up"
        elif dy > 0:
            direction = "Down"
        else:
            break
            
        pos_before = pos
        mgba.press_buttons([direction])
        time.sleep(0.55)
        pos = mgba.get_coordinates()
        
        if pos == pos_before:
            print(f"Coordinates did not change at {pos} going {direction} towards ({tx}, {ty}). Checking for battle...")
            # Execute flee sequence
            mgba.press_buttons(["B", "sleep 1000", "Down", "sleep 200", "Right", "sleep 200", "A", "sleep 2000", "B", "sleep 1000"])
            time.sleep(1.0)
            
            # Recheck coordinates
            pos = mgba.get_coordinates()
            if pos == pos_before:
                print("Coordinates still the same. We bumped into a real wall or NPC! Aborting walk.")
                return False
            else:
                print("Successfully fled from battle! Continuing walk...")
        step_count += 1
    return True

print("Starting definitive 3F West toggle run...")
# We are currently at (20, 16) in State A

# Step 1: Walk to 3F West Switch at (2, 12)
path = [
    (20, 15),
    (22, 15),
    (22, 14),
    (24, 14),
    (24, 11),
    (26, 11),
    (26, 3),
    (19, 3),
    (2, 3),
    (2, 12)
]

success = True
for target in path:
    if not walk_to_with_flee(target[0], target[1]):
        success = False
        break

if success:
    pos = mgba.get_coordinates()
    if pos['x'] == 2 and pos['y'] == 12:
        print("At (2, 12) on 3F West. Facing UP to toggle switch to State B...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
        time.sleep(1.5)
        print("Mewtwo switch toggled to State B!")
        
        # Step 2: Walk back to 3F East balcony at (20, 16)
        return_path = [
            (2, 3),
            (19, 3),
            (26, 3),
            (26, 11),
            (24, 11),
            (24, 14),
            (22, 14),
            (22, 15),
            (20, 15),
            (20, 18)  # Try to walk through (20, 17) which is now OPEN in State B!
        ]
        
        return_success = True
        for target in return_path:
            if not walk_to_with_flee(target[0], target[1]):
                return_success = False
                break
                
        if return_success:
            pos_end = mgba.get_coordinates()
            print("Successfully reached (20, 18) in State B! Current pos:", pos_end)
            if pos_end['x'] == 20 and pos_end['y'] == 18:
                print("Stepping Left to drop over the balcony...")
                mgba.press_buttons(["Left"])
                time.sleep(3.0)
                print("Landed on B1F East! Position after drop:", mgba.get_coordinates())
                mgba.take_screenshot()
        else:
            print("Failed return path walk.")
else:
    print("Failed initial path walk.")
