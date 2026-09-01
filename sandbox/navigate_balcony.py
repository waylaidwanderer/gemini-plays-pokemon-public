import mgba
import time

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    # Give a short sleep to let the emulator register the movement
    time.sleep(0.15)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current} trying to move {direction}")
        return False
    return next_pos

def walk_path(path):
    for direction in path:
        res = step(direction)
        if not res:
            return False
        print(f"Moved to {res}")
    return True

# Current position is (16, 11).
# Path to (3, 11):
# 1. 2 steps Right to (18, 11)
# 2. 4 steps Up to (18, 7)
# 3. 6 steps Left to (12, 7)
# 4. 4 steps Down to (12, 11)
# 5. 9 steps Left to (3, 11)

path = (
    ["Right"] * 2 +
    ["Up"] * 4 +
    ["Left"] * 6 +
    ["Down"] * 4 +
    ["Left"] * 9
)

print("Starting navigation...")
if walk_path(path):
    print("Reached (3, 11) successfully! Now facing left and toggling the switch...")
    # Turn left to face (2, 11)
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
    
    # Toggle switch with 4 A-presses
    for i in range(1, 5):
        print(f"Pressing A ({i}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(0.4) # generous delay to allow dialogue to process
        
    print("Toggle sequence completed. Checking coordinates and taking screenshot...")
    pos = mgba.get_coordinates()
    print(f"Final coordinates: {pos}")
    mgba.take_screenshot()
else:
    print("Failed to navigate to the switch.")
