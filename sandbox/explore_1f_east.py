import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking LEFT to column 5 on 1F/2F...")
path_left = [
    ('Left', 8, 11),
    ('Left', 7, 11),
    ('Left', 6, 11),
    ('Left', 5, 11)
]

for btn, tx, ty in path_left:
    pos = mgba.get_coordinates()
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        pass
    else:
        print(f"Blocked at ({pos['x']}, {pos['y']}) trying to go {btn}")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            break

# Now walk DOWN column 5 to row 27
print("Walking DOWN column 5 to row 27...")
pos = mgba.get_coordinates()
for row in range(pos['y'] + 1, 28):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['y'] == row:
        pass
    else:
        print(f"Blocked at row {new_pos['y']}. Let's check for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            break

# Now try to walk RIGHT along row 27 to find the eastern corridor
print("Walking RIGHT along the south on row 27...")
pos = mgba.get_coordinates()
for col in range(pos['x'] + 1, 28):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == col:
        pass
    else:
        print(f"Blocked at column {new_pos['x']} on row 27! Checking if we are blocked by a gate.")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            break

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
