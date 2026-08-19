import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Walking left to the stairs at (7, 10)...")
pos = mgba.get_coordinates()
print("Initial position:", pos)

path = [
    ('Left', 10, 10),
    ('Left', 9, 10),
    ('Left', 8, 10),
    ('Left', 7, 10)
]

for btn, tx, ty in path:
    while True:
        pos = mgba.get_coordinates()
        print(f"At {pos}, moving {btn} to ({tx}, {ty})...")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == tx and new_pos['y'] == ty:
            print("Moved successfully.")
            break
        else:
            if new_pos != pos:
                print("Map transition or warp detected! Position:", new_pos)
                break
            print("Blocked or battle! Escaping...")
            run_from_battle()
            time.sleep(0.5)
            mgba.press_buttons([btn])
            time.sleep(0.4)
            new_pos2 = mgba.get_coordinates()
            if new_pos2['x'] == tx and new_pos2['y'] == ty:
                print("Moved successfully after battle.")
                break
            elif new_pos2 != pos:
                print("Map transition/warp detected after battle! Position:", new_pos2)
                break
            else:
                print("Failed again.")
                break

print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
