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
            return False
        step_count += 1
    return True

# 1. Walk to Nurse Joy's counter at (3, 3)
if walk_to_step(3, 3):
    print("At Nurse Joy's counter. Healing...")
    mgba.press_buttons(["Up", "sleep 300"])
    # Talk and heal
    mgba.press_buttons(["A", "sleep 1500", "A", "sleep 1500", "A", "sleep 5000", "A", "sleep 1000", "A", "sleep 1000", "B"])
    time.sleep(11.0)
    
    # Exit Pokemon Center: Walk DOWN to (3, 8) to trigger warp
    print("Exiting Pokemon Center...")
    mgba.press_buttons(["Down", "sleep 300", "Down", "sleep 300", "Down", "sleep 300", "Down", "sleep 300", "Down", "sleep 300", "Down", "sleep 2000"])
    time.sleep(4.0) # Wait for map transition to Cinnabar Island!
    
    pos = mgba.get_coordinates()
    print("Position outside Pokemon Center:", pos)
    
    if pos['x'] == 11 and pos['y'] == 12:
        # Walk to Pokemon Mansion entrance at (6, 3)
        if walk_to_step(6, 12):
            if walk_to_step(6, 3):
                print("At Mansion entrance doormat. Entering...")
                mgba.press_buttons(["Up"])
                time.sleep(2.0) # Wait for map transition!
                print("Landed inside Mansion 1F! Current position:", mgba.get_coordinates())
                mgba.take_screenshot()
