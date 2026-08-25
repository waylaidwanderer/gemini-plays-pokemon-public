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

# We are starting at (12, 11) on 2F East (State B)
# 1. Walk UP Column 12 to Row 3
steps_up_col12 = [
    ("Up", {"x": 12, "y": 10}),
    ("Up", {"x": 12, "y": 9}),
    ("Up", {"x": 12, "y": 8}),
    ("Up", {"x": 12, "y": 7}),
    ("Up", {"x": 12, "y": 6}),
    ("Up", {"x": 12, "y": 5}),
    ("Up", {"x": 12, "y": 4}),
    ("Up", {"x": 12, "y": 3}),
]

success = True
for d, c in steps_up_col12:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk RIGHT along Row 3 to Column 18
    print("Reached (12, 3)! Walking RIGHT along Row 3 to Column 18...")
    steps_right_row3 = [
        ("Right", {"x": 13, "y": 3}),
        ("Right", {"x": 14, "y": 3}),
        ("Right", {"x": 15, "y": 3}),
        ("Right", {"x": 16, "y": 3}),
        ("Right", {"x": 17, "y": 3}),
        ("Right", {"x": 18, "y": 3}),
    ]
    for d, c in steps_right_row3:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 3. Walk DOWN Column 18 to Row 11
    print("Reached (18, 3)! Walking DOWN Column 18 to Row 11...")
    steps_down_col18 = [
        ("Down", {"x": 18, "y": 4}),
        ("Down", {"x": 18, "y": 5}),
        ("Down", {"x": 18, "y": 6}),
        ("Down", {"x": 18, "y": 7}),
        ("Down", {"x": 18, "y": 8}),
        ("Down", {"x": 18, "y": 9}),
        ("Down", {"x": 18, "y": 10}),
        ("Down", {"x": 18, "y": 11}),
    ]
    for d, c in steps_down_col18:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 4. Walk LEFT along Row 11 to Column 15 (stairs)
    print("Reached (18, 11)! Walking LEFT along Row 11 to Column 15...")
    steps_left_row11 = [
        ("Left", {"x": 17, "y": 11}),
        ("Left", {"x": 16, "y": 11}),
        ("Left", {"x": 15, "y": 11}),
    ]
    for d, c in steps_left_row11:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 5. Step UP onto the stairs at (15, 11) to warp UP to 3F East
    print("Reached (15, 11) next to stairs! Walking UP onto stairs at (15, 11) to warp UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # wait for warp animation
    pos = mgba.get_coordinates()
    print(f"Warped UP to 3F East! Landing position: {pos}")
    
    # 6. On 3F East, walk RIGHT to Column 20
    steps_3f_east = [
        ("Right", {"x": 16, "y": 11}),
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
    ]
    for d, c in steps_3f_east:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        # 7. Walk UP Column 20 to Row 3
        print("Reached (20, 11)! Walking UP Column 20 to Row 3...")
        steps_up_col20 = [
            ("Up", {"x": 20, "y": 10}),
            ("Up", {"x": 20, "y": 9}),
            ("Up", {"x": 20, "y": 8}),
            ("Up", {"x": 20, "y": 7}),
            ("Up", {"x": 20, "y": 6}),
            ("Up", {"x": 20, "y": 5}),
            ("Up", {"x": 20, "y": 4}),
            ("Up", {"x": 20, "y": 3}),
        ]
        for d, c in steps_up_col20:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            # 8. Walk RIGHT along Row 3 to Column 26
            print("Reached (20, 3)! Walking RIGHT along Row 3 to Column 26...")
            steps_right_row3_3f = [
                ("Right", {"x": 21, "y": 3}),
                ("Right", {"x": 22, "y": 3}),
                ("Right", {"x": 23, "y": 3}),
                ("Right", {"x": 24, "y": 3}),
                ("Right", {"x": 25, "y": 3}),
                ("Right", {"x": 26, "y": 3}),
            ]
            for d, c in steps_right_row3_3f:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                # 9. Step DOWN/RIGHT onto Column 26 to fall through pit
                print("Reached (26, 3)! Stepping DOWN to trigger pitfall...")
                mgba.press_buttons(["Down"])
                time.sleep(2.0)
                pos = mgba.get_coordinates()
                print(f"Landed on 1F East inside fenced room! Position: {pos}")
                
                # 10. Walk UP to (26, 3), LEFT to (22, 3)
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
                    # 11. Step UP onto stairs at (22, 2) to warp DOWN to B1F East
                    print("Reached (22, 3) on 1F East! Stepping UP onto stairs to warp DOWN to B1F East...")
                    mgba.press_buttons(["Up"])
                    time.sleep(1.5)
                    pos = mgba.get_coordinates()
                    print(f"Warped DOWN to B1F East! Landing position: {pos}")
                    
                    # 12. Walk LEFT to (21, 3), DOWN to (21, 4), LEFT to (19, 4), DOWN to (19, 5)
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
                        print("Bypassed B1F East wall! Walking LEFT along Row 5 directly to B1F West...")
                        curr = mgba.get_coordinates()
                        while curr['x'] > 1:
                            if not walk_step("Left", {"x": curr['x'] - 1, "y": 5}):
                                success = False
                                break
                            curr = mgba.get_coordinates()
                            
                        if success:
                            print("Successfully reached (1, 5) on B1F West! Facing UP and retrieving Secret Key...")
                            mgba.press_buttons(["Up"])
                            time.sleep(0.3)
                            mgba.press_buttons(["A"])   # Opens "Obtained the SECRET KEY!"
                            time.sleep(1.5)
                            mgba.press_buttons(["A"])   # Dismiss obtain text
                            time.sleep(1.0)
                            pos = mgba.get_coordinates()
                            print(f"Secret Key retrieved successfully! Current position: {pos}")
                            
                            # 13. Use DIG to escape to Cinnabar Island!
                            print("Using DIG to escape...")
                            mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"]) # opens PKMN menu
                            for _ in range(5):
                                mgba.press_buttons(["Down", "sleep 150"])
                            mgba.press_buttons(["A", "sleep 300", "A"]) # selects TRUFFLE, then selects DIG
                            time.sleep(3.0) # wait for warp animation
                            print("Warped out! Final position:", mgba.get_coordinates())
                        else:
                            print("Failed to reach Secret Key on B1F West.")
                    else:
                        print("Failed to navigate B1F East.")
                else:
                    print("Failed to navigate 1F East fenced room.")
            else:
                print("Failed to reach (26, 3) on 3F East.")
        else:
            print("Failed to reach (20, 3) on 3F East.")
    else:
        print("Failed to navigate 3F East.")
else:
    print("Mansion key retrieve route failed.")
