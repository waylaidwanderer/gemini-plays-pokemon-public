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
            chk_pos = mgba.get_coordinates()
            if chk_pos['x'] != pos['x'] or chk_pos['y'] != pos['y']:
                print(f"Displaced to {chk_pos}")
                return False
        else:
            attempts = 0
            if new_pos['x'] != tx or new_pos['y'] != ty:
                # We warped/fell!
                print(f"WARP/FALL DETECTED! Landed at: {new_pos}")
                mgba.take_screenshot()
                return "WARPED"
                
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
    return False

def main():
    print("--- Systematic Pitfall Search on 3F East (State B) ---")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We are currently at (24, 18).
    # Walk to (24, 16) first
    if not walk_to_target(24, 16):
        print("Failed to reach (24, 16)")
        return
        
    # We will probe the following grid of tiles in State B:
    # Row 14, 15, 16 on Columns 24, 25, 26, 27, 28
    # Since Row 16 is open horizontally, we can walk Left/Right on Row 16, and step Up to probe Row 15 and Row 14!
    probe_cols = [24, 25, 26, 27, 28]
    for col in probe_cols:
        print(f"\n--- Probing Column {col} ---")
        # 1. Walk to (col, 16)
        res = walk_to_target(col, 16)
        if res == "WARPED": return
        if not res: continue
        
        # 2. Walk Up to (col, 15)
        res = walk_to_target(col, 15)
        if res == "WARPED": return
        if not res: continue
        
        # 3. Walk Up to (col, 14)
        res = walk_to_target(col, 14)
        if res == "WARPED": return
        if not res: continue
        
        # 4. Walk back Down to (col, 16)
        res = walk_to_target(col, 15)
        if res == "WARPED": return
        res = walk_to_target(col, 16)
        if res == "WARPED": return

    print("Finished probing lower East grid. No pitfall triggered.")
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
