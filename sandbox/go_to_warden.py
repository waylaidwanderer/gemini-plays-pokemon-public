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

# Select DIG (usually option 2 or 1 if it's the only field move? Paras typically only has DIG as field move, so it's option 1 or 2).
# Let's see: Paras movedex usually has DIG. Since we used DIG before, let's select DIG.
# Typically, field moves are listed above CANCEL.
# Let's press Down, A to select the field move.
print("Selecting DIG...")
bridge.press_buttons(["A"]) # Or "Down", "A" if DIG is second.
time.sleep(1.0)
bridge.press_buttons(["Down", "A"])
time.sleep(3.0) # Wait for DIG animation and warp

# Confirm we emerged in Fuchsia City outside Pokemon Center at (19, 28)
curr = bridge.get_coordinates()
print("Emerged after DIG at:", curr)

if curr is not None and curr[0] == 19 and curr[1] == 28:
    print("Successfully warped outside Fuchsia City Pokémon Center!")
    
    # 2. Walk to Warden's House at (27, 27)
    # Let's define the path from (19, 28) to Warden's House at (27, 27).
    # Is there any obstacle?
    # Pokémon Center is at (18-21, 22-27). We are at (19, 28) (directly south of PC).
    # Warden's House is at (27, 27) in the southeast quadrant.
    # To walk to (27, 27):
    # - Walk RIGHT along Row 28 to Column 27: (27, 28).
    # - Walk UP Column 27 to Row 27: (27, 27).
    # Let's walk there!
    print("Walking to Warden's House at (27, 27)...")
    walk_to_waypoint(27, 28)
    walk_to_waypoint(27, 27)
    
    # Enter the Warden's House (triggers transition)
    print("Entering Warden's House...")
    bridge.press_buttons(["Up"])
    time.sleep(1.0)
    
    # Check coordinates inside Warden's House (typically (4, 7) or similar)
    curr_house = bridge.get_coordinates()
    print("Inside Warden's House at:", curr_house)
    
    # 3. Walk to Warden at (2, 3) and talk to him!
    print("Walking to Warden at (2, 3)...")
    walk_to_waypoint(2, 4)
    bridge.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Talk to Warden
    print("Talking to Warden...")
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    
    # Mash A to clear dialogue
    print("Clearing dialogue...")
    for _ in range(10):
        bridge.press_buttons(["A"])
        time.sleep(0.8)
        
    print("Warden Interaction Complete! Check position and inventory to confirm Strength.")
else:
    print("DIG failed or we emerged in wrong position.")
