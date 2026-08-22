import mgba
import time

def handle_battle():
    print("Checking for battle...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.25)

def walk_exact_route(waypoints):
    for wp in waypoints:
        tx, ty = wp
        print(f"Walking to waypoint ({tx}, {ty})...")
        attempts = 0
        while attempts < 35:
            pos = mgba.get_coordinates()
            cur = (pos['x'], pos['y'])
            if cur == (tx, ty):
                break
                
            dx = tx - cur[0]
            dy = ty - cur[1]
            
            if dx < 0: direction = "Left"
            elif dx > 0: direction = "Right"
            elif dy < 0: direction = "Up"
            elif dy > 0: direction = "Down"
            else:
                break
                
            pos_before = pos
            mgba.press_buttons([direction])
            time.sleep(0.55)
            pos = mgba.get_coordinates()
            
            if pos == pos_before:
                print(f"BUMPED at {cur} going {direction} towards {wp}!")
                handle_battle()
                time.sleep(0.5)
                pos = mgba.get_coordinates()
                if pos == pos_before:
                    print("Physical obstruction. Exiting to prevent loop.")
                    return False
            attempts += 1
    return True

print("Current position:", mgba.get_coordinates())

# 1. Flee from the wild Grimer battle first
print("Fleeing from battle...")
# Select RUN (Down, Right, A)
mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
time.sleep(1.5)

# Clear the "Got away safely!" text
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.25)

pos = mgba.get_coordinates()
print("Starting B1F East overworld coordinates:", pos)

# 2. Walk directly from current position (19, 16) to Secret Key Stand tile (1, 5)
route = [(19, 5), (1, 5)]
if walk_exact_route(route):
    print("SUCCESS! Reached Secret Key stand tile (1, 5)!")
    
    # 3. Face UP and retrieve the Secret Key at (1, 4)
    print("Facing UP and retrieving key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    # Interact to retrieve key, and clear text box
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B"])
    time.sleep(1.5)
    print("SECRET KEY RETRIEVED! Double checking coordinates...")
    print("Position:", mgba.get_coordinates())
    
    # 4. Escape using DIG (TRUFFLE in 6th slot, DIG is Option 1)
    print("Opening START menu to DIG out...")
    mgba.press_buttons(["Start", "sleep 500"])
    time.sleep(1.0)
    # Select POKéMON (option 2)
    mgba.press_buttons(["Down", "sleep 100", "A", "sleep 500"])
    time.sleep(1.0)
    # Select TRUFFLE (the 6th Pokémon, so Down 5 times, then A)
    mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "sleep 100", "A", "sleep 500"])
    time.sleep(1.0)
    # Select DIG (option 1, or press Down if DIG is not first, but TRUFFLE's option 1 is DIG!)
    mgba.press_buttons(["A", "sleep 500"])
    time.sleep(1.0)
    # Confirm
    mgba.press_buttons(["A"])
    time.sleep(3.0)
    print("ESCAPED! Final Cinnabar coordinates:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("FAILED route on B1F East.")
    mgba.take_screenshot()
