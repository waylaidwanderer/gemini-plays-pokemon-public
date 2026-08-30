import mgba
import time

def step_strict(direction, target_x, target_y):
    for attempt in range(2):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
            print(f"WARPED! From {pos_before} to {pos_after}")
            return "WARPED"
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            return "SUCCESS"
        time.sleep(0.1)
    return "BLOCKED"

def flee_battle():
    print("Clearing encounter text...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)

    print("Clearing player summon text...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)

    print("Navigating menu to RUN...")
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A"])
    time.sleep(2.0)

    print("Clearing escape text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Fled battle.")

# 1. Flee from the wild battle
flee_battle()

# 2. Test the warp at (22, 1)
print("Testing warp at (22, 1) from different directions...")
# We are currently at (22, 2). Let's step UP to (22, 1)
step_strict("Up", 22, 1)
pos = mgba.get_coordinates()
print(f"Standing at: {pos}")

# Try pressing Up from (22, 1)
print("Trying UP from (22, 1)...")
mgba.press_buttons(["Up"])
time.sleep(1.0)
print(f"Pos after Up: {mgba.get_coordinates()}")

# If still at (22, 1), step down and try to walk Left/Right onto (22, 1)?
# But (21, 1) and (23, 1) are walls, so we can only walk into (22, 1) from (22, 2).
# Let's try pressing Left from (22, 1) or Right from (22, 1)
print("Trying Left from (22, 1)...")
mgba.press_buttons(["Left"])
time.sleep(1.0)
print(f"Pos after Left: {mgba.get_coordinates()}")

print("Trying Right from (22, 1)...")
mgba.press_buttons(["Right"])
time.sleep(1.0)
print(f"Pos after Right: {mgba.get_coordinates()}")

