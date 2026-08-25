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

# Starting at (12, 10) on 2F West (State B)
# 1. Walk LEFT along Row 10 to Column 6
steps_to_col6 = [
    ("Left", {"x": 11, "y": 10}),
    ("Left", {"x": 10, "y": 10}),
    ("Left", {"x": 9, "y": 10}),
    ("Left", {"x": 8, "y": 10}),
    ("Left", {"x": 7, "y": 10}),
    ("Left", {"x": 6, "y": 10}),
]

success = True
for d, c in steps_to_col6:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk UP Column 6 to Row 3
    print("Reached (6, 10)! Walking UP Column 6 to Row 3...")
    steps_up_col6 = [
        ("Up", {"x": 6, "y": 9}),
        ("Up", {"x": 6, "y": 8}),
        ("Up", {"x": 6, "y": 7}),
        ("Up", {"x": 6, "y": 6}),
        ("Up", {"x": 6, "y": 5}),
        ("Up", {"x": 6, "y": 4}),
        ("Up", {"x": 6, "y": 3}),
    ]
    for d, c in steps_up_col6:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 3. Walk RIGHT along Row 3 to Column 18
    print("Reached (6, 3)! Walking RIGHT along Row 3 to Column 18...")
    curr = mgba.get_coordinates()
    while curr['x'] < 18:
        if not walk_step("Right", {"x": curr['x'] + 1, "y": 3}):
            success = False
            break
        curr = mgba.get_coordinates()

if success:
    # 4. Walk DOWN Column 18 to Row 10
    print("Reached (18, 3)! Walking DOWN Column 18 to Row 10...")
    curr = mgba.get_coordinates()
    while curr['y'] < 10:
        if not walk_step("Down", {"x": 18, "y": curr['y'] + 1}):
            success = False
            break
        curr = mgba.get_coordinates()

if success:
    # 5. Walk LEFT along Row 10 to Column 15
    print("Reached (18, 10)! Walking LEFT along Row 10 to Column 15...")
    curr = mgba.get_coordinates()
    while curr['x'] > 15:
        if not walk_step("Left", {"x": curr['x'] - 1, "y": 10}):
            success = False
            break
        curr = mgba.get_coordinates()

if success:
    # 6. Step DOWN onto the stairs at (15, 11) to warp UP to 3F East
    print("Reached (15, 10)! Standing next to stairs. Walking DOWN onto stairs at (15, 11)...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"Warped UP to 3F East! Landing position: {pos}")
    
    # 7. On 3F East (State B)
    # Walk Right from (15, 11) to Column 20, Up to Row 3, Right to (26, 3) and step Down to drop
    steps_3f_east = [
        ("Right", {"x": 16, "y": 11}),
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
        ("Up", {"x": 20, "y": 10}),
        ("Up", {"x": 20, "y": 9}),
        ("Up", {"x": 20, "y": 8}),
        ("Up", {"x": 20, "y": 7}),
        ("Up", {"x": 20, "y": 6}),
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
        
        # 8. On 1F East fenced room
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
            
            # 9. On B1F East (State B)
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
                        pos = mgba.get_coordinates()
                        print(f"Secret Key retrieved successfully! Current position: {pos}")
                        
                        # 10. Use DIG to escape to Cinnabar Island!
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
                print(f"Unexpected landing position on B1F East: {pos}")
        else:
            print("Failed to navigate 1F East fenced room.")
    else:
        print("Failed to navigate 3F East.")
else:
    print("Master bypass route failed or got blocked.")

