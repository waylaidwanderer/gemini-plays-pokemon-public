import mgba
import time

def flee_battle():
    print("Fleeing battle...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.4)

def walk_to_target(tx, ty):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
        
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        else: break
        
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            attempts += 1
            flee_battle()
        else:
            attempts = 0
    return mgba.get_coordinates() == {'x': tx, 'y': ty}

def main():
    print("Walking to northeast stairs at (22, 1)...")
    path = [
        (26, 3), (26, 2), (26, 1),
        (25, 1), (24, 1), (23, 1), (22, 1)
    ]
    
    for i, target in enumerate(path):
        tx, ty = target
        print(f"[{i}] Moving to ({tx}, {ty})...")
        if not walk_to_target(tx, ty):
            print(f"Failed to reach ({tx}, {ty})")
            return
            
    # Once at (22, 1), step UP to trigger stairs warp
    print("Stepping UP to trigger warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Position after warp:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
