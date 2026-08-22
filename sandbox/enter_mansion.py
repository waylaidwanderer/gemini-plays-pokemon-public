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
            print(f"BUMPED at {pos} going {direction} towards ({tx}, {ty})")
            # If we bumped, try to move around or exit
            return False
        step_count += 1
    return True

# Ensure we walk safely around the NPC
if walk_to_step(13, 6):
    if walk_to_step(11, 6):
        if walk_to_step(11, 4):
            if walk_to_step(6, 4):
                if walk_to_step(6, 3):
                    print("At door. Entering...")
                    mgba.press_buttons(["Up"])
                    time.sleep(2.0)
                    pos_inside = mgba.get_coordinates()
                    print("Landed inside Mansion! Position:", pos_inside)
                    
                    # Walk UP immediately to clear exit warp
                    mgba.press_buttons(["Up"])
                    time.sleep(0.55)
                    mgba.press_buttons(["Up"])
                    time.sleep(0.55)
                    mgba.press_buttons(["Up"])
                    time.sleep(0.55)
                    mgba.press_buttons(["Up"])
                    time.sleep(0.55)
                    print("Safe position inside Mansion 1F:", mgba.get_coordinates())
                    mgba.take_screenshot()
