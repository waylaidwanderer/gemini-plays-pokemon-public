import mgba
import time

def walk_to_step_island(tx, ty):
    pos = mgba.get_coordinates()
    print(f"Walking on Island from {pos} to ({tx}, {ty})...")
    
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
            print(f"BUMPED on Island at {pos} going {direction} towards ({tx}, {ty})")
            return False
        step_count += 1
    return True

# 1. Dismiss "The door is locked.."
print("Dismissing locked door text...")
mgba.press_buttons(["B", "sleep 1000"])

# 2. Walk to Mansion entrance and enter
if walk_to_step_island(6, 4):
    if walk_to_step_island(6, 3):
        print("At Mansion entrance. Entering...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0) # Wait for transition
        pos = mgba.get_coordinates()
        print("Landed inside Mansion 1F! Position:", pos)
        
        # 3. Walk UP immediately to avoid warping out!
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        print("Position inside after walking UP:", mgba.get_coordinates())
        mgba.take_screenshot()
