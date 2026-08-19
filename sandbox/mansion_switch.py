import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking to 1F stairs from (2, 12) on 2F...")

# Step 1: Walk to (5, 10) stairs on 2F
path_to_stairs = [
    ('Right', 3, 12),
    ('Right', 4, 12),
    ('Right', 5, 12),
    ('Up', 5, 11),
    ('Up', 5, 10) # Warp to 1F (lands at (5, 11))
]

for btn, tx, ty in path_to_stairs:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         # Check if we warped to 1F
         if tx == 5 and ty == 10 and new_pos['y'] == 11 and new_pos['x'] == 5:
              print("Warped to 1F successfully!")
              break
         print("Blocked or in battle, checking...")
         run_from_battle()
         time.sleep(0.5)
         # Try again
         mgba.press_buttons([btn])
         time.sleep(0.3)
         new_pos2 = mgba.get_coordinates()
         if new_pos2['x'] == tx and new_pos2['y'] == ty:
              print("Moved successfully after battle.")
         else:
              print("Failed again. Position:", new_pos2)
              break

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Arrived on 1F at:", pos)

# Step 2: From 1F (5, 11), walk down column 5 to (5, 26)
path_down_1f = [
    ('Down', 5, 12),
    ('Down', 5, 13),
    ('Down', 5, 14),
    ('Down', 5, 15),
    ('Down', 5, 16),
    ('Down', 5, 17),
    ('Down', 5, 18),
    ('Down', 5, 19),
    ('Down', 5, 20),
    ('Down', 5, 21),
    ('Down', 5, 22),
    ('Down', 5, 23),
    ('Down', 5, 24),
    ('Down', 5, 25),
    ('Down', 5, 26)
]

print("Walking DOWN column 5 to row 26 on 1F...")
for btn, tx, ty in path_down_1f:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
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

# Step 3: From (5, 26) on 1F, walk Right to (21, 26)
path_east_1f = [
    ('Right', 6, 26),
    ('Right', 7, 26),
    ('Right', 8, 26),
    ('Right', 9, 26),
    ('Right', 10, 26),
    ('Right', 11, 26),
    ('Right', 12, 26),
    ('Right', 13, 26),
    ('Right', 14, 26),
    ('Right', 15, 26),
    ('Right', 16, 26),
    ('Right', 17, 26),
    ('Right', 18, 26),
    ('Right', 19, 26),
    ('Right', 20, 26),
    ('Right', 21, 26)
]

print("Walking EAST along row 26 on 1F...")
for btn, tx, ty in path_east_1f:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
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

# Step 4: From (21, 26) on 1F, walk UP column 21 to (21, 24)
path_to_b1f_stairs = [
    ('Up', 21, 25),
    ('Up', 21, 24) # Warp to B1F!
]

print("Walking to B1F stairs...")
for btn, tx, ty in path_to_b1f_stairs:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
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

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
