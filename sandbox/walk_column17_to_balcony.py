import mgba
import time

def run_from_battle():
    print("In battle! Attempting to run...")
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

# Starting from (17, 1). Let's walk Down Column 17!
print("Starting walk down Column 17...")
pos = mgba.get_coordinates()
print("Initial Position:", pos)

while pos['y'] < 18:
    pos_before = pos
    pos = walk_step("Down")
    if pos_before['y'] == pos['y']:
        print(f"BLOCKED walking DOWN at coordinate: ({pos['x']}, {pos['y']})")
        break
    print(f"Reached: ({pos['x']}, {pos['y']})")

if pos['y'] >= 18:
    print("SUCCESS! Reached Row 18 (the Balcony corridor)!")
