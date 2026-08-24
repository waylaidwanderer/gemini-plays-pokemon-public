import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(8):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 800"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 4:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting at (5, 11) on 3F West
print("Starting on 3F West:", get_pos())

# 1. Walk to (4, 11)
walk_step("Left")
print("Position 1:", get_pos())

# 2. Walk to (4, 13)
for _ in range(2):
    walk_step("Down")
print("Position 2:", get_pos())

# 3. Walk to (2, 13)
for _ in range(2):
    walk_step("Left")
print("Position 3:", get_pos())

# 4. Walk to (2, 12)
walk_step("Up")
print("Position 4:", get_pos())

# Now at (2, 12) facing UP towards the statue at (2, 11)
print("Toggling the switch at (2, 11)...")
mgba.press_buttons(["Up", "sleep 200"]) # Ensure facing Up
mgba.press_buttons(["A", "sleep 1000"]) # Interrupted by dialog: "A secret switch!"
mgba.press_buttons(["A", "sleep 1000"]) # Selects "YES" to "Press it?"
mgba.press_buttons(["B", "sleep 500"])  # Clears dialogue "Who wouldn't?"
print("Toggled! New position:", get_pos())

# Check state of the switch by looking at the screen or taking a screenshot
sc = mgba.take_screenshot()
print("Screenshot after toggling switch:", sc)
