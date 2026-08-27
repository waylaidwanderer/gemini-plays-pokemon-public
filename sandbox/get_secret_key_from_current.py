import mgba
import time

def escape_battle():
    print("MASHING B to return to main battle menu...")
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 400"])
    print("Navigating to RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 3000"])
    print("Dismissing escape text...")
    mgba.press_buttons(["A", "sleep 1000"])

def walk_step_robust(direction, expected_coords, retries=15):
    for i in range(retries):
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
            
        mgba.press_buttons([direction])
        time.sleep(0.45)
        
        new_pos = mgba.get_coordinates()
        if new_pos == expected_coords:
            print(f"Moved {direction} to {new_pos}")
            return True
            
        # If we didn't reach the expected coordinates, we might be in a battle
        print(f"Failed to move {direction} to {expected_coords}. Current pos: {new_pos}. Checking for battle...")
        time.sleep(0.5)
        # Try to escape battle
        escape_battle()
        time.sleep(1.0)
        
    return False

def run_steps_robust(steps):
    for d, c in steps:
        if not walk_step_robust(d, c):
            return False
    return True

# Ensure any menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# We are at (26, 9) on 1F East. Let's define the steps to the stairs at (22, 4)
steps_to_stairs = [
    ("Up", {"x": 26, "y": 8}),
    ("Up", {"x": 26, "y": 7}),
    ("Up", {"x": 26, "y": 6}),
    ("Up", {"x": 26, "y": 5}),
    ("Up", {"x": 26, "y": 4}),
    ("Left", {"x": 25, "y": 4}),
    ("Left", {"x": 24, "y": 4}),
    ("Left", {"x": 23, "y": 4}),
    ("Left", {"x": 22, "y": 4}),
    ("Up", {"x": 22, "y": 3})
]

if run_steps_robust(steps_to_stairs):
    print("SUCCESSFULLY WARPED TO B1F EAST!")
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warp:", pos)
else:
    print("FAILED TO WARP TO B1F EAST.")
    exit(1)

# On B1F East, we land at (22, 3). Let's define the steps to the Secret Key room on B1F West
steps_to_key_room = [
    ("Down", {"x": 22, "y": 4}),
    ("Left", {"x": 21, "y": 4}),
    ("Left", {"x": 20, "y": 4}),
    ("Left", {"x": 19, "y": 4}),
    ("Down", {"x": 19, "y": 5})
]

# Append horizontal steps along Row 5 from Column 18 to Column 1
for x in range(18, 0, -1):
    steps_to_key_room.append(("Left", {"x": x, "y": 5}))

if run_steps_robust(steps_to_key_room):
    print("SUCCESSFULLY REACHED THE SECRET KEY ROOM!")
    pos = mgba.get_coordinates()
    print("Position before picking up key:", pos)
else:
    print("FAILED TO REACH THE SECRET KEY ROOM.")
    exit(1)

# Align UP towards the Secret Key
print("Aligning UP towards the Secret Key...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Press A to pick up the Secret Key and dismiss the text boxes
print("Retrieving the Secret Key...")
mgba.press_buttons([
    "A", "sleep 2500",
    "A", "sleep 2500",
    "A", "sleep 2500"
])
time.sleep(8.5)

pos = mgba.get_coordinates()
print("Final position after picking up Secret Key:", pos)
mgba.take_screenshot()
