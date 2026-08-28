import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def run_away_or_battle():
    print("Dialogue/Battle detected! Clearing...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 600"])
    mgba.press_buttons(["B", "sleep 300"])

def step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    print(f"New position: {new_pos}")
    return new_pos

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

# --- 1. Navigate 3F West to 3F East Pitfall ---
# Start from (4, 10)
print("Navigating to Row 9...")
safe_step("Right")
safe_step("Up")

# Walk Right along Row 9 to Column 11
print("Walking Right to Column 11...")
for _ in range(6):
    safe_step("Right")

# Walk Up Column 11 to Row 6
print("Walking Up to Row 6...")
safe_step("Up")
safe_step("Up")
safe_step("Up")

# Walk Right along Row 6 to Column 21
print("Walking Right to Column 21...")
for _ in range(10):
    safe_step("Right")

# Walk Left to Column 19
print("Walking Left to Column 19...")
safe_step("Left")
safe_step("Left")

# Walk Up Column 19 to Row 3
print("Walking Up to Row 3...")
safe_step("Up")
safe_step("Up")
safe_step("Up")

# Walk Right along Row 3 to Column 25
print("Walking Right to Column 25...")
for _ in range(6):
    safe_step("Right")

# Step Right onto the pitfall at (26, 3) to fall to 1F East (landing at 26, 4)
print("Stepping Right onto the pitfall...")
mgba.press_buttons(["Right"])
time.sleep(2.5) # Wait for drop transition
print("Current position after pitfall drop:", get_pos())
mgba.take_screenshot()

# --- 2. Warp Down to B1F East ---
# We should land at (26, 4) on 1F East.
# Let's walk to (21, 2) on 1F East:
# Left to Column 21, Up to Row 2
print("Walking to B1F East stairs...")
for _ in range(5):
    safe_step("Left")
safe_step("Up")
safe_step("Up")

# Step Right onto the stairs at (22, 2) to warp down to B1F East
print("Stepping Right onto B1F East stairs...")
mgba.press_buttons(["Right"])
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
