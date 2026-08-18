import mgba
import time

def move_to(target_x, target_y):
    current = mgba.get_coordinates()
    print(f"Starting move from {current} to ({target_x}, {target_y})")
    
    # Simple direct step-by-step path walking
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
            
        print(f"Pressing {button} to move from ({current['x']}, {current['y']})")
        mgba.press_buttons([button])
        time.sleep(0.3)
        
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"ERROR: Did not move from ({current['x']}, {current['y']}) when pressing {button}!")
            # Take a screenshot to help diagnose
            scr = mgba.take_screenshot()
            print(f"Screenshot taken: {scr}")
            return False
        current = next_pos
        
    print(f"Successfully reached ({current['x']}, {current['y']})")
    return True

# We want to go:
# (19, 10) -> (19, 6) -> (20, 6) -> (20, 5) -> (21, 5) -> (21, 3) -> (20, 3) -> (20, 1) -> enter elevator at (20, 0)
waypoints = [
    (19, 6),
    (20, 6),
    (20, 5),
    (21, 5),
    (21, 3),
    (20, 3),
    (20, 1)
]

success = True
for wp in waypoints:
    if not move_to(wp[0], wp[1]):
        success = False
        break

if success:
    print("Reached elevator entrance at (20, 1). Entering elevator at (20, 0)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    final_pos = mgba.get_coordinates()
    print(f"Final position after entering: {final_pos}")
    mgba.take_screenshot()
