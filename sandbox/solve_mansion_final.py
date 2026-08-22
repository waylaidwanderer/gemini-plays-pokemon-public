import mgba
import time

def walk_to_step(tx, ty):
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
            print(f"Coordinates did not change at {pos} going {direction} towards ({tx}, {ty}). Likely a battle or real block! Exiting script.")
            return False
        step_count += 1
    return True

pos = mgba.get_coordinates()
print("Starting definitive State B balcony drop-off run from:", pos)

# We are currently at (22, 7) in State B.
# Walk Left to Column 19, UP Column 19 to Row 3, Right to Column 26, and Down to balcony!
path = [
    (19, 7),
    (19, 3),
    (26, 3),
    (26, 11),
    (24, 11),
    (24, 14),
    (22, 14),
    (22, 15),
    (20, 15),
    (20, 18)
]

success = True
for target in path:
    if not walk_to_step(target[0], target[1]):
        success = False
        break

if success:
    pos_end = mgba.get_coordinates()
    print("Successfully reached (20, 18) in State B! Current pos:", pos_end)
    if pos_end['x'] == 20 and pos_end['y'] == 18:
        print("Stepping Left to drop over the balcony...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0)
        print("Landed on B1F East! Position after drop:", mgba.get_coordinates())
        mgba.take_screenshot()
else:
    print("Walk interrupted. Handle the situation, then run the script again!")
