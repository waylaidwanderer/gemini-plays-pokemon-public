import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.5)

print("Starting 3F pit drop execution...")
print("Current position:", mgba.get_coordinates())

# Path:
# (13, 12) -> Left to (12, 12) -> Up to (12, 7) -> Right to (21, 7) -> Up to (21, 4) -> Right to (24, 4) -> Down into pit (24, 5)
steps = [
    ('Left', 12, 12),
    ('Up', 12, 11),
    ('Up', 12, 10),
    ('Up', 12, 9),
    ('Up', 12, 8),
    ('Up', 12, 7),
    ('Right', 13, 7),
    ('Right', 14, 7),
    ('Right', 15, 7),
    ('Right', 16, 7),
    ('Right', 17, 7),
    ('Right', 18, 7),
    ('Right', 19, 7),
    ('Right', 20, 7),
    ('Right', 21, 7),
    ('Up', 21, 6),
    ('Up', 21, 5), # Shutter gate (now OPEN in State B!)
    ('Up', 21, 4),
    ('Right', 22, 4),
    ('Right', 23, 4),
    ('Right', 24, 4),
    ('Down', 24, 5) # Drop through pit!
]

for btn, tx, ty in steps:
    pos = mgba.get_coordinates()
    print(f"3F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         if new_pos != pos:
              print("Warp/Pit trigger detected! Position:", new_pos)
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
              print("Warp/Pit trigger detected after battle! Position:", new_pos2)
              break
         else:
              print("Failed again. Position:", new_pos2)
              break

print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
