import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Probing 1F row 11 towards the east...")
path_right = [
    ('Right', 8, 11),
    ('Right', 9, 11),
    ('Right', 10, 11),
    ('Right', 11, 11),
    ('Right', 12, 11),
    ('Right', 13, 11),
    ('Right', 14, 11),
    ('Right', 15, 11),
    ('Right', 16, 11),
    ('Right', 17, 11),
    ('Right', 18, 11),
    ('Right', 19, 11),
    ('Right', 20, 11)
]

for btn, tx, ty in path_right:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, Next Step: {btn} to ({tx}, {ty})")
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
            # Re-align
            new_pos_after = mgba.get_coordinates()
            found = False
            for idx, (b, tx_r, ty_r) in enumerate(path_right):
                if new_pos_after['x'] == tx_r and new_pos_after['y'] == ty_r:
                    print(f"Re-aligned to index {idx}")
                    # Skip to next index
                    break
            # Since we got blocked, we stop
            break
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
