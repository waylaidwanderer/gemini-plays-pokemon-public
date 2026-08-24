import mgba
import time
import os

# Clean up obsolete workspace files
obsolete_files = [
    "walk_to_statue_2f.py",
    "test_col9_up.py",
    "go_to_2f_east_switch.py",
    "mansion_2f_traverse.py",
    "enter_mansion_clean.py"
]
for f in obsolete_files:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted obsolete file: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

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

# Starting at (5, 11) on 3F West of Pokemon Mansion in State A
# 1. Walk the bypass around the NPC to reach the switch at (2, 12)
steps_to_switch = [
    ("Down", {"x": 5, "y": 12}),
    ("Left", {"x": 4, "y": 12}),
    ("Down", {"x": 4, "y": 13}),
    ("Left", {"x": 3, "y": 13}),
    ("Left", {"x": 2, "y": 13}),
    ("Up", {"x": 2, "y": 12}),
]

success = True
for direction, coords in steps_to_switch:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (2, 12) on 3F West successfully! Toggling switch to State B...")
    # Stand at (2, 12) facing UP towards statue at (2, 11) and toggle
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])   # Opens "A secret switch! Press it?"
    time.sleep(1.0)             # Wait for text scroll
    mgba.press_buttons(["A"])   # Selects YES and toggles
    time.sleep(1.0)             # Wait for toggle
    mgba.press_buttons(["B"])   # Safely dismisses text box
    time.sleep(0.5)
    print("Switch toggled to State B!")
    
    # 2. Walk back to (7, 10) on 3F West and warp down
    steps_3f_back_to_stairs = [
        ("Down", {"x": 2, "y": 13}),
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Right", {"x": 6, "y": 13}),
        ("Right", {"x": 7, "y": 13}),
        ("Up", {"x": 7, "y": 12}),
        ("Up", {"x": 7, "y": 11}),
    ]
    for direction, coords in steps_3f_back_to_stairs:
        if not walk_step(direction, coords):
            success = False
            break
            
    if success:
        print("Reached (7, 11) on 3F West! Stepping UP onto stairs at (7, 10) to warp DOWN...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0) # Wait for warp
        pos = mgba.get_coordinates()
        print(f"Warped down to 2F West! Landing position: {pos}")
        
        # 3. On 2F West (State B)
        # Landing coordinate is (7, 11).
        steps_2f_west = [
            ("Left", {"x": 6, "y": 11}),
            ("Up", {"x": 6, "y": 10}),
            ("Up", {"x": 6, "y": 9}),  # OPEN in State B!
            ("Up", {"x": 6, "y": 8}),
            ("Up", {"x": 6, "y": 7}),
            ("Up", {"x": 6, "y": 6}),
            ("Up", {"x": 6, "y": 5}),
            ("Up", {"x": 6, "y": 4}),
            ("Up", {"x": 6, "y": 3}),
            # Walk RIGHT along Row 3 to Column 18
            ("Right", {"x": 7, "y": 3}),
            ("Right", {"x": 8, "y": 3}),
            ("Right", {"x": 9, "y": 3}),
            ("Right", {"x": 10, "y": 3}),
            ("Right", {"x": 11, "y": 3}),
            ("Right", {"x": 12, "y": 3}),
            ("Right", {"x": 13, "y": 3}),
            ("Right", {"x": 14, "y": 3}),
            ("Right", {"x": 15, "y": 3}),
            ("Right", {"x": 16, "y": 3}),
            ("Right", {"x": 17, "y": 3}),
            ("Right", {"x": 18, "y": 3}),
            # Walk DOWN Column 18 to Row 10
            ("Down", {"x": 18, "y": 4}),
            ("Down", {"x": 18, "y": 5}),
            ("Down", {"x": 18, "y": 6}),
            ("Down", {"x": 18, "y": 7}),
            ("Down", {"x": 18, "y": 8}),
            ("Down", {"x": 18, "y": 9}),
            ("Down", {"x": 18, "y": 10}),
            # Walk LEFT along Row 10 to Column 15
            ("Left", {"x": 17, "y": 10}),
            ("Left", {"x": 16, "y": 10}),
            ("Left", {"x": 15, "y": 10}),
        ]
        for direction, coords in steps_2f_west:
            if not walk_step(direction, coords):
                success = False
                break
                
        if success:
            print("Reached (15, 10) on 2F East! Stepping DOWN onto stairs at (15, 11) to warp up...")
            mgba.press_buttons(["Down"])
            time.sleep(1.0) # Wait for warp
            pos = mgba.get_coordinates()
            print(f"Warped up to 3F East! Landing position: {pos}")
            
            # 4. On 3F East (State B)
            # Landing coordinate should be (15, 12).
            steps_3f_east = [
                ("Up", {"x": 15, "y": 11}),
                ("Up", {"x": 15, "y": 10}),
                ("Up", {"x": 15, "y": 9}),
                ("Up", {"x": 15, "y": 8}),
                ("Up", {"x": 15, "y": 7}),
                ("Up", {"x": 15, "y": 6}),
                # Walk Right along Row 6 to (19, 6)
                ("Right", {"x": 16, "y": 6}),
                ("Right", {"x": 17, "y": 6}),
                ("Right", {"x": 18, "y": 6}),
                ("Right", {"x": 19, "y": 6}),
                # Up Column 19 to Row 3
                ("Up", {"x": 19, "y": 5}),
                ("Up", {"x": 19, "y": 4}),
                ("Up", {"x": 19, "y": 3}),
                # Right along Row 3 to (26, 3)
                ("Right", {"x": 20, "y": 3}),
                ("Right", {"x": 21, "y": 3}),
                ("Right", {"x": 22, "y": 3}),
                ("Right", {"x": 23, "y": 3}),
                ("Right", {"x": 24, "y": 3}),
                ("Right", {"x": 25, "y": 3}),
                ("Right", {"x": 26, "y": 3}),
            ]
            for direction, coords in steps_3f_east:
                if not walk_step(direction, coords):
                    success = False
                    break
                    
            if success:
                print("Reached (26, 3) on 3F East! Stepping DOWN to trigger pitfall...")
                mgba.press_buttons(["Down"])
                time.sleep(1.0) # Wait for drop animation
                pos = mgba.get_coordinates()
                print(f"Landed on 1F East inside fenced room at: {pos}")
                
                # Walk to (21, 2) and then step Right to (22, 2)
                print("Routing to 1F East stairs (22, 2)...")
                curr = mgba.get_coordinates()
                while curr['y'] > 2:
                    if not walk_step("Up", {"x": curr['x'], "y": curr['y'] - 1}):
                        break
                    curr = mgba.get_coordinates()
                while curr['x'] > 21:
                    if not walk_step("Left", {"x": curr['x'] - 1, "y": curr['y']}):
                        break
                    curr = mgba.get_coordinates()
                # Step Right onto (22, 2) to warp down
                print("Stepping onto stairs at (22, 2) to warp to B1F East...")
                mgba.press_buttons(["Right"])
                time.sleep(1.0) # Wait for warp animation
                
                curr = mgba.get_coordinates()
                print(f"Warped to B1F East! Current coordinates: {curr}")
                
                # 5. Route on B1F East:
                steps_b1f = [
                    ("Left", {"x": 21, "y": 3}),
                    ("Down", {"x": 21, "y": 4}),
                    ("Left", {"x": 20, "y": 4}),
                    ("Left", {"x": 19, "y": 4}),
                    ("Down", {"x": 19, "y": 5}),
                ]
                for d, c in steps_b1f:
                    walk_step(d, c)
                    
                # Now walk Left all the way to (1, 5) on Row 5
                curr = mgba.get_coordinates()
                print("Walking Left on B1F Row 5 to the Secret Key room...")
                while curr['x'] > 1:
                    if not walk_step("Left", {"x": curr['x'] - 1, "y": 5}):
                        break
                    curr = mgba.get_coordinates()
                    
                # Stand at (1, 5) facing UP and retrieve the Secret Key
                curr = mgba.get_coordinates()
                if curr == {"x": 1, "y": 5}:
                    print("Successfully reached (1, 5)! Facing UP and picking up the Secret Key...")
                    mgba.press_buttons(["Up"])
                    time.sleep(0.3)
                    mgba.press_buttons(["A"])
                    time.sleep(1.5)
                    # Clear dialog
                    mgba.press_buttons(["A"])
                    time.sleep(1.0)
                    img_path = mgba.take_screenshot()
                    print(f"Secret Key retrieved! Screenshot: {img_path}")
                else:
                    print(f"Failed to reach (1, 5) on B1F. Current position: {curr}")
            else:
                print("Failed to navigate 3F East.")
        else:
            print("Failed to navigate 2F West.")
    else:
        print("Failed to warp down to 2F West.")
else:
    print("Failed to navigate 3F West.")
