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
        
        print(f"Walking {direction} to ({tx}, {ty}) from {pos}...")
        mgba.press_buttons([direction])
        time.sleep(0.6)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            attempts += 1
            print("No movement. Fleeing battle...")
            flee_battle()
        else:
            attempts = 0
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
    return False

def main():
    print("--- Systematic Stair / Warp Search on 3F East ---")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # 1. Walk from (26, 12) to (22, 3) via Row 12, Column 24, and Row 3
    # Wait, in State B, Column 22 on Row 12 is blocked, but Column 24 and 25 are open!
    # Let's trace a safe path to (22, 3):
    # - Walk Left to Column 24: (25, 12), (24, 12)
    # - Walk Up Column 24 to Row 3: (24, 11), (24, 10), (24, 9), (24, 8), (24, 7), (24, 6), (24, 5), (24, 4), (24, 3)
    # - Walk Left to Column 22: (23, 3), (22, 3)
    path = [
        (25, 12), (24, 12),
        (24, 11), (24, 10), (24, 9), (24, 8), (24, 7), (24, 6), (24, 5), (24, 4), (24, 3),
        (23, 3), (22, 3)
    ]
    
    print("Walking to (22, 3)...")
    for tx, ty in path:
        if not walk_to_target(tx, ty):
            print(f"Failed to reach ({tx}, {ty})")
            return
            
    # 2. Walk Up to (22, 2)
    if not walk_to_target(22, 2):
        print("Failed to reach (22, 2)")
        return
        
    # 3. Walk Up to (22, 1)
    if not walk_to_target(22, 1):
        print("Failed to reach (22, 1)")
        return
        
    # 4. Try walking UP into (22, 0)
    print("Testing UP onto (22, 0)...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    new_pos = mgba.get_coordinates()
    print("Position after UP:", new_pos)
    
    if new_pos['y'] == 0:
        # We moved to Row 0! Check if we warped
        print("Moved to Row 0! Check if warp triggers.")
        mgba.take_screenshot()
        # Walk Left/Right to find warp on Row 0
        for x in [21, 23]:
            print(f"Walking to ({x}, 0)...")
            mgba.press_buttons(["Left" if x < new_pos['x'] else "Right"])
            time.sleep(1.5)
            chk_pos = mgba.get_coordinates()
            print("Position:", chk_pos)
            mgba.take_screenshot()
            
    # 5. Try walking Left to (21, 1) and Right to (23, 1)
    print("Testing other tiles on Row 1...")
    for x in [21, 23]:
        print(f"Walking to ({x}, 1)...")
        if walk_to_target(x, 1):
            # Try walking UP from there
            print("Testing UP from here...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            chk_pos = mgba.get_coordinates()
            print("Position:", chk_pos)
            mgba.take_screenshot()

if __name__ == "__main__":
    main()
