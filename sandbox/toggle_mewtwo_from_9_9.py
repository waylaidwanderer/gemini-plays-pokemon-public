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

# 1. Walk Left to Column 5 Row 9
print("Moving Left to Column 5...")
safe_step("Left")
safe_step("Left")
safe_step("Left")
safe_step("Left")

# 2. Walk Down to Row 12
print("Moving Down to Row 12...")
safe_step("Down")
safe_step("Down")
safe_step("Down")

# 3. Walk Left to Column 2
print("Moving Left to Column 2...")
safe_step("Left")
safe_step("Left")
safe_step("Left")

# 4. Turn UP toward the Mewtwo statue switch at (2, 11)
print("Turning UP...")
mgba.press_buttons(["Up", "sleep 300"])

# 5. Interact with the switch
print("Interacting with the switch...")
mgba.press_buttons(["A", "sleep 500"])
mgba.take_screenshot()

# Press A to select YES to the switch, and clear text
print("Confirming and clearing text...")
mgba.press_buttons(["A", "sleep 500"]) # select YES
mgba.press_buttons(["A", "sleep 500"]) # clear "Who wouldn't?"
mgba.press_buttons(["A", "sleep 500"]) # clear "Click!"
mgba.take_screenshot()

print("Current position:", get_pos())
