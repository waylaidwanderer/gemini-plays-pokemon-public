import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Fleeing...")
    mgba.press_buttons(["sleep 2000"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2500"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def step(direction):
    pos_before = get_pos()
    print(f"Stepping {direction} from {pos_before}...")
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    if pos_before == pos_after:
        # Try a second time (handles turning in place)
        mgba.press_buttons([direction, "sleep 450"])
        pos_after = get_pos()
        if pos_before == pos_after:
            print("Blocked! Checking for battle...")
            run_from_battle()
            # Try once more after fleeing
            mgba.press_buttons([direction, "sleep 450"])
            pos_after = get_pos()
    return pos_after

# We are currently in battle! Let's flee!
print("Fleeing from the active wild battle...")
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 3000"])
print("Overworld position after fleeing:", get_pos())

# Ensure we are at (1, 11)
print("Walking to (1, 11)...")
pos = get_pos()
while pos['x'] != 1:
    pos = step("Left")
while pos['y'] != 11:
    pos = step("Down") if pos['y'] < 11 else step("Up")

# Check if Row 9 gate is open (by trying to walk UP Column 1 to Row 6)
print("Testing if Row 9 gate is open (walking UP to Row 6)...")
gate_open = True
for _ in range(5):
    pos_before = get_pos()
    pos_after = step("Up")
    if pos_before == pos_after:
        print("Row 9 gate is CLOSED! We are in State A.")
        gate_open = False
        break

if not gate_open:
    # We must walk back to (1, 11) and toggle the switch
    print("Walking back to (1, 11) to toggle the switch...")
    pos = get_pos()
    while pos['x'] != 1:
        pos = step("Left")
    while pos['y'] != 11:
        pos = step("Down") if pos['y'] < 11 else step("Up")

    print("Toggling Mewtwo switch at (2, 11) from (1, 11) facing RIGHT...")
    mgba.press_buttons(["Right", "sleep 300"])
    mgba.press_buttons(["A", "sleep 1200"]) # A secret switch!
    mgba.press_buttons(["A", "sleep 1200"]) # Would you like to toggle it?
    mgba.press_buttons(["A", "sleep 1200"]) # Selects YES
    mgba.press_buttons(["A", "sleep 1200"]) # Who wouldn't?
    mgba.press_buttons(["B", "sleep 500"])  # Close dialog

    print("Mansion toggled to State B! Re-attempting walk to Row 6...")
    # Walk UP Column 1 to Row 6 (5 steps from (1, 11))
    for _ in range(5):
        step("Up")

# Now we should be at (1, 6) in State B!
print("Walking RIGHT along Row 6 to Column 26...")
for _ in range(25):
    step("Right")

# Step onto pitfall
print("Stepping onto pitfall at (26, 6)...")
step("Right")
mgba.press_buttons(["sleep 2500"])

print("SUCCESS! Final landing position:", get_pos())
mgba.take_screenshot()
