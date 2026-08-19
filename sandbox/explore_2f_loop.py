import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking LEFT to Mewtwo statue at (2, 11) on 2F...")

# Start at (6, 11)
path = [
    ('Left', 5, 11),
    ('Left', 4, 11),
    ('Left', 3, 11)
]

for btn, tx, ty in path:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
        print("Blocked, checking for battle...")
        run_from_battle()
        time.sleep(0.5)
        # Try once more after battle
        mgba.press_buttons([btn])
        time.sleep(0.3)
        new_pos2 = mgba.get_coordinates()
        if new_pos2['x'] == tx and new_pos2['y'] == ty:
            print("Moved successfully after battle.")
        else:
            print("Failed again. Current position:", new_pos2)
            break

# Now we should be at (3, 11) facing Left
# Let's turn left and press A
print("Turning left and pressing A to interact with Mewtwo statue at (2, 11)...")
mgba.press_buttons(["Left", "sleep 100", "A", "sleep 1000"])

# Take screenshot to verify
img = mgba.take_screenshot()
print("Final Position:", mgba.get_coordinates())
print("Screenshot:", img)
