import mgba
import time

def move_to(target_x, target_y):
    current = mgba.get_coordinates()
    print(f"Moving from {current} to ({target_x}, {target_y})")
    
    while current['x'] != target_x or current['y'] != target_y:
        dx = target_x - current['x']
        dy = target_y - current['y']
        
        button = None
        if dy < 0:
            button = "Up"
        elif dy > 0:
            button = "Down"
        elif dx < 0:
            button = "Left"
        elif dx > 0:
            button = "Right"
            
        if not button:
            break
            
        mgba.press_buttons([button])
        time.sleep(0.3)
        
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"ERROR: Stuck at ({current['x']}, {current['y']}) trying to move {button}!")
            mgba.take_screenshot()
            return False
        current = next_pos
        
    return True

# 1. Waypoints to the elevator on 5F (updated with the southern corridor path via Column 24)
waypoints_5f = [
    (15, 16),
    (24, 16),
    (24, 5),
    (22, 5),
    (22, 3),
    (20, 3),
    (20, 1)
]

print("Starting Saffron Silph Co. 5F to 3F Elevator Journey...")
success = True
for wp in waypoints_5f:
    if not move_to(wp[0], wp[1]):
        success = False
        break

if success:
    # 2. Enter elevator
    print("Entering elevator...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # 3. Walk to elevator panel at (3, 1)
    if move_to(3, 1):
        print("Interacting with elevator panel...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        
        # 4. Select 3F on elevator menu
        print("Selecting 3F...")
        mgba.press_buttons(["Down", "Down", "A"])
        time.sleep(1.0) # Wait for animation/warp
        
        # 5. Exit elevator on 3F
        print("Exiting elevator onto 3F...")
        exit_path = ["Down", "Down", "Left", "Down"]
        for btn in exit_path:
            mgba.press_buttons([btn])
            time.sleep(0.3)
            
        final_pos = mgba.get_coordinates()
        print(f"Exited elevator. Final position on 3F: {final_pos}")
        mgba.take_screenshot()
    else:
        print("ERROR: Failed to navigate inside elevator.")
else:
    print("ERROR: Failed 5F overworld navigation.")
