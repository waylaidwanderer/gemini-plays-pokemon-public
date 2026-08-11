import mgba
import time

def walk_to_target(target_x, target_y):
    print(f"Starting path from current position to ({target_x}, {target_y})")
    
    while True:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        print(f"Current Position: ({cx}, {cy})")
        
        if cx == target_x and cy == target_y:
            print("Reached target!")
            break
            
        # Check if map transition occurred
        # Area 1 (East) entrance is usually x=0
        if cx == 0 and cy in [22, 23]:
            print("Detected map transition to Area 1 (East)!")
            break
            
        buttons = []
        if cy > target_y:
            buttons.append("Up")
        elif cy < target_y:
            buttons.append("Down")
        elif cx < target_x:
            buttons.append("Right")
        elif cx > target_x:
            buttons.append("Left")
            
        if buttons:
            print(f"Pressing: {buttons[0]}")
            mgba.press_buttons([buttons[0]])
            # Allow a short sleep to let the frame process and position update
            mgba.press_buttons(["sleep 100"])
        else:
            break

# 1. Walk up to Row 22
walk_to_target(15, 22)

# 2. Walk right to Column 29
walk_to_target(29, 22)

# 3. Walk up to Row 11 (this should trigger the transition to Area 1 (East))
walk_to_target(29, 11)

# Double-check transition
pos = mgba.get_coordinates()
print(f"Final script position: ({pos['x']}, {pos['y']})")
