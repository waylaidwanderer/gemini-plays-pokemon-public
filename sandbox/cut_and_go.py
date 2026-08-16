import mgba
import time

def press_and_wait(btn, delay=0.8):
    mgba.press_buttons([btn])
    time.sleep(delay)

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

# Step 1: Use CUT on the bush directly in front of us
print("Executing CUT on bush at (26, 13) from (26, 14)...")
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

# Step 2: Walk to the Gatehouse
waypoints = [
    (26, 9),
    (19, 9),
    (19, 8),
    (37, 8),
    (37, 2),
    (22, 2),
    (22, 4),
    (18, 4),
    (18, 3) # Warp into Gatehouse
]

success = True
for wp in waypoints:
    if not walk_to_waypoint(wp[0], wp[1]):
        success = False
        break

if success:
    print("Transitioning into Gatehouse...")
    time.sleep(1.5)
    
    # Check position inside Gatehouse (should be 3, 5)
    curr = mgba.get_coordinates()
    print("Position inside Gatehouse:", curr)
    
    # Walk to (3, 4)
    walk_to_waypoint(3, 4)
    
    # Face LEFT
    print("Facing LEFT to speak to clerk...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    final_pos = mgba.get_coordinates()
    print("Final position of Chunk B:", final_pos)
    mgba.take_screenshot()
else:
    print("Failed to reach Gatehouse.")
