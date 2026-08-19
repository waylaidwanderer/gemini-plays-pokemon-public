import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    # Wait for battle transition to fully end and overworld to accept input
    time.sleep(1.5)

print("Starting definitive 2F stairs pathfinder...")
print("Current position:", mgba.get_coordinates())

path_to_stairs = [
    ('Right', 5, 11),
    ('Right', 6, 11),
    ('Right', 7, 11),
    ('Right', 8, 11),
    ('Right', 9, 11),
    ('Right', 10, 11),
    ('Down', 10, 12),
    ('Right', 11, 12),
    ('Right', 12, 12),
    ('Up', 12, 11),
    ('Up', 12, 10),
    ('Up', 12, 9),
    ('Up', 12, 8),
    ('Up', 12, 7),
    ('Up', 12, 6),
    ('Up', 12, 5),
    ('Right', 13, 5),
    ('Right', 14, 5),
    ('Right', 15, 5), # Shutter gate (now OPEN in State B!)
    ('Right', 16, 5),
    ('Right', 17, 5),
    ('Right', 18, 5),
    ('Up', 18, 4),
    ('Up', 18, 3),
    ('Up', 18, 2) # Warp to 3F!
]

for btn, tx, ty in path_to_stairs:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         if new_pos != pos:
              print("Warp triggered! Position:", new_pos)
              break
         print("Blocked or battle! Escaping...")
         run_from_battle()
         time.sleep(1.0)
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
