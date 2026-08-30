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
    print("--- Dynamic Stair Climber (Down to 2F) ---")
    
    # We want to reach (22, 4) by walking UP from (22, 5)
    while True:
        pos = mgba.get_coordinates()
        print("Current position:", pos)
        
        # Check if we warped to 2F East
        # On 2F East, we land at (22, 2) or (22, 1) or similar.
        # But wait, how do we know if we warped?
        # The warp leads to 2F East. If we are on 2F East, we won't see Row 2 shutter gates.
        # But also, we can check if we successfully completed the final Up step onto (22, 4).
        # On 2F, (22, 4) has no warp. If we are on 2F East, (22, 1) or (22, 2) is the landing.
        # Let's take a screenshot and check coordinates after warp.
        
        # If we successfully warped, we will no longer be at 3F East.
        # Let's see: on 3F East, can we have y=4 on column 22?
        # No, because (22, 4) is the stairs warp tile! If we step on it, we warp immediately.
        # If our coordinates show we successfully stepped onto (22, 4) but did not warp (or we are at (22, 2) on 2F),
        # let's look at the result.
        
        if pos['x'] == 22 and pos['y'] == 5:
            # We are at (22, 5). Step Up to trigger the warp!
            print("At (22, 5). Stepping UP to trigger warp...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            
            # Check position after warp
            new_pos = mgba.get_coordinates()
            print("Position after stepping UP:", new_pos)
            mgba.take_screenshot()
            # If we warped, we are done!
            # Since the stairs warp is a map transition, coordinates will update to 2F East landing (22, 5) or similar.
            # Let's check if our Y is different or if we successfully warped.
            break
            
        elif pos['x'] == 23 and pos['y'] == 5:
            # At (23, 5), walk Left to (22, 5)
            if not walk_to_target(22, 5):
                print("Failed to walk to (22, 5)")
                
        elif pos['x'] == 23:
            # On Column 23, walk down to (23, 5)
            if not walk_to_target(23, 5):
                print("Failed to walk to (23, 5)")
                
        else:
            # We are likely at Column 22 or elsewhere. Walk to Column 23.
            # Wait, if we are at (22, 5), we already handle it.
            # If we are at (22, 1), (22, 2), (22, 3), we walk Right to Column 23.
            target_x = 23
            target_y = pos['y']
            if pos['y'] > 5:
                # If we got displaced below row 5, walk to Row 5 first
                target_y = 5
                
            if not walk_to_target(target_x, target_y):
                print(f"Failed to walk to ({target_x}, {target_y})")
                
        time.sleep(0.3)

if __name__ == "__main__":
    main()
