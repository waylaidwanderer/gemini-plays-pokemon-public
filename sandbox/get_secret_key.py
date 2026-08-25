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

# 1. Walk from (5, 27) to (6, 10) and step Left onto (5, 10) to warp UP to 2F West
# Walk UP Column 5 from Row 27 to Row 11
for y in range(26, 10, -1):
    if not walk_step("Up", {"x": 5, "y": y}):
        break
        
# From (5, 11), walk Right to (6, 11), Up to (6, 10), Left onto (5, 10)
walk_step("Right", {"x": 6, "y": 11})
walk_step("Up", {"x": 6, "y": 10})

print("Stepping Left onto stairs at (5, 10) to warp UP to 2F West...")
mgba.press_buttons(["Left"])
time.sleep(1.5) # Wait for warp
pos = mgba.get_coordinates()
print(f"Warped UP to 2F West! Current position: {pos}")

# 2. On 2F West (State B)
# Landing coordinate is (5, 11). Walk Right to (7, 11) and Up onto stairs at (7, 10) to warp UP to 3F West
if pos == {"x": 5, "y": 11}:
    walk_step("Right", {"x": 6, "y": 11})
    walk_step("Right", {"x": 7, "y": 11})
    print("Stepping UP onto stairs at (7, 10) to warp UP to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for warp
    pos = mgba.get_coordinates()
    print(f"Warped UP to 3F West! Landing position: {pos}")
    
    # 3. On 3F West (State B)
    # Landing coordinate is (7, 11). Walk Left to (1, 11), UP Column 1 to Row 6 (1, 6), and Right to (11, 6)
    if pos == {"x": 7, "y": 11}:
        steps_3f_west = [
            ("Left", {"x": 6, "y": 11}),
            ("Left", {"x": 5, "y": 11}),
            ("Left", {"x": 4, "y": 11}),
            ("Left", {"x": 3, "y": 11}),
            ("Left", {"x": 2, "y": 11}),
            ("Left", {"x": 1, "y": 11}),
            ("Up", {"x": 1, "y": 10}),
            ("Up", {"x": 1, "y": 9}),   # Open gate in State B!
            ("Up", {"x": 1, "y": 8}),
            ("Up", {"x": 1, "y": 7}),
            ("Up", {"x": 1, "y": 6}),
            ("Right", {"x": 2, "y": 6}),
            ("Right", {"x": 3, "y": 6}),
            ("Right", {"x": 4, "y": 6}),
            ("Right", {"x": 5, "y": 6}),
            ("Right", {"x": 6, "y": 6}),
            ("Right", {"x": 7, "y": 6}),
            ("Right", {"x": 8, "y": 6}),
            ("Right", {"x": 9, "y": 6}),
            ("Right", {"x": 10, "y": 6}),
            ("Right", {"x": 11, "y": 6}), # Crossed horizontally to 3F East!
        ]
        
        success = True
        for d, c in steps_3f_west:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            # 4. On 3F East (State B)
            # Walk Right from (11, 6) to Column 20, Up to Row 3, Right to (26, 3) and step Down to drop
            steps_3f_east = [
                ("Right", {"x": 12, "y": 6}),
                ("Right", {"x": 13, "y": 6}),
                ("Right", {"x": 14, "y": 6}),
                ("Right", {"x": 15, "y": 6}),
                ("Right", {"x": 16, "y": 6}),
                ("Right", {"x": 17, "y": 6}),
                ("Right", {"x": 18, "y": 6}),
                ("Right", {"x": 19, "y": 6}),
                ("Right", {"x": 20, "y": 6}),
                ("Up", {"x": 20, "y": 5}),
                ("Up", {"x": 20, "y": 4}),
                ("Up", {"x": 20, "y": 3}),  # Open vertical passage!
                ("Right", {"x": 21, "y": 3}),
                ("Right", {"x": 22, "y": 3}),
                ("Right", {"x": 23, "y": 3}),
                ("Right", {"x": 24, "y": 3}),
                ("Right", {"x": 25, "y": 3}),
                ("Right", {"x": 26, "y": 3}),
            ]
            for d, c in steps_3f_east:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                print("Reached (26, 3) on 3F East! Stepping DOWN to trigger pitfall...")
                mgba.press_buttons(["Down"])
                time.sleep(2.0) # Wait for drop animation
                pos = mgba.get_coordinates()
                print(f"Landed on 1F East inside fenced room! Position: {pos}")
                
                # 5. On 1F East fenced room
                # Landing coordinate should be (26, 4). Walk UP to (26, 3), Left to (22, 3), Up onto stairs at (22, 2)
                steps_1f_east = [
                    ("Up", {"x": 26, "y": 3}),
                    ("Left", {"x": 25, "y": 3}),
                    ("Left", {"x": 24, "y": 3}),
                    ("Left", {"x": 23, "y": 3}),
                    ("Left", {"x": 22, "y": 3}),
                ]
                for d, c in steps_1f_east:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    print("Reached (22, 3) on 1F East! Stepping UP onto stairs to warp DOWN to B1F East...")
                    mgba.press_buttons(["Up"])
                    time.sleep(1.5) # Wait for warp
                    pos = mgba.get_coordinates()
                    print(f"Warped DOWN to B1F East! Landing position: {pos}")
                    
                    # 6. On B1F East (State B)
                    # Landing coordinate should be (22, 3). Walk Left to (21, 3), Down to (21, 4), Left to (19, 4), Down to (19, 5), Left to (1, 5)
                    if pos == {"x": 22, "y": 3}:
                        steps_b1f = [
                            ("Left", {"x": 21, "y": 3}),
                            ("Down", {"x": 21, "y": 4}),
                            ("Left", {"x": 20, "y": 4}),
                            ("Left", {"x": 19, "y": 4}),
                            ("Down", {"x": 19, "y": 5}),
                        ]
                        for d, c in steps_b1f:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            print("Successfully bypassed B1F East wall! Walking Left along Row 5 to the Secret Key...")
                            curr = mgba.get_coordinates()
                            while curr['x'] > 1:
                                if not walk_step("Left", {"x": curr['x'] - 1, "y": 5}):
                                    success = False
                                    break
                                curr = mgba.get_coordinates()
                                
                            if success:
                                print("Successfully reached (1, 5) on B1F West! Standing facing UP and retrieving the Secret Key...")
                                mgba.press_buttons(["Up"])
                                time.sleep(0.3)
                                mgba.press_buttons(["A"])   # Opens "Obtained the SECRET KEY!"
                                time.sleep(1.5)
                                mgba.press_buttons(["A"])   # Dismiss obtain text
                                time.sleep(1.0)
                                img_path = mgba.take_screenshot()
                                print(f"Secret Key retrieved successfully! Screenshot: {img_path}")
                                print("Current position:", mgba.get_coordinates())
                            else:
                                print("Failed to reach Secret Key on B1F West.")
                        else:
                            print("Failed to navigate B1F East.")
                    else:
                        print(f"Unexpected landing position on B1F East: {pos}")
                else:
                    print("Failed to navigate 1F East fenced room.")
            else:
                print("Failed to navigate 3F East.")
        else:
            print("Failed to navigate 3F West.")
    else:
         print(f"Unexpected landing position on 3F West: {pos}")
else:
    print("Failed to navigate 1F West.")
