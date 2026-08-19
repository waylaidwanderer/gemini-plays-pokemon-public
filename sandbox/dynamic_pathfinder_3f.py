import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.5)

print("Starting dynamic 3F routing execution...")

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Check if we reached (11, 11)
    if pos['x'] == 11 and pos['y'] == 11:
        print("Reached (11, 11)!")
        break
        
    btn = None
    tx, ty = None, None
    
    if pos['y'] == 13:
        btn = 'Up'
        tx, ty = 8, 12
    elif pos['y'] == 12:
        btn = 'Up'
        tx, ty = 8, 11
    elif pos['y'] == 11:
        if pos['x'] == 8:
            btn = 'Right'
            tx, ty = 9, 11
        elif pos['x'] == 9:
            btn = 'Right'
            tx, ty = 10, 11
        elif pos['x'] == 10:
            btn = 'Right'
            tx, ty = 11, 11
            
    if not btn:
        print("No valid move decided. We might be out of the expected room. Stopping.")
        break
        
    print(f"Pressing {btn} to reach ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
        # Check if position changed (battle warp or similar)
        if new_pos != pos:
            print("Warp or battle reset detected. New position:", new_pos)
            # If battle screen is open, run_from_battle will handle it
            run_from_battle()
        else:
            print("Blocked by NPC or wall. Waiting...")
            time.sleep(0.5)

# We are at (11, 11). Face right and toggle the switch to State B
print("At (11, 11). Toggling switch to State B...")
mgba.press_buttons(["Right", "sleep 200", "A", "sleep 1000"])
print("Selecting YES...")
mgba.press_buttons(["A", "sleep 1000"])
print("Clearing dialogue...")
mgba.press_buttons(["B", "sleep 500"])
print("Switch toggled successfully to State B!")

# Now walk to the eastern side:
# (11, 11) -> Down -> (11, 12) -> Right -> (12, 12) -> Right -> (13, 12)
path_east = [
    ('Down', 11, 12),
    ('Right', 12, 12),
    ('Right', 13, 12)
]

print("Walking to eastern side...")
for btn, tx, ty in path_east:
    while True:
        pos = mgba.get_coordinates()
        print(f"3F East: At {pos}, moving {btn} to ({tx}, {ty})...")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == tx and new_pos['y'] == ty:
             print("Moved successfully.")
             break
        else:
             print("Blocked or battle! Escaping...")
             run_from_battle()
             time.sleep(0.5)

print("Final Position on eastern side of 3F:", mgba.get_coordinates())
mgba.take_screenshot()
