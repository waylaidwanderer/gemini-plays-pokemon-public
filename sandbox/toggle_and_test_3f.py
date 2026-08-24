import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Fleeing...")
    mgba.press_buttons(["sleep 2000"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 3000"])
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

print("Starting at:", get_pos())

# Phase 1: Walk LEFT from (4, 11) to (1, 11) -> 3 steps
for _ in range(3):
    step("Left")

print("Arrived at (1, 11). Current position:", get_pos())

# Phase 2: Toggle Mewtwo switch at (2, 11) from (1, 11) facing RIGHT
print("Facing RIGHT towards (2, 11)...")
mgba.press_buttons(["Right", "sleep 300"])
print("Toggling switch...")
mgba.press_buttons(["A", "sleep 1200"]) # A secret switch!
mgba.press_buttons(["A", "sleep 1200"]) # Would you like to toggle it?
mgba.press_buttons(["A", "sleep 1200"]) # Selects YES
mgba.press_buttons(["A", "sleep 1200"]) # Who wouldn't?
mgba.press_buttons(["B", "sleep 500"])  # Close dialog

print("Switch toggled to State B! Current position:", get_pos())

# Phase 3: Walk UP Column 1 to Row 6 (5 steps)
for _ in range(5):
    step("Up")

# Phase 4: Walk RIGHT along Row 6 to Column 26 (25 steps)
for _ in range(25):
    step("Right")

# Phase 5: Step RIGHT onto pitfall to drop to 1F East inside fenced room
print("Stepping onto pitfall...")
step("Right")
mgba.press_buttons(["sleep 2500"])

print("SUCCESS! Landing position on 1F East:", get_pos())
mgba.take_screenshot()
