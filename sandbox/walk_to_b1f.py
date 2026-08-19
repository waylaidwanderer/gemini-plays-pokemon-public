import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Clearing battle text box and walking to B1F stairs on 1F (State B)...")

# Clear the text box
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Starting position in overworld:", pos)

# Path down column 9 from (9, 13) to (9, 26)
path_down = [
    ('Down', 9, 14),
    ('Down', 9, 15),
    ('Down', 9, 16),
    ('Down', 9, 17),
    ('Down', 9, 18),
    ('Down', 9, 19),
    ('Down', 9, 20),
    ('Down', 9, 21),
    ('Down', 9, 22),
    ('Down', 9, 23),
    ('Down', 9, 24),
    ('Down', 9, 25),
    ('Down', 9, 26)
]

print("Walking DOWN column 9 to Row 26...")
for btn, tx, ty in path_down:
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

# Path east along row 26 to (21, 26)
path_east = [
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

print("Walking EAST along row 26...")
for btn, tx, ty in path_east:
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

# Path UP column 21 to the stairs at (21, 24)
path_stairs = [
    ('Up', 21, 25),
    ('Up', 21, 24) # Warp to B1F!
]

print("Walking UP to B1F stairs...")
for btn, tx, ty in path_stairs:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
         print("Moved successfully.")
    else:
         # Check if we warped to B1F
         if tx == 21 and ty == 24 and new_pos['y'] != 24:
              print("Warped to B1F successfully!")
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

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
