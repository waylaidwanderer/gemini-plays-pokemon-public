import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting at (19, 6)
print("Starting position:", mgba.get_coordinates())

# Walk Left to Column 17
print("Walking Left to Column 17...")
pos = mgba.get_coordinates()
while pos['x'] > 17:
    pos = walk_step("Left")
print("Arrived at:", pos)

# Walk Down Column 17 to see how far we can go
print("Walking Down Column 17...")
while pos['y'] < 18:
    pos_before = pos
    pos = walk_step("Down")
    if pos_before['y'] == pos['y']:
        print(f"BLOCKED walking DOWN at: ({pos['x']}, {pos['y']})")
        break
    print(f"Reached: ({pos['x']}, {pos['y']})")

if pos['y'] >= 18:
    print("SUCCESS: We reached Row 18 on Column 17!")
