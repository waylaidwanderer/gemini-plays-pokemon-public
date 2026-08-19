import mgba
import time

print("Walking to (2, 12) on 2F and toggling Mewtwo statue switch from the FRONT...")

# Start at (5, 11) on 2F
path = [
    ('Left', 4, 11),
    ('Left', 3, 11),
    ('Down', 3, 12),
    ('Left', 2, 12)
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
         print(f"Blocked. Expected ({tx}, {ty}), got {new_pos}")
         break

# We should be at (2, 12). Let's face UP and press A to trigger the switch!
print("Facing UP and interacting with Mewtwo statue at (2, 11)...")
mgba.press_buttons(["Up", "sleep 200", "A", "sleep 1000"])

# Select "Yes" to the switch question, and clear text
print("Confirming 'Yes' and clearing text...")
mgba.press_buttons(["A", "sleep 1000", "A", "sleep 500"])

final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
img = mgba.take_screenshot()
print("Screenshot:", img)
