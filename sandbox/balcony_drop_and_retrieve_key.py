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

# --- 1. Navigate to 3F Balcony Ledge at (19, 18) ---
# Start from (21, 2)
print("Navigating to Column 19 Row 4...")
safe_step("Down") # (21, 3)
safe_step("Down") # (21, 4)
safe_step("Left") # (20, 4)
safe_step("Left") # (19, 4)

# Walk Down Column 19 to Row 18
print("Walking DOWN Column 19 to the balcony ledge...")
for _ in range(14):
    safe_step("Down")

# Step Down off the balcony ledge to drop to B1F East
print("Stepping DOWN to drop to B1F East...")
mgba.press_buttons(["Down"])
time.sleep(2.5) # Wait for drop transition
print("Current position after drop:", get_pos())
mgba.take_screenshot()

# --- 2. Walk to B1F West and Retrieve Secret Key ---
# We land at (19, 16) on B1F East.
# Let's walk UP Column 19 to Row 5:
print("Walking UP Column 19 to Row 5...")
for _ in range(11):
    safe_step("Up")

# Walk Left along Row 5 directly to B1F West at (1, 5)
# Note: the gate at (9, 5) is OPEN in State B!
print("Walking Left to B1F West along Row 5...")
for _ in range(18):
    safe_step("Left")

# Face Up toward the Secret Key at (1, 4)
print("Facing Up toward the Secret Key...")
mgba.press_buttons(["Up", "sleep 300"])

# Interact and press A to retrieve the Secret Key
print("Retrieving the Secret Key...")
mgba.press_buttons(["A", "sleep 500"])
mgba.press_buttons(["A", "sleep 500"])
mgba.take_screenshot()

print("Mansion Key retrieval sequence complete!")
