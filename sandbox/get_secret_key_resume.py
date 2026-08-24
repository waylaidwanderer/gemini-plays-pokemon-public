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

# Starting at (1, 10) on 3F West
print("PHASE 1: Walking to the 3F East pitfall...")
# Walk UP from (1, 10) to (1, 6) -> 4 steps
for _ in range(4):
    step("Up")

# Walk RIGHT from (1, 6) to (26, 6) -> 25 steps
for _ in range(25):
    step("Right")

# Step RIGHT onto the pitfall (27, 6) to drop
print("PHASE 2: Dropping through pitfall...")
step("Right")
# Wait for drop transition
mgba.press_buttons(["sleep 2500"])
print("Position after drop:", get_pos())
mgba.take_screenshot()
