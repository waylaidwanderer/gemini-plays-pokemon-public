import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    print(f"New position: {new_pos}")
    return new_pos

def run_away_or_battle():
    print("Dialogue/Battle detected! Clearing...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 600"])
    mgba.press_buttons(["B", "sleep 300"])

def safe_step(direction):
    old_pos = get_pos()
    new_pos = step(direction)
    if new_pos == old_pos:
        time.sleep(0.5)
        if get_pos() != old_pos:
            run_away_or_battle()
            time.sleep(1.0)
            return step(direction)
        else:
            print("BLOCKED physically")
            return old_pos
    return new_pos

# --- 1. Navigate from (4, 11) to Row 9 ---
print("Stepping to Row 9...")
safe_step("Right") # (5, 11)
safe_step("Up")    # (5, 10)
safe_step("Up")    # (5, 9)

# --- 2. Walk Right along Row 9 to Column 11 ---
print("Walking Right to Column 11...")
for _ in range(6):
    safe_step("Right")

# --- 3. Walk Up Column 11 to Row 6 ---
print("Walking Up to Row 6...")
safe_step("Up") # (11, 8)
safe_step("Up") # (11, 7)
safe_step("Up") # (11, 6)

# --- 4. Walk Right to 3F East ---
print("Crossing to 3F East...")
for _ in range(5):
    safe_step("Right")

mgba.take_screenshot()
print("Reached 3F East! Final position:", get_pos())
