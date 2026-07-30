import mgba
import time

# 1. Close the textbox first
print("Closing textbox...")
mgba.press_buttons(["A"])
time.sleep(0.5)

def walk_to(target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}, targeting ({target_x}, {target_y})")
    
    while pos['x'] != target_x or pos['y'] != target_y:
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        button = None
        if dy > 0:
            button = "Down"
        elif dy < 0:
            button = "Up"
        elif dx > 0:
            button = "Right"
        elif dx < 0:
            button = "Left"
            
        if not button:
            break
            
        print(f"Pressing {button}...")
        mgba.press_buttons([button])
        time.sleep(0.1)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Blocked!
            print(f"BLOCKED at {pos}! Trying again...")
            time.sleep(0.5)
            mgba.press_buttons([button])
            time.sleep(0.1)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"STUCK at {pos}! Exiting walk.")
                return False
                
        pos = new_pos
        print(f"Moved to: {pos}")
        
    return True

success = True
# Walk path to Gym exit
success = success and walk_to(5, 10)
success = success and walk_to(4, 10)
success = success and walk_to(4, 17)

if success:
    print("Pressing Down to exit Gym...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    final_pos = mgba.get_coordinates()
    print(f"Gym exit complete! Position: {final_pos}")
else:
    print("Gym exit failed or was blocked.")
