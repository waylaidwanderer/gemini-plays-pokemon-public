import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Returning to 1F and exploring east...")

# Step 1: Walk to (5, 10) stairs on 2F to warp to 1F
path_to_stairs = [
    ('Right', 4, 11),
    ('Right', 5, 11),
    ('Up', 5, 10)
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
        # On 1F, we land at (5, 11) after the automatic step down
        # Wait, if we warp, the coordinates will change
        print("Warped or blocked. Position:", new_pos)
        break

time.sleep(1.0) # Wait for warp to complete
pos = mgba.get_coordinates()
print("Position after warp attempt:", pos)

# Step 2: From 1F (5, 11), walk down to (5, 26)
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

print("Walking down to Row 26 on 1F...")
for btn, tx, ty in path_down_1f:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
        print("Blocked, checking for battle...")
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

# Step 3: From (5, 26) on 1F, walk EAST as far as possible
print("Exploring EAST along Row 26 on 1F...")
current_x = 5
while current_x < 30:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, attempting to move RIGHT...")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] > pos['x'] and new_pos['y'] == 26:
        print("Moved Right successfully.")
        current_x = new_pos['x']
    else:
        print("Blocked or in battle, checking...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            new_pos_after = mgba.get_coordinates()
            current_x = new_pos_after['x']
        else:
            current_x = new_pos['x']

print("Final position of 1F exploration:", mgba.get_coordinates())
mgba.take_screenshot()
