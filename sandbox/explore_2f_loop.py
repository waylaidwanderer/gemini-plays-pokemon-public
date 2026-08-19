import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking to 2F and then to 3F stairs...")

# Step 1: Walk left on 1F row 11 from (10, 11) to (5, 11)
path_left_1f = [
    ('Left', 9, 11),
    ('Left', 8, 11),
    ('Left', 7, 11),
    ('Left', 6, 11),
    ('Left', 5, 11)
]

for btn, tx, ty in path_left_1f:
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
        # Try again
        mgba.press_buttons([btn])
        time.sleep(0.3)
        new_pos2 = mgba.get_coordinates()
        if new_pos2['x'] == tx and new_pos2['y'] == ty:
            print("Moved successfully after battle.")
        else:
            print("Failed again. Position:", new_pos2)
            break

# Step 2: Step UP onto the stairs at (5, 10) to warp to 2F
print("Warping to 2F...")
mgba.press_buttons(["Up"])
time.sleep(1.5) # Wait for warp and automatic step down to (5, 11) on 2F
pos_2f = mgba.get_coordinates()
print("Position after warp attempt (expected 2F):", pos_2f)

# Step 3: On 2F, walk UP column 6 to row 5, then Left to column 5
path_bypass_2f = [
    ('Right', 6, 11),
    ('Up', 6, 10),
    ('Up', 6, 9),
    ('Up', 6, 8),
    ('Up', 6, 7),
    ('Up', 6, 6),
    ('Up', 6, 5),
    ('Left', 5, 5) # Step onto 3F stairs!
]

print("Executing 2F column 6 bypass to 3F...")
for btn, tx, ty in path_bypass_2f:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
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

# Take one step onto 3F stairs if we are at (5, 5)
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
mgba.take_screenshot()
