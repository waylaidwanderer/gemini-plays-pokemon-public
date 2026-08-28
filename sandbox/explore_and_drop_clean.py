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

# Dismiss "Got away safely!" text first
print("Dismissing 'Got away safely!'...")
mgba.press_buttons(["B", "sleep 500"])

# --- 1. Navigate 3F East to Pitfall ---
# Start from (20, 4)
print("Moving Up to Row 3...")
safe_step("Up") # (20, 3)

# Walk Right along Row 3 to Column 25
print("Walking Right along Row 3 to Column 25...")
for _ in range(5):
    safe_step("Right") # (25, 3)

# Step Right onto the pitfall at (26, 3) to fall to 1F East (landing at 26, 4)
print("Stepping Right onto the pitfall...")
mgba.press_buttons(["Right"])
time.sleep(2.5) # Wait for drop transition
print("Current position after pitfall drop:", get_pos())
mgba.take_screenshot()

# --- 2. Warp Down to B1F East ---
# We should land at (26, 4) on 1F East.
# Let's walk to (21, 2) on 1F East:
# Walk Left to Column 22, Row 4:
print("Walking to B1F East stairs landing...")
for _ in range(4):
    safe_step("Left") # (22, 4)
safe_step("Up") # (22, 3)

# Step Up onto the stairs at (22, 2) to warp down to B1F East
print("Stepping Up onto B1F East stairs...")
mgba.press_buttons(["Up"])
time.sleep(2.5) # Wait for warp
print("Current position on B1F East:", get_pos())
mgba.take_screenshot()

# --- 3. Walk to B1F West and Retrieve Secret Key ---
# We should land at (22, 2) on B1F East.
# Let's walk to B1F West at (1, 5):
# B1F East is open along Row 5 in State B.
# Walk Down to Row 5, then Left all the way to Column 1
print("Walking to B1F West along Row 5...")
safe_step("Down")
safe_step("Down")
safe_step("Down")
for _ in range(21):
    safe_step("Left")

# Face Up toward the Secret Key at (1, 4)
print("Facing Up toward the Secret Key...")
mgba.press_buttons(["Up", "sleep 300"])

# Interact and press A to retrieve the Secret Key
print("Retrieving Secret Key...")
mgba.press_buttons(["A", "sleep 500"])
mgba.press_buttons(["A", "sleep 500"])
mgba.take_screenshot()

print("Mansion key retrieval completed!")
