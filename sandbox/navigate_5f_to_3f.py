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

print("Re-aligning and navigating from (12, 1) to elevator...")

# 1. Walk from current position (12, 1) back to elevator entrance at (20, 1)
if move_to(20, 1):
    print("Reached elevator entrance. Entering elevator...")
    # Enter elevator door
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Wait for map transition to elevator (x < 5, y < 5)
    retries = 10
    while retries > 0:
        pos = mgba.get_coordinates()
        if pos['x'] < 5 and pos['y'] < 5:
            print(f"Transitioned to elevator map successfully at {pos}!")
            break
        print(f"Waiting for elevator map transition... current pos: {pos}")
        time.sleep(0.3)
        retries -= 1
        
    if retries == 0:
        print("ERROR: Elevator map transition timed out!")
        mgba.take_screenshot()
    else:
        # We are inside the elevator
        # 2. Walk to elevator panel at (3, 1)
        if move_to(3, 1):
            print("Interacting with elevator panel...")
            mgba.press_buttons(["A"])
            time.sleep(0.5)
            
            # 3. Select 3F on elevator menu
            print("Selecting 3F...")
            mgba.press_buttons(["Down", "Down", "A"])
            time.sleep(1.0) # Wait for animation/warp
            
            # 4. Exit elevator on 3F
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
    print("ERROR: Failed to return to elevator entrance.")
