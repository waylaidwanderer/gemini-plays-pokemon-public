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

# --- Step 1: Walk to Column 19 Row 6 ---
print("Walking to (19, 6)...")
safe_step("Right")
safe_step("Right")
safe_step("Right")

# --- Step 2: Walk Up to Row 4 ---
print("Walking UP to Row 4...")
safe_step("Up")
safe_step("Up")

# --- Step 3: Walk Right to Column 21 ---
print("Walking Right to Column 21...")
safe_step("Right")
safe_step("Right")

# --- Step 4: Walk Up to Row 2 ---
print("Walking UP to Row 2...")
safe_step("Up")
safe_step("Up")

# --- Step 5: Walk Right to Column 25 ---
print("Walking Right to Column 25...")
safe_step("Right")
safe_step("Right")
safe_step("Right")
safe_step("Right")

# --- Step 6: Walk Down to Row 3 ---
print("Walking Down to Row 3...")
safe_step("Down")

# --- Step 7: Step Right onto Pitfall at (26, 3) to Fall ---
print("Stepping Right onto Pitfall at (26, 3)...")
mgba.press_buttons(["Right"])
time.sleep(2.5) # Wait for drop transition
print("Current position after drop:", get_pos())
mgba.take_screenshot()

# --- Step 8: Walk to B1F East Stairs ---
# We land on 1F East inside the fenced room at (26, 4).
# Walk to the B1F East stairs warp landing at (21, 2):
print("Walking to B1F East stairs landing...")
safe_step("Left")
safe_step("Left")
safe_step("Left")
safe_step("Left")
safe_step("Left")
safe_step("Up")
safe_step("Up")

# Step Right onto the stairs at (22, 2) to warp down to B1F East
print("Warping DOWN to B1F East...")
mgba.press_buttons(["Right"])
time.sleep(2.5) # Wait for warp
print("Current position on B1F East:", get_pos())
mgba.take_screenshot()

# --- Step 9: Walk to B1F West and Retrieve Secret Key ---
# We land at (22, 2) on B1F East.
# Walk Down to Row 5, and Left to Column 1
print("Walking to B1F West along Row 5...")
safe_step("Down")
safe_step("Down")
safe_step("Down")
for _ in range(21):
    safe_step("Left")

# Face Up toward the Secret Key at (1, 4)
print("Facing Up toward the Secret Key...")
mgba.press_buttons(["Up", "sleep 300"])

# Retrieve the Secret Key
print("Retrieving the Secret Key...")
mgba.press_buttons(["A", "sleep 500"])
mgba.press_buttons(["A", "sleep 500"])
mgba.take_screenshot()

print("Mansion Key retrieval sequence complete!")
