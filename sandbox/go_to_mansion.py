import mgba
import time

print("Walking to Pokemon Mansion entrance...")
targets = [
    (6, 12),  # Walk Left to Column 6
    (6, 3)    # Walk Up to the entrance warp at (6, 3)
]

for target in targets:
    while True:
        current_pos = mgba.get_coordinates()
        print(f"Current Position: {current_pos}, Target: {target}")
        if current_pos['x'] == target[0] and current_pos['y'] == target[1]:
            break
            
        dx = target[0] - current_pos['x']
        dy = target[1] - current_pos['y']
        
        if dx < 0:
            direction = "Left"
        elif dx > 0:
            direction = "Right"
        elif dy < 0:
            direction = "Up"
        elif dy > 0:
            direction = "Down"
            
        print(f"Stepping {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.3)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Position after warping into Mansion:", pos)
mgba.take_screenshot()
