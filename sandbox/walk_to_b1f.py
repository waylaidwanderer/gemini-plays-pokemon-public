import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Navigating from 1F to 2F, then to 3F...")

# We are at (7, 11) on 1F
# Step 1: Walk to (5, 11) and warp to 2F via (5, 10)
path_to_2f = [
    ('Left', 6, 11),
    ('Left', 5, 11),
    ('Up', 5, 10) # Warp to 2F (lands at (5, 11) on 2F)
]

for btn, tx, ty in path_to_2f:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         if tx == 5 and ty == 10 and new_pos['y'] == 11 and new_pos['x'] == 5:
              print("Warped to 2F successfully!")
              break
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

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Arrived on 2F at:", pos)

# Step 2: On 2F, walk Right to (7, 11) and UP to (7, 10) to warp to 3F
path_to_3f = [
    ('Right', 6, 11),
    ('Right', 7, 11),
    ('Up', 7, 10) # Warp to 3F (lands at (7, 11) on 3F)
]

print("Walking on 2F to 3F stairs...")
for btn, tx, ty in path_to_3f:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         if tx == 7 and ty == 10 and new_pos['y'] == 11 and new_pos['x'] == 7:
              print("Warped to 3F successfully!")
              break
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

time.sleep(1.0)
pos_3f = mgba.get_coordinates()
print("Final Position on 3F:", pos_3f)
mgba.take_screenshot()
