import mgba
import time

def move_strict(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Stepping {direction} from {pos_before} to ({target_x}, {target_y})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        print(f"Arrived at ({target_x}, {target_y})")
        return True
    else:
        print(f"BLOCKED or Battle encountered! Position is {pos_after}. Exiting script.")
        return False

# Starting at current (22, 1) on 3F East (Mansion is in State B)
path_to_switch = [
    # Walk Left along Row 1 to Column 4
    ("Left", 21, 1),
    ("Left", 20, 1),
    ("Left", 19, 1),
    ("Left", 18, 1),
    ("Left", 17, 1),
    ("Left", 16, 1),
    ("Left", 15, 1),
    ("Left", 14, 1),
    ("Left", 13, 1),
    ("Left", 12, 1),
    ("Left", 11, 1),
    ("Left", 10, 1),
    ("Left", 9, 1),
    ("Left", 8, 1),
    ("Left", 7, 1),
    ("Left", 6, 1),
    ("Left", 5, 1),
    ("Left", 4, 1),
    # Walk DOWN Column 4 to Row 5
    ("Down", 4, 2),
    ("Down", 4, 3),
    ("Down", 4, 4),
    ("Down", 4, 5),
    # Walk Left to Column 2 Row 6 via (3,5) -> (3,6) -> (2,6)
    ("Left", 3, 5),
    ("Down", 3, 6),
    ("Left", 2, 6)
]

print("Executing path to Mewtwo Switch via Row 1 detour...")
arrived = True
for direction, tx, ty in path_to_switch:
    if not move_strict(direction, tx, ty):
        arrived = False
        break

if arrived:
    # Face UP and toggle switch
    print("Arrived at (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling Mewtwo Switch (4-press sequence)...")
    for i in range(1, 5):
        print(f"A-press {i}...")
        mgba.press_buttons(["A"])
        time.sleep(1.8)
        
    print("Switch toggled! Walking back to verification point (22, 2)...")
    
    path_back = [
        # Walk Right to Column 3 Row 6
        ("Right", 3, 6),
        # Walk UP Column 3 to Row 5 (detours around closed gate at 4,6 in State A)
        ("Up", 3, 5),
        # Walk Right to Column 4
        ("Right", 4, 5),
        # Walk UP Column 4 to Row 1
        ("Up", 4, 4),
        ("Up", 4, 3),
        ("Up", 4, 2),
        ("Up", 4, 1),
        # Walk Right along Row 1 to Column 22
        ("Right", 5, 1),
        ("Right", 6, 1),
        ("Right", 7, 1),
        ("Right", 8, 1),
        ("Right", 9, 1),
        ("Right", 10, 1),
        ("Right", 11, 1),
        ("Right", 12, 1),
        ("Right", 13, 1),
        ("Right", 14, 1),
        ("Right", 15, 1),
        ("Right", 16, 1),
        ("Right", 17, 1),
        ("Right", 18, 1),
        ("Right", 19, 1),
        ("Right", 20, 1),
        ("Right", 21, 1),
        ("Right", 22, 1),
        # Walk DOWN to Row 2
        ("Down", 22, 2)
    ]
    
    back_arrived = True
    for direction, tx, ty in path_back:
        if not move_strict(direction, tx, ty):
            back_arrived = False
            break
            
    if back_arrived:
        print("Arrived at (22, 2). Testing if gate at (21, 2) is open...")
        if move_strict("Left", 21, 2):
            print("VERDICT: THE GATE AT (21, 2) IS NOW OPEN! State A is active!")
            # Step back to (22, 2) to keep state clean
            move_strict("Right", 22, 2)
        else:
            print("VERDICT: THE GATE AT (21, 2) IS CLOSED! State B is active!")
            
else:
    print("Failed to reach switch.")
