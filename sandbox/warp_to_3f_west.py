import mgba
import time

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

# Phase 1: Walk UP on Cinnabar to enter Mansion 1F West
steps_outside = [
    ("Up", {"x": 6, "y": 12}),
    ("Up", {"x": 6, "y": 11}),
    ("Up", {"x": 6, "y": 10}),
]

success = True
for direction, coords in steps_outside:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Stepping UP into door at (6, 9) to enter Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for map transition
    pos = mgba.get_coordinates()
    print(f"Entered Mansion 1F West! Landing position: {pos}")
    
    # Check if we are indeed inside at (2, 7)
    if pos == {"x": 2, "y": 7}:
        # 1F West path: walk to (10, 7) then down to (10, 10) then left to (6, 10)
        steps_1f = [
            ("Right", {"x": 3, "y": 7}),
            ("Right", {"x": 4, "y": 7}),
            ("Right", {"x": 5, "y": 7}),
            ("Right", {"x": 6, "y": 7}),
            ("Right", {"x": 7, "y": 7}),
            ("Right", {"x": 8, "y": 7}),
            ("Right", {"x": 9, "y": 7}),
            ("Right", {"x": 10, "y": 7}),
            ("Down", {"x": 10, "y": 8}),
            ("Down", {"x": 10, "y": 9}),
            ("Down", {"x": 10, "y": 10}),
            ("Left", {"x": 9, "y": 10}),
            ("Left", {"x": 8, "y": 10}),
            ("Left", {"x": 7, "y": 10}),
            ("Left", {"x": 6, "y": 10}),
        ]
        
        for d, c in steps_1f:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            print("Reached (6, 10) on 1F West! Stepping LEFT onto stairs to warp UP to 2F West...")
            mgba.press_buttons(["Left"])
            time.sleep(1.5) # Wait for warp
            pos = mgba.get_coordinates()
            print(f"Warped UP to 2F West! Current coordinates: {pos}")
            
            # 2F West path: walk to (7, 11) and warp UP to 3F West
            # Landing on 2F West should be (5, 11).
            if pos == {"x": 5, "y": 11}:
                steps_2f = [
                    ("Right", {"x": 6, "y": 11}),
                    ("Right", {"x": 7, "y": 11}),
                ]
                for d, c in steps_2f:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    print("Reached (7, 11) on 2F West! Stepping UP onto stairs to warp UP to 3F West...")
                    mgba.press_buttons(["Up"])
                    time.sleep(1.5) # Wait for warp
                    pos = mgba.get_coordinates()
                    print(f"Warped UP to 3F West! Landing position: {pos}")
                else:
                    print("Failed to navigate 2F West.")
            else:
                print(f"Unexpected landing position on 2F West: {pos}")
        else:
            print("Failed to navigate 1F West.")
    else:
        print(f"Unexpected landing position inside Mansion: {pos}")
else:
    print("Failed to enter Mansion.")
