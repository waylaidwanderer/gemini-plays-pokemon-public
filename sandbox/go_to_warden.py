import mgba
import time
from PIL import Image

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
                print(f"Stuck at ({x}, {y})")
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

print("--- PHASE 1: WALKING TO WARDEN ---")
# Stand at (2, 4) in front of the Warden at (2, 3)
walk_to_waypoint(2, 4)

# Face UP
print("Facing UP to talk to Warden...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Talking to Warden...")
mgba.press_buttons(["A"])
time.sleep(1.0)

# Complete dialogue (press A 12 times to clear all pages and get HM04)
print("Completing dialogue...")
for i in range(12):
    mgba.press_buttons(["A"])
    time.sleep(1.2)

# Take screenshot to verify we have the item
final_pos = mgba.get_coordinates()
print("Position after conversation:", final_pos)
mgba.take_screenshot()

