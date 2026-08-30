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

# Starting at current (26, 23)
path = [
    # 1. Walk UP Column 26 to Row 16
    ("Up", 26, 22),
    ("Up", 26, 21),
    ("Up", 26, 20),
    ("Up", 26, 19),
    ("Up", 26, 18),
    ("Up", 26, 17),
    ("Up", 26, 16),
    # 2. Walk Left along Row 16 to Column 21
    ("Left", 25, 16),
    ("Left", 24, 16),
    ("Left", 23, 16),
    ("Left", 22, 16),
    ("Left", 21, 16),
    # 3. Walk DOWN Column 21 through open balcony gates (21, 17) to Row 18
    ("Down", 21, 17),
    ("Down", 21, 18),
    # 4. Walk Left to balcony drop warp at (19, 18)
    ("Left", 20, 18),
    ("Left", 19, 18)
]

print("Executing precise walk to balcony drop...")
for direction, tx, ty in path:
    if not move_strict(direction, tx, ty):
        break
