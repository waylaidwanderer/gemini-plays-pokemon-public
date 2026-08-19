import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating to B1F in State B via 1F stairs (7, 10)...")
buttons_pressed = 0

# Segment 1: Walk to 2F stairs and warp to 1F (lands at 7, 11)
while True:
    pos = mgba.get_coordinates()
    print(f"2F Stairs: At {pos}...")
    
    # Check if we successfully warped to 1F (pos['y'] > 10 is row 11 on 1F)
    # But wait, we can just detect when the map changes or if we land at (7, 11) on 1F.
    # Since we start at (9, 9) on 2F, if we are at (7, 11) and just moved from (7, 10), we are on 1F!
    
    btn = None
    if pos['x'] == 9 and pos['y'] == 9:
        btn = 'Left'
    elif pos['x'] == 8 and pos['y'] == 9:
        btn = 'Left'
    elif pos['x'] == 7 and pos['y'] == 9:
        btn = 'Down'
    elif pos['x'] == 7 and pos['y'] == 10:
        print("At stairs on 2F! Toggling warp to 1F...")
        btn = 'Down' # Step DOWN onto stairs to warp to 1F
    else:
        print("Warp check...")
        break
        
    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        run_from_battle()
        buttons_pressed += 6
        time.sleep(0.5)
        
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

# Segment 2: Walk from 1F landing (7, 11) to B1F stairs (21, 24)
path_on_1f = [
    ('Right', 8, 11),
    ('Right', 9, 11),
    ('Right', 10, 11),
    ('Down', 10, 12),
    ('Down', 10, 13),
    ('Down', 10, 14),
    ('Down', 10, 15),
    ('Down', 10, 16),
    ('Right', 11, 16),
    ('Right', 12, 16),
    ('Right', 13, 16),
    ('Right', 14, 16),
    ('Right', 15, 16),
    ('Right', 16, 16),
    ('Right', 17, 16),
    ('Right', 18, 16),
    ('Right', 19, 16),
    ('Down', 19, 17),
    ('Down', 19, 18),
    ('Down', 19, 19),
    ('Down', 19, 20),
    ('Down', 19, 21),
    ('Down', 19, 22),
    ('Down', 19, 23),
    ('Down', 19, 24),
    ('Right', 20, 24),
    ('Right', 21, 24),
    ('Down', 21, 25) # Warp to B1F!
]

print("Walking to B1F stairs on 1F in State B...")
for btn, tx, ty in path_on_1f:
    while True:
        pos = mgba.get_coordinates()
        print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
        mgba.press_buttons([btn])
        buttons_pressed += 1
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == tx and new_pos['y'] == ty:
            print("Moved successfully.")
            break
        else:
            if new_pos != pos:
                print("Warp triggered! New Position:", new_pos)
                break
            print("Blocked or battle! Escaping...")
            run_from_battle()
            buttons_pressed += 6
            time.sleep(0.5)

print("Definitive 1F routing script completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
