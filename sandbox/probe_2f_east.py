import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking to (7, 9) on 2F...")
mgba.press_buttons(["Down"])
time.sleep(0.3)
print("Current position:", mgba.get_coordinates())

# Now try to walk Right as far as possible on row 9
path_right = [
    ('Right', 8, 9),
    ('Right', 9, 9),
    ('Right', 10, 9),
    ('Right', 11, 9),
    ('Right', 12, 9),
    ('Right', 13, 9)
]

print("Probing row 9 towards the east...")
for btn, tx, ty in path_right:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, Next Step: {btn} to ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Step succeeded.")
    else:
        print(f"Blocked at column {pos['x']} when trying to go Right to {tx}.")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")
        break

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
