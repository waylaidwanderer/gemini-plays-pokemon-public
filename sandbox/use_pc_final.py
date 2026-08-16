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

print("--- NAVIGATING TO PC BYPASS ---")
# Start at (8, 7)
walk_to_waypoint(8, 4)
walk_to_waypoint(13, 4)

# Face UP
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Access PC
print("Accessing PC...")
press_and_wait("A", 1.5) # "ACE booted up the PC!"
press_and_wait("A", 1.0) # Clear "ACE booted up the PC!" and show main menu

# Highlight "BILL's PC" (it's first by default) and select
print("Selecting BILL's PC...")
press_and_wait("A", 1.5) # "Accessed BILL's PC."
press_and_wait("A", 1.0) # Clear and show Bill's PC menu

# Move cursor Down 3 times to "CHANGE BOX"
print("Navigating to CHANGE BOX...")
press_and_wait("Down", 0.5) # DEPOSIT PKMN
press_and_wait("Down", 0.5) # RELEASE PKMN
press_and_wait("Down", 0.5) # CHANGE BOX
press_and_wait("A", 1.5)    # "Which BOX?" and shows list of boxes

# Since we are currently on Box 4, the cursor is highlighting Box 4.
# We want to select Box 5 (which is the next option Down).
print("Selecting Box 5...")
press_and_wait("Down", 0.8) # Highlight Box 5
press_and_wait("A", 1.2)    # "Switching BOX will reboot the PC. Is that OK?"
press_and_wait("A", 1.5)    # Select YES (default)
press_and_wait("A", 1.5)    # Clear "BOX 5 is selected." and reboot

# Exit PC by pressing B multiple times
print("Exiting PC...")
press_and_wait("B", 1.0) # Close Bill's PC menu
press_and_wait("B", 1.0) # Close main PC menu
press_and_wait("B", 1.0) # Close PC entirely

print("PC interaction complete!")
mgba.take_screenshot()
