import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Potential battle or obstacle! Attempting to run/clear...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    # Select RUN (Right, Down, A)
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])

def walk_to_tile(tx, ty):
    print(f"Target: ({tx}, {ty})")
    max_attempts = 40
    for attempt in range(max_attempts):
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == tx and y == ty:
            print(f"Arrived at ({tx}, {ty})!")
            return True
            
        if x < tx:
            d = "Right"
        elif x > tx:
            d = "Left"
        elif y < ty:
            d = "Down"
        elif y > ty:
            d = "Up"
        else:
            return True
            
        print(f"Currently at ({x}, {y}). Stepping {d}...")
        mgba.press_buttons([d, "sleep 150"])
        
        pos_after = get_pos()
        if pos == pos_after:
            print("Did not move. Waiting for NPC or checking for battle...")
            moved = False
            for wait_attempt in range(5):
                mgba.press_buttons(["sleep 200"]) # Wait a bit for NPC to move
                mgba.press_buttons([d, "sleep 150"])
                pos_check = get_pos()
                if pos_check != pos:
                    moved = True
                    break
            
            if not moved:
                print("Still blocked. Assuming battle, running...")
                run_from_battle()
                mgba.press_buttons([d, "sleep 150"])
            
    print(f"Failed to reach ({tx}, {ty}) after {max_attempts} attempts.")
    return False

# Currently at (15, 6) on B1F East in State B
# Walk to (1, 5)
success = True
if success:
    success = walk_to_tile(15, 5)
if success:
    success = walk_to_tile(1, 5)

# Retrieve Secret Key at (1, 4)
if success:
    print("Picking up the Secret Key at (1, 4)...")
    mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
    print("Secret Key retrieved! Current position:", get_pos())

# DIG out back to Cinnabar Island
if success:
    print("Escaping via DIG...")
    mgba.press_buttons(["Start", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
    for _ in range(4): # 4 Down presses to select TRUFFLE (the 5th slot)
        mgba.press_buttons(["Down", "sleep 150"])
    mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE (Slot 5)
    mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
    time.sleep(3.0)
    print("SUCCESS! Final position on Cinnabar Island:", get_pos())
else:
    print("Failed navigation!")
