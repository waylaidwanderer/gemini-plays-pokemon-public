import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking to northwest switch on 3F via Row 11...")

# Start at (8, 12) on 3F
path_to_switch = [
    ('Up', 8, 11),
    ('Left', 7, 11),
    ('Left', 6, 11),
    ('Left', 5, 11),
    ('Left', 4, 11),
    ('Left', 3, 11),
    ('Down', 3, 12),
    ('Left', 2, 12)
]

for btn, tx, ty in path_to_switch:
    pos = mgba.get_coordinates()
    print(f"3F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         print("Blocked or in battle, checking...")
         run_from_battle()
         time.sleep(0.5)
         mgba.press_buttons([btn])
         time.sleep(0.3)
         new_pos2 = mgba.get_coordinates()
         if new_pos2['x'] == tx and new_pos2['y'] == ty:
              print("Moved successfully after battle.")
         else:
              print("Failed again. Position:", new_pos2)
              break

# Now at (2, 12). Face UP and interact to toggle to State A
print("Facing UP and interacting with Mewtwo statue at (2, 11) on 3F...")
mgba.press_buttons(["Up", "sleep 200", "A", "sleep 1000"])

print("Confirming 'Yes' and clearing text...")
mgba.press_buttons(["A", "sleep 1000", "A", "sleep 500"])

# Verify position and State A
final_pos = mgba.get_coordinates()
print("Final Position (expected 2, 12):", final_pos)
mgba.take_screenshot()
