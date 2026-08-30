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

# Starting at current (6, 1) on 3F East (Mansion is in State A)
path = [
    # 1. Walk Right along Row 1 to Column 26
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
    ("Right", 23, 1),
    ("Right", 24, 1),
    ("Right", 25, 1),
    ("Right", 26, 1),
    # 2. Walk DOWN Column 26 to Row 12 (bypasses horizontal wall at 25,4)
    ("Down", 26, 2),
    ("Down", 26, 3),
    ("Down", 26, 4),
    ("Down", 26, 5),
    ("Down", 26, 6),
    ("Down", 26, 7),
    ("Down", 26, 8),
    ("Down", 26, 9),
    ("Down", 26, 10),
    ("Down", 26, 11),
    ("Down", 26, 12),
    # 3. Walk Left to Column 25
    ("Left", 25, 12),
    # 4. Walk DOWN Column 25 to Row 16 (gate at 25,13 is open in State A)
    ("Down", 25, 13),
    ("Down", 25, 14),
    ("Down", 25, 15),
    ("Down", 25, 16),
    # 5. Walk Left along Row 16 to Column 21
    ("Left", 24, 16),
    ("Left", 23, 16),
    ("Left", 22, 16),
    ("Left", 21, 16),
    # 6. Walk DOWN Column 21 through open balcony gates (21, 17) to Row 18
    ("Down", 21, 17),
    ("Down", 21, 18),
    # 7. Walk Left to balcony drop warp at (19, 18)
    ("Left", 20, 18),
    ("Left", 19, 18)
]

print("Executing precise detour walk to balcony drop in State A...")
for direction, tx, ty in path:
    if not move_strict(direction, tx, ty):
        break
