import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Starting ultimate 2F to 3F stairs execution...")
buttons_pressed = 0

# Segment 1: Walk to the eastern switch at (12, 8) in State A
path_to_east_switch = [
    ('Down', 1, 12),
    ('Down', 1, 13),
    ('Right', 2, 13),
    ('Right', 3, 13),
    ('Right', 4, 13),
    ('Right', 5, 13),
    ('Up', 5, 12),
    ('Up', 5, 11),
    ('Up', 5, 10),
    ('Up', 5, 9),
    ('Up', 5, 8),
    ('Right', 6, 8),
    ('Right', 7, 8),
    ('Right', 8, 8),
    ('Right', 9, 8),
    ('Right', 10, 8), # Through the open gate in State A!
    ('Right', 11, 8),
    ('Right', 12, 8)
]

print("Walking to eastern switch at (12, 8)...")
for btn, tx, ty in path_to_east_switch:
    while True:
        pos = mgba.get_coordinates()
        print(f"2F East: At {pos}, moving {btn} to ({tx}, {ty})...")
        mgba.press_buttons([btn])
        buttons_pressed += 1
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == tx and new_pos['y'] == ty:
            print("Moved successfully.")
            break
        else:
            print("Blocked or battle! Escaping...")
            run_from_battle()
            buttons_pressed += 6
            time.sleep(0.5)

# Segment 2: Toggle the switch on the statue at (12, 9) to State B
pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 8:
    print("Reached (12, 8)! Toggling the switch to State B...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 1000"])
    mgba.press_buttons(["A", "sleep 1000", "B", "sleep 500"])
    print("Switch set to State B.")
    buttons_pressed += 3

# Segment 3: Walk from (12, 8) to (18, 2) stairs in State B
path_to_3f_stairs = [
    ('Up', 12, 7),
    ('Up', 12, 6),
    ('Up', 12, 5),
    ('Right', 13, 5),
    ('Right', 14, 5),
    ('Right', 15, 5), # Through the open gate in State B!
    ('Right', 16, 5),
    ('Right', 17, 5),
    ('Right', 18, 5),
    ('Up', 18, 4),
    ('Up', 18, 3),
    ('Up', 18, 2) # Warp!
]

print("Walking to northeast stairs...")
for btn, tx, ty in path_to_3f_stairs:
    while True:
        pos = mgba.get_coordinates()
        print(f"2F Warp: At {pos}, moving {btn} to ({tx}, {ty})...")
        mgba.press_buttons([btn])
        buttons_pressed += 1
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == tx and new_pos['y'] == ty:
            print("Moved successfully.")
            break
        else:
            if new_pos != pos:
                print("Warp triggered! Position:", new_pos)
                break
            print("Blocked or battle! Escaping...")
            run_from_battle()
            buttons_pressed += 6
            time.sleep(0.5)

print("Ultimate 2F execution finished. Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
