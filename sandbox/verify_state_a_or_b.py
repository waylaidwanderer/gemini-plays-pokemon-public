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

# Start at current (19, 16)
path = [
    # 1. Walk Right along Row 16 to Column 25
    ("Right", 20, 16),
    ("Right", 21, 16),
    ("Right", 22, 16),
    ("Right", 23, 16),
    ("Right", 24, 16),
    ("Right", 25, 16),
    # 2. Walk UP Column 25 to Row 12 (gate at (25, 13) is open)
    ("Up", 25, 15),
    ("Up", 25, 14),
    ("Up", 25, 13),
    ("Up", 25, 12),
    # 3. Walk Right to Column 26
    ("Right", 26, 12),
    # 4. Walk UP Column 26 to Row 2
    ("Up", 26, 11),
    ("Up", 26, 10),
    ("Up", 26, 9),
    ("Up", 26, 8),
    ("Up", 26, 7),
    ("Up", 26, 6),
    ("Up", 26, 5),
    ("Up", 26, 4),
    ("Up", 26, 3),
    ("Up", 26, 2),
    # 5. Walk Left to Column 22 on Row 2
    ("Left", 25, 2),
    ("Left", 24, 2),
    ("Left", 23, 2),
    ("Left", 22, 2)
]

print("Executing precise path to verification gate at (21, 2)...")
arrived = True
for direction, tx, ty in path:
    if not move_strict(direction, tx, ty):
        arrived = False
        break

if arrived:
    print("Arrived at (22, 2). Testing step Left to (21, 2)...")
    if move_strict("Left", 21, 2):
        print("VERDICT: THE MANSION IS IN STATE A (Gate at (21,2) is open!)")
        # Step back to (22, 2) to keep path clean
        move_strict("Right", 22, 2)
    else:
        print("VERDICT: THE MANSION IS IN STATE B (Gate at (21,2) is closed!)")
else:
    print("Failed to reach verification gate.")
