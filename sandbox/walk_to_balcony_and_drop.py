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

# Starting at current (26, 19)
path = [
    # 1. Walk Left to Column 25 on Row 19
    ("Left", 25, 19),
    # 2. Walk UP Column 25 to Row 16
    ("Up", 25, 18),
    ("Up", 25, 17),
    ("Up", 25, 16),
    # 3. Walk Left along Row 16 to Column 21
    ("Left", 24, 16),
    ("Left", 23, 16),
    ("Left", 22, 16),
    ("Left", 21, 16),
    # 4. Walk DOWN Column 21 through open balcony gates (21, 17) to Row 18
    ("Down", 21, 17),
    ("Down", 21, 18),
    # 5. Walk Left to balcony drop warp at (19, 18)
    ("Left", 20, 18),
    ("Left", 19, 18)
]

print("Executing precise walk from (26, 19) to balcony drop...")
for direction, tx, ty in path:
    if not move_strict(direction, tx, ty):
        break
