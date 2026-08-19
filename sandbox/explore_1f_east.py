import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Closing menus...")
# Press B 3 times to clear menus
mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
time.sleep(0.5)

# Verify we are in the overworld
pos = mgba.get_coordinates()
print("Position in overworld:", pos)

# Walk back to (3, 7) on 2F
path_to_stairs = [
    ('Right', 2, 3),
    ('Down', 2, 4),
    ('Down', 2, 5),
    ('Down', 2, 6),
    ('Down', 2, 7),
    ('Right', 3, 7)
]

print("Walking to stairs...")
for btn, tx, ty in path_to_stairs:
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    print(f"Step {btn} -> ({tx}, {ty}). Current pos: {new_pos}")

# Warp to 1F by pressing Down on (3, 7)
print("Warping to 1F...")
mgba.press_buttons(["Down"])
time.sleep(1.5)
print("Position on 1F:", mgba.get_coordinates())

# Now try to explore EAST on 1F from (16, 5)
east_path = [
    ('Right', 17, 5),
    ('Right', 18, 5),
    ('Right', 19, 5),
    ('Right', 20, 5),
    ('Right', 21, 5)
]

print("Exploring EAST on 1F...")
for btn, tx, ty in east_path:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, Next Step: {btn} to ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Step succeeded.")
    else:
        print(f"Failed to step to ({tx}, {ty}). Current coordinate: {new_pos}")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            print("Blocked. Stopping.")
            break
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot taken:", img)
