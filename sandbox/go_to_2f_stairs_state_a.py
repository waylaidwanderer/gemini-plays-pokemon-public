import mgba
import time

# 1. Dismiss "Who wouldn't?" text
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
    ("Right", 3, 12),
    ("Up", 3, 11),
    ("Right", 4, 11),
    ("Right", 5, 11),
    ("Right", 6, 11),
    ("Right", 7, 11),
]

success = True
for direction, tx, ty in path:
    if not walk_step(direction, tx, ty):
        success = False
        break

if success:
    print("At (7, 11)! Stepping Up to stairs warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    print("Warp complete! New Position:", mgba.get_coordinates())

mgba.take_screenshot()
