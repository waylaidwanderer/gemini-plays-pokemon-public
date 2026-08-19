import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# Step 1: Step UP to enter Mansion from Cinnabar (6, 10)
print("Entering Pokémon Mansion...")
mgba.press_buttons(["Up"])
time.sleep(1.5) # Wait for warp
print("Position inside Mansion lobby:", mgba.get_coordinates())

# Step 2: On 1F, walk UP column 3 to stairs at (3, 2)
# We usually land at (2, 7) or (3, 7).
# Let's walk to column 3 row 7, and then UP to (3, 2).
path_1f = [
    ('Right', 3, 7),
    ('Up', 3, 6), ('Up', 3, 5), ('Up', 3, 4), ('Up', 3, 3), ('Up', 3, 2)
]

print("Walking to 1F/2F stairs...")
for btn, tx, ty in path_1f:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, pressing {btn} to reach ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if tx == 3 and ty == 2:
        time.sleep(1.5) # Wait for warp
        print("Warped to 2F! Position:", mgba.get_coordinates())
        break
    if new_pos['x'] == tx and new_pos['y'] == ty:
        continue
    else:
        print(f"Failed to reach ({tx}, {ty}), checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()

# Step 3: On 2F, walk from (3, 3) to 3F stairs at (7, 7)
# Path: DOWN column 3 to row 7, then Right to (7, 7)
path_2f = [
    ('Down', 3, 4), ('Down', 3, 5), ('Down', 3, 6), ('Down', 3, 7),
    ('Right', 4, 7), ('Right', 5, 7), ('Right', 6, 7), ('Right', 7, 7)
]

print("Walking to 2F/3F stairs...")
for btn, tx, ty in path_2f:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, pressing {btn} to reach ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if tx == 7 and ty == 7:
        time.sleep(1.5) # Wait for warp
        print("Warped to 3F! Position:", mgba.get_coordinates())
        break
    if new_pos['x'] == tx and new_pos['y'] == ty:
        continue
    else:
        print(f"Failed to reach ({tx}, {ty}), checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()

# Step 4: On 3F, walk from (7, 7) to switch at (2, 11)
# Path: Left along row 7 to column 2, then walk around Mewtwo statue at (2, 11) via column 3
path_3f = [
    ('Left', 6, 7), ('Left', 5, 7), ('Left', 4, 7), ('Left', 3, 7), ('Left', 2, 7),
    ('Down', 2, 8), ('Down', 2, 9), ('Down', 2, 10),
    ('Right', 3, 10),
    ('Down', 3, 11), ('Down', 3, 12),
    ('Left', 2, 12)
]

print("Walking to 3F switch...")
for btn, tx, ty in path_3f:
    pos = mgba.get_coordinates()
    print(f"3F: At {pos}, pressing {btn} to reach ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        continue
    else:
        print(f"Failed to reach ({tx}, {ty}), checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()

# Step 5: Toggle switch at (2, 11)
if mgba.get_coordinates() == {'x': 2, 'y': 12}:
    print("Facing UP towards the switch...")
    mgba.press_buttons(["Up", "sleep 300"])
    print("Interacting with Mewtwo statue...")
    mgba.press_buttons(["A", "sleep 1000"]) # open text box
    print("Pressing YES...")
    mgba.press_buttons(["A", "sleep 1000"]) # select YES
    print("Dismissing final text...")
    mgba.press_buttons(["A", "sleep 500"]) # dismiss dialogue
    print("Switch successfully toggled!")

print("Final position:", mgba.get_coordinates())
