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
    # If we are in a battle, run away
    print("Dialogue/Battle detected! Attempting to clear...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 300"])
    # Navigate to RUN
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 600"])
    mgba.press_buttons(["B", "sleep 300"])

def safe_step(direction):
    old_pos = get_pos()
    new_pos = step(direction)
    if new_pos == old_pos:
        # Check if we got into a battle/dialogue
        time.sleep(0.5)
        if get_pos() != old_pos:
            run_away_or_battle()
            time.sleep(1.0)
            return step(direction)
        else:
            print("BLOCKED physically")
            return old_pos
    return new_pos

# 1. Walk to Row 13
print("Moving Down to Row 13...")
safe_step("Down")
safe_step("Down")

# 2. Walk to Column 1
print("Moving Left to Column 1...")
safe_step("Left")
safe_step("Left")
safe_step("Left")
safe_step("Left")

# 3. Walk to Row 11
print("Moving Up to Row 11...")
safe_step("Up")
safe_step("Up")

# 4. Turn Right toward Mewtwo statue at (2, 11)
print("Turning Right...")
mgba.press_buttons(["Right", "sleep 300"])

# 5. Interact with the switch
print("Interacting with the switch...")
mgba.press_buttons(["A", "sleep 500"])
mgba.take_screenshot()

# Press A to select YES to the switch, and clear text
print("Pressing A to confirm switch and clear dialogue...")
mgba.press_buttons(["A", "sleep 500"])
mgba.press_buttons(["A", "sleep 500"])
mgba.press_buttons(["A", "sleep 500"])
mgba.take_screenshot()

print("Final position and state check:", get_pos())
