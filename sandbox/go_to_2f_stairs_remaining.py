import mgba
import time

# Dismiss "Got away safely!"
print("Dismissing 'Got away safely!'...")
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
    ("Right", 12, 5),
    ("Right", 13, 5),
    ("Right", 14, 5),
    ("Right", 15, 5),
    ("Right", 16, 5),
    ("Right", 17, 5),
    ("Right", 18, 5),
    ("Up", 18, 4),
    ("Up", 18, 3),
]

success = True
for direction, tx, ty in path:
    if not walk_step(direction, tx, ty):
        success = False
        break

if success:
    print("At (18, 3)! Stepping Up to stairs warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    print("Warp complete! New Position:", mgba.get_coordinates())

mgba.take_screenshot()
