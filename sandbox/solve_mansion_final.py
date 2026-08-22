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
        mgba.press_buttons(["B", "sleep 550"]) # let emulator advance
        pos = mgba.get_coordinates()
        
        if pos == pos_before:
            print(f"Coordinates did not change at {pos} going {direction} towards ({tx}, {ty}). Checking for battle...")
            # Wait for battle transition to complete
            mgba.press_buttons(["B", "sleep 3500"])
            
            # Execute flee sequence
            print("Executing flee sequence...")
            mgba.press_buttons(["B", "sleep 1500", "Down", "sleep 300", "Right", "sleep 300", "A", "sleep 2500", "B", "sleep 1000"])
            mgba.press_buttons(["B", "sleep 8000"]) # Let escape animation finish
            
            # Recheck coordinates
            pos = mgba.get_coordinates()
            if pos == pos_before:
                print("Coordinates still the same. We bumped into a real wall or NPC! Aborting walk.")
                return False
            else:
                print("Successfully fled from battle! Continuing walk...")
        step_count += 1
    return True

pos = mgba.get_coordinates()
print("Starting balcony return run in State B from:", pos)

# We are currently at (2, 11). Walk back to the balcony at (20, 18)
return_path = [
    (2, 3),
    (26, 3),
    (26, 11),
    (24, 11),
    (24, 14),
    (22, 14),
    (22, 15),
    (20, 15),
    (20, 18) # Gate is open in State B!
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
        mgba.press_buttons(["Left", "sleep 3000"])
        print("Landed on B1F! Position after drop:", mgba.get_coordinates())
        mgba.take_screenshot()
else:
    print("Failed return path walk.")
