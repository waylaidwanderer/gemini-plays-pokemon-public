import mgba
import time

# 1. Dismiss "Got away safely!"
print("Dismissing text box...")
mgba.press_buttons(["A"])
time.sleep(1.0) # Wait for overworld to load

def walk_step(direction, target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Standing at {pos}. Pressing {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    print(f"Now at {new_pos}. Target was ({target_x}, {target_y})")
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        return True
    else:
        print("Failed to reach target! Could be a battle or obstacle.")
        return False

path = [
    # Walk Right to (11, 11)
    ("Right", 10, 11),
    ("Right", 11, 11),
    # Walk Up to (11, 5)
    ("Up", 11, 10),
    ("Up", 11, 9),
    ("Up", 11, 8),
    ("Up", 11, 7),
    ("Up", 11, 6),
    ("Up", 11, 5),
    # Walk Right to (18, 5)
    ("Right", 12, 5),
    ("Right", 13, 5),
    ("Right", 14, 5),
    ("Right", 15, 5), # Gate (15, 5) is OPEN in State A!
    ("Right", 16, 5),
    ("Right", 17, 5),
    ("Right", 18, 5),
    # Walk Up to (18, 3)
    ("Up", 18, 4),
    ("Up", 18, 3),
]

success = True
for direction, tx, ty in path:
    if not walk_step(direction, tx, ty):
        success = False
        break

if success:
    print("At (18, 3) on 2F! Stepping Up to stairs warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    print("Warp complete! Position on 3F:", mgba.get_coordinates())

mgba.take_screenshot()
