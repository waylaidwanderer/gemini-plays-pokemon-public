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

# Starting at current (21, 3) on 3F East (Mansion is in State B)
path_to_switch = [
    # Continue Left on Row 3
    ("Left", 20, 3),
    ("Left", 19, 3),
    ("Left", 18, 3),
    ("Left", 17, 3),
    ("Left", 16, 3),
    ("Left", 15, 3),
    ("Left", 14, 3),
    ("Left", 13, 3),
    ("Left", 12, 3),
    ("Left", 11, 3),
    ("Left", 10, 3),
    # Bypasses Column 9 partition wall using Row 2 detour
    ("Up", 10, 2),
    ("Left", 9, 2),
    ("Left", 8, 2),
    ("Down", 8, 3),
    # Continue Left on Row 3
    ("Left", 7, 3),
    ("Left", 6, 3),
    ("Left", 5, 3),
    ("Left", 4, 3),
    # Walk DOWN Column 4 to Row 6
    ("Down", 4, 4),
    ("Down", 4, 5),
    ("Down", 4, 6),
    # Walk Left to Column 2 Row 6
    ("Left", 3, 6),
    ("Left", 2, 6)
]

print("Executing precise path to Mewtwo Switch at (2, 5)...")
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
        
    print("Switch toggled to State A! Walking back to balcony drop...")
    
    path_back = [
        # Walk Right to Column 3 Row 6
        ("Right", 3, 6),
        # Walk UP Column 3 to Row 5 (detours around closed gate at 4,6 in State A)
        ("Up", 3, 5),
        # Walk Right to Column 4
        ("Right", 4, 5),
        # Walk UP Column 4 to Row 3
        ("Up", 4, 4),
        ("Up", 4, 3),
        # Walk Right along Row 3 to Column 8 (using Row 2 detour to cross Column 9 wall)
        ("Right", 5, 3),
        ("Right", 6, 3),
        ("Right", 7, 3),
        ("Right", 8, 3),
        # Walk UP to Row 2
        ("Up", 8, 2),
        # Walk Right across Column 9
        ("Right", 9, 2),
        ("Right", 10, 2),
        # Walk DOWN to Row 3
        ("Down", 10, 3),
        # Continue Right to Column 25
        ("Right", 11, 3),
        ("Right", 12, 3),
        ("Right", 13, 3),
        ("Right", 14, 3),
        ("Right", 15, 3),
        ("Right", 16, 3),
        ("Right", 17, 3),
        ("Right", 18, 3),
        ("Right", 19, 3),
        ("Right", 20, 3),
        ("Right", 21, 3),
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        # Walk DOWN Column 25 to Row 16
        ("Down", 25, 4),
        ("Down", 25, 5),
        ("Down", 25, 6),
        ("Down", 25, 7),
        ("Down", 25, 8),
        ("Down", 25, 9),
        ("Down", 25, 10),
        ("Down", 25, 11),
        ("Down", 25, 12),
        ("Down", 25, 13), # Gate is open in State A
        ("Down", 25, 14),
        ("Down", 25, 15),
        ("Down", 25, 16),
        # Walk Left along Row 16 to Column 21
        ("Left", 24, 16),
        ("Left", 23, 16),
        ("Left", 22, 16),
        ("Left", 21, 16),
        # Walk DOWN Column 21 through open balcony gates (21, 17) to Row 18
        ("Down", 21, 17),
        ("Down", 21, 18),
        # Walk Left to balcony drop warp at (19, 18)
        ("Left", 20, 18),
        ("Left", 19, 18)
    ]
    
    for direction, tx, ty in path_back:
        if not move_strict(direction, tx, ty):
            break
            
else:
    print("Failed to reach switch.")
