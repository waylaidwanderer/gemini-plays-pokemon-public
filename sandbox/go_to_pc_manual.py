import bridge
import time

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
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y}). Retrying movement...")
                bridge.press_buttons(["A", "B"])
                time.sleep(0.5)
                stuck_count = 0
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

# Starting at (3, 7) inside Fuchsia Pokemon Center
print("Navigating to PC at (13, 3)...")
walk_to_waypoint(3, 4)
walk_to_waypoint(13, 4)
walk_to_waypoint(13, 3)

# Face UP to access the PC
print("Facing UP...")
bridge.press_buttons(["Up"])
time.sleep(0.5)

# Boot up the PC
print("Booting up PC...")
bridge.press_buttons(["A"])
time.sleep(1.0)
bridge.press_buttons(["A"]) # Confirm boot up text
time.sleep(1.0)

# Select BILL'S PC (usually option 1)
print("Selecting BILL'S PC...")
bridge.press_buttons(["A"])
time.sleep(1.0)
bridge.press_buttons(["A"]) # Clear "BILL'S PC was accessed" text
time.sleep(1.0)

# Select CHANGE BOX (usually option 4)
# Let's count options:
# 1. WITHDRAW PKMN
# 2. DEPOSIT PKMN
# 3. RELEASE PKMN
# 4. CHANGE BOX
# 5. CANCEL
# So we need to press DOWN 3 times, then A.
print("Selecting CHANGE BOX...")
bridge.press_buttons(["Down", "Down", "Down", "A"])
time.sleep(1.2)

# Select Box 4
# Currently Box 3 is active. The box list is:
# BOX 1
# BOX 2
# BOX 3
# BOX 4
# ...
# We need to press DOWN 3 times to highlight Box 4, then A.
print("Selecting BOX 4...")
bridge.press_buttons(["Down", "Down", "Down", "A"])
time.sleep(1.2)

# Select YES to confirm
print("Confirming box change...")
bridge.press_buttons(["A"]) # Select YES
time.sleep(1.2)
bridge.press_buttons(["A"]) # Clear "Changed BOX to BOX 4."
time.sleep(1.2)

# Exit BILL'S PC menu (press B to cancel)
print("Exiting BILL's PC...")
bridge.press_buttons(["B"])
time.sleep(1.0)

# Exit PC main menu (select CANCEL or press B)
print("Exiting PC...")
bridge.press_buttons(["B"])
time.sleep(1.0)

print("PC Box Switch process completed! Verification needed.")
