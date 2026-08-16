import mgba
import time

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = mgba.get_coordinates()
        if curr is None:
            time.sleep(0.5)
            continue
            
        x, y = curr['x'], curr['y']
        if x == target_x and y == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        if (x, y) == last_coords:
            stuck_count += 1
            if stuck_count > 4:
                print(f"Stuck at ({x}, {y}) trying to reach ({target_x}, {target_y})")
                return False
        else:
            stuck_count = 0
            last_coords = (x, y)
            
        if x < target_x: btn = "Right"
        elif x > target_x: btn = "Left"
        elif y < target_y: btn = "Down"
        else: btn = "Up"
        
        mgba.press_buttons([btn])
        time.sleep(0.42)

def cut_bush_at_26_13():
    print("Cutting bush at (26, 13)...")
    # Walk to (26, 12)
    walk_to_waypoint(26, 12)
    
    # Face DOWN
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    
    # Open Start menu
    mgba.press_buttons(["Start"])
    time.sleep(1.0)
    
    # Select POKEMON (second option: Down, then A)
    mgba.press_buttons(["Down", "A"])
    time.sleep(1.0)
    
    # Select TRUFFLE in Slot 2 (Down, then A)
    mgba.press_buttons(["Down", "A"])
    time.sleep(1.0)
    
    # Select Option 2 (CUT is Option 2: Down, then A)
    mgba.press_buttons(["Down", "A"])
    time.sleep(3.0) # Wait for CUT animation and text
    
    # Dismiss any leftover text by pressing B
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.5)
    print("CUT execution complete.")

# 1. Walk from (18, 4) to (26, 12) to cut the bush
waypoints_part1 = [
    (22, 4),
    (22, 2),
    (37, 2),
    (37, 9),
    (26, 9),
    (26, 12)
]

print("--- PART 1: WALKING TO CUT BUSH ---")
for wp in waypoints_part1:
    walk_to_waypoint(wp[0], wp[1])

# Cut the bush
cut_bush_at_26_13()

# 2. Walk from (26, 12) through cut bush to the Pokémon Center entrance at (19, 27)
waypoints_part2 = [
    (26, 14),
    (22, 14),
    (22, 21),
    (19, 21),
    (19, 28)
]

print("--- PART 2: WALKING TO PC ENTRANCE ---")
for wp in waypoints_part2:
    walk_to_waypoint(wp[0], wp[1])

# Enter Pokémon Center
print("Entering Pokémon Center...")
mgba.press_buttons(["Up"])
time.sleep(1.5)

curr = mgba.get_coordinates()
print("Position after entering:", curr)
mgba.take_screenshot()
