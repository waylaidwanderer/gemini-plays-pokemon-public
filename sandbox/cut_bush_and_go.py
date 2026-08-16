import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

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

print("--- ROBUST CUT BUSH AND GO ---")

# Step 1: Walk to (26, 14) and face UP
walk_to_waypoint(26, 14)
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Step 2: Open Start menu and force cursor to POKEDEX (top)
press_and_screenshot("Start", "start_menu_open")

# Press UP 7 times to force cursor to the very top
for i in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.2)
print("Cursor forced to top (POKEDEX)")

# Press Down once to highlight POKEMON, then A to select
press_and_screenshot("Down", "highlight_pokemon")
press_and_screenshot("A", "pokemon_menu")

# Select TRUFFLE in Slot 2 (Down, then A)
press_and_screenshot("Down", "highlight_truffle")
press_and_screenshot("A", "truffle_submenu")

# Select Option 2 (CUT is Option 2: Down, then A)
press_and_screenshot("Down", "highlight_cut")
press_and_screenshot("A", "cut_execution", delay=3.0)

# Clear dialogue and exit back to overworld
for i in range(4):
    press_and_screenshot("B", f"clear_text_{i+1}", delay=0.5)

# Step 3: Walk to the Gatehouse
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
    print("Final position:", final_pos)
    mgba.take_screenshot()
else:
    print("Failed to reach Gatehouse.")
