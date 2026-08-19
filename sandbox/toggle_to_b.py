import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Starting State B toggle and 3F warp sequence...")
print("Current position:", mgba.get_coordinates())

# Path 1: (5, 10) to (2, 12)
path_to_switch = [
    ('Down', 5, 11),
    ('Down', 5, 12),
    ('Left', 4, 12),
    ('Left', 3, 12),
    ('Left', 2, 12)
]

for btn, tx, ty in path_to_switch:
    pos = mgba.get_coordinates()
    print(f"Moving {btn} to ({tx}, {ty}) from {pos}...")
    mgba.press_buttons([btn])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         print("Blocked! Checking battle...")
         run_from_battle()
         time.sleep(0.5)
         mgba.press_buttons([btn])
         time.sleep(0.4)
         new_pos2 = mgba.get_coordinates()
         if new_pos2['x'] == tx and new_pos2['y'] == ty:
              print("Moved successfully after battle.")
         else:
              print("Failed again. Position:", new_pos2)
              break

final_pos = mgba.get_coordinates()
if final_pos['x'] == 2 and final_pos['y'] == 12:
    print("At (2, 12). Toggling switch to State B...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 1000"])
    print("Selecting YES...")
    mgba.press_buttons(["A", "sleep 1000"])
    print("Clearing dialogue...")
    mgba.press_buttons(["B", "sleep 500"])

# Path 2: (2, 12) to (7, 10) warp to 3F
path_to_warp = [
    ('Right', 3, 12),
    ('Right', 4, 12),
    ('Right', 5, 12),
    ('Up', 5, 11),
    ('Right', 6, 11),
    ('Up', 6, 10),
    ('Right', 7, 10) # Warp!
]

print("Walking to 3F warp...")
for btn, tx, ty in path_to_warp:
    pos = mgba.get_coordinates()
    print(f"Moving {btn} to ({tx}, {ty}) from {pos}...")
    mgba.press_buttons([btn])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         if new_pos != pos:
              print("Warp triggered! Position:", new_pos)
              break
         print("Blocked! Checking battle...")
         run_from_battle()
         time.sleep(0.5)
         mgba.press_buttons([btn])
         time.sleep(0.4)
         new_pos2 = mgba.get_coordinates()
         if new_pos2['x'] == tx and new_pos2['y'] == ty:
              print("Moved successfully after battle.")
         elif new_pos2 != pos:
              print("Warp triggered after battle! Position:", new_pos2)
              break
         else:
              print("Failed again. Position:", new_pos2)
              break

print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
