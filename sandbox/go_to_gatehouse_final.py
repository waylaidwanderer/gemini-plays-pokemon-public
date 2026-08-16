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

print("--- CHUNK A: EXIT PC AND WALK TO BUSH ---")

# Step 1: Exit Pokémon Center from (13, 4)
walk_to_waypoint(3, 4)
walk_to_waypoint(3, 7)

# Step Down to exit
print("Stepping DOWN to exit Pokémon Center...")
mgba.press_buttons(["Down"])
time.sleep(1.5)

curr = mgba.get_coordinates()
print("Position outside PC:", curr)

if curr and curr['x'] == 19 and curr['y'] == 28:
    print("SUCCESS! Outside Pokémon Center.")
    
    # Step 2: Walk to (26, 12)
    waypoints = [
        (24, 28),
        (24, 21),
        (22, 21),
        (22, 14),
        (26, 14),
        (26, 12)
    ]
    for wp in waypoints:
        walk_to_waypoint(wp[0], wp[1])
        
    # Cut the bush
    cut_bush_at_26_13()
    
    final_pos = mgba.get_coordinates()
    print("Final position of Chunk A:", final_pos)
    mgba.take_screenshot()
else:
    print("Failed to exit Pokémon Center. Verify current position.")
