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

# ==========================================================
# PHASE 0: Fuchsia City - CUT Bush and Walk to Gatehouse
# ==========================================================
print("Ensuring we face UP...")
bridge.press_buttons(["Up"])
time.sleep(0.5)

print("Opening Start menu...")
bridge.press_buttons(["Start"])
time.sleep(1.0)

print("Resetting Start menu cursor to POKEDEX...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.1)

print("Selecting POKEMON...")
bridge.press_buttons(["Down", "A"])
time.sleep(1.0)

print("Resetting POKEMON cursor to first Pokémon...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.1)

print("Selecting TRUFFLE...")
bridge.press_buttons(["Down", "A"])
time.sleep(1.0)

# Press A directly to select CUT (since the cursor defaults to the first option, which is CUT)
print("Selecting CUT...")
bridge.press_buttons(["A"])
time.sleep(3.0) # Wait for animation

print("Closing remaining dialogues/menus...")
bridge.press_buttons(["B", "B", "B"])
time.sleep(1.0)

curr = bridge.get_coordinates()
print("Bush Cut! Current Position:", curr)

# Walk to Gatehouse
print("Walking to Gatehouse...")
fuchsia_gatehouse_waypoints = [
    (26, 9),
    (19, 9),
    (19, 8),
    (37, 8),
    (37, 2),
    (22, 2),
    (22, 4),
    (18, 4),
    (18, 3) # Emerge in Gatehouse
]

for wx, wy in fuchsia_gatehouse_waypoints:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed gatehouse entry waypoint: ({wx}, {wy})")
        exit(1)

# Wait for map transition to Gatehouse
time.sleep(1.5)
curr = bridge.get_coordinates()
print("Entered Safari Gatehouse! Position:", curr)
