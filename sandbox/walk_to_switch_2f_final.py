import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Starting definitive 2F routing script to State B & 3F stairs...")
buttons_pressed = 0

# Segment 1: Walk to the west switch at (1, 11) in State A
print("Navigating to west switch at (1, 11)...")
while True:
    pos = mgba.get_coordinates()
    print(f"West Switch Path: At {pos}...")
    
    if pos['x'] == 1 and pos['y'] == 11:
        print("Reached switch access position!")
        break
        
    btn = None
    if pos['x'] == 9 and pos['y'] == 11:
        btn = 'Left'
    elif pos['x'] == 8 and pos['y'] == 11:
        btn = 'Left'
    elif pos['x'] == 7 and pos['y'] == 11:
        btn = 'Left'
    elif pos['x'] == 6 and pos['y'] == 11:
        btn = 'Left'
    elif pos['x'] == 5 and pos['y'] < 13:
        btn = 'Down'
    elif pos['y'] == 13 and pos['x'] > 1:
        btn = 'Left'
    elif pos['x'] == 1 and pos['y'] > 11:
        btn = 'Up'
    else:
        # Recovery
        if pos['x'] > 8:
            btn = 'Left'
        elif pos['y'] > 13:
            btn = 'Up'
        elif pos['x'] < 1:
            btn = 'Right'
        elif pos['y'] < 11:
            btn = 'Down'
            
    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        if btn == 'Left' and pos['y'] == 11 and (pos['x'] == 8 or pos['x'] == 9 or pos['x'] == 7):
            print("Bumped into Cooltrainer NPC on row 11. Waiting for her to move...")
            time.sleep(1.0)
            continue
        print("We are blocked or in battle!")
        run_from_battle()
        buttons_pressed += 6
        time.sleep(0.5)

# Segment 2: Toggle the switch to State B
pos = mgba.get_coordinates()
if pos['x'] == 1 and pos['y'] == 11:
    print("At (1, 11). Toggling the switch to State B...")
    mgba.press_buttons(["Right", "sleep 200", "A", "sleep 1000"])
    mgba.press_buttons(["A", "sleep 1000", "B", "sleep 500"])
    print("Switch set to State B.")
    buttons_pressed += 3

# Segment 3: Walk from (1, 11) to northeast stairs (18, 2) in State B
path_to_3f_stairs = [
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
    ('Right', 8, 8), # Through open central gate on row 8 in State B!
    ('Right', 9, 8),
    ('Right', 10, 8),
    ('Right', 11, 8),
    ('Right', 12, 8),
    ('Up', 12, 7),
    ('Up', 12, 6),
    ('Up', 12, 5),
    ('Right', 13, 5),
    ('Right', 14, 5),
    ('Right', 15, 5), # Through open northeast gate at (15, 5) in State B!
    ('Right', 16, 5),
    ('Right', 17, 5),
    ('Right', 18, 5),
    ('Up', 18, 4),
    ('Up', 18, 3),
    ('Up', 18, 2) # Warp!
]

print("Walking from (1, 11) to northeast stairs in State B...")
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

print("Definitive 2F routing script completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
