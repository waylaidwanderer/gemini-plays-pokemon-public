import bridge
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.2)
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = bridge.get_coordinates()
        if curr is None:
            print("Coordinates are None. Waiting...")
            time.sleep(0.5)
            continue
            
        x, y = curr
        if x == target_x and y == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        if curr == last_coords:
            stuck_count += 1
            if stuck_count > 4:
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y}). Attempting escape...")
                escape_battle()
                stuck_count = 0
                time.sleep(0.5)
                # Press B to recover any open menus
                bridge.press_buttons(["B", "B"])
                time.sleep(0.5)
        else:
            stuck_count = 0
            last_coords = curr
            
        # Choose direction to move
        if x < target_x:
            btn = "Right"
        elif x > target_x:
            btn = "Left"
        elif y < target_y:
            btn = "Down"
        elif y > target_y:
            btn = "Up"
            
        bridge.press_buttons([btn])
        time.sleep(0.44)

# 1. Open Menu and use DIG on TRUFFLE
print("Opening Start Menu...")
bridge.press_buttons(["Start"])
time.sleep(1.0)

# Select POKEMON (usually option 3 from top, but cursor defaults to last selected option which was SAVE)
# Let's count options:
# 1. POKEDEX
# 2. POKEMON
# 3. ITEM
# 4. ACE
# 5. SAVE (cursor should be here by default!)
# To go from SAVE to POKEMON, we press UP 3 times, then A.
print("Selecting POKEMON menu...")
bridge.press_buttons(["Up", "Up", "Up", "A"])
time.sleep(1.2)

# Select TRUFFLE (Paras, usually slot 2)
print("Selecting TRUFFLE (Paras)...")
bridge.press_buttons(["Down", "A"])
time.sleep(1.2)

print("Now inside TRUFFLE's sub-menu! Stopping to let the player verify options.")

