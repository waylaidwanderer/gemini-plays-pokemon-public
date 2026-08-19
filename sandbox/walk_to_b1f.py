import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Starting definitive B1F pathfinder script...")
print("Current position:", mgba.get_coordinates())

# Step 1: Walk from current position (14, 5) to (2, 12) on 2F
path_to_switch = [
    ('Left', 13, 5),
    ('Left', 12, 5),
    ('Down', 12, 6),
    ('Down', 12, 7),
    ('Down', 12, 8),
    ('Down', 12, 9),
    ('Down', 12, 10),
    ('Down', 12, 11),
    ('Down', 12, 12),
    ('Left', 11, 12),
    ('Left', 10, 12),
    ('Left', 9, 12),
    ('Left', 8, 12),
    ('Left', 7, 12),
    ('Left', 6, 12), # Wait! Is (6, 12) blocked on 2F?
    # Actually, let's go via Row 11 to avoid row 12 blockage if any!
    # Let's check row 11:
]

# Let's build a safe path to (2, 12) on 2F:
# From (14, 5):
# Left to (12, 5), Down column 12 to (12, 11), Left to (3, 11), Down to (3, 12), Left to (2, 12)
safe_path_to_switch = [
    ('Left', 13, 5),
    ('Left', 12, 5),
    ('Down', 12, 6),
    ('Down', 12, 7),
    ('Down', 12, 8),
    ('Down', 12, 9),
    ('Down', 12, 10),
    ('Down', 12, 11),
    ('Left', 11, 11),
    ('Left', 10, 11),
    ('Left', 9, 11),
    ('Left', 8, 11),
    ('Left', 7, 11),
    ('Left', 6, 11),
    ('Left', 5, 11),
    ('Left', 4, 11),
    ('Left', 3, 11),
    ('Down', 3, 12),
    ('Left', 2, 12)
]

print("Walking to switch at (2, 12)...")
for btn, tx, ty in safe_path_to_switch:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         print("Blocked or battle! Escaping...")
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

# Toggle the switch to State B
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    print("Reached (2, 12)! Toggling switch to State B...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 1000"])
    mgba.press_buttons(["A", "sleep 1000", "B", "sleep 500"])
    print("Switch set to State B.")

# Step 2: Walk from (2, 12) to northeast stairs at (18, 2) on 2F
# Path:
# (2, 12) -> Right to (3, 12) -> Up to (3, 11) -> Right to (12, 11) -> Up to (12, 5) -> Right to (18, 5) -> Up to (18, 2)
path_to_stairs = [
    ('Right', 3, 12),
    ('Up', 3, 11),
    ('Right', 4, 11),
    ('Right', 5, 11),
    ('Right', 6, 11),
    ('Right', 7, 11),
    ('Right', 8, 11),
    ('Right', 9, 11),
    ('Right', 10, 11),
    ('Right', 11, 11),
    ('Right', 12, 11),
    ('Up', 12, 10),
    ('Up', 12, 9),
    ('Up', 12, 8),
    ('Up', 12, 7),
    ('Up', 12, 6),
    ('Up', 12, 5),
    ('Right', 13, 5),
    ('Right', 14, 5),
    ('Right', 15, 5), # Gate tile (OPEN in State B!)
    ('Right', 16, 5),
    ('Right', 17, 5),
    ('Right', 18, 5),
    ('Up', 18, 4),
    ('Up', 18, 3),
    ('Up', 18, 2) # Stairs! Warp to 3F!
]

print("Walking to northeast stairs...")
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
