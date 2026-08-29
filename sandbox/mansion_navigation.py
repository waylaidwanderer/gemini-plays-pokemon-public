import mgba
import time

def walk_up_to_row(target_y):
    current_pos = mgba.get_coordinates()
    print(f"Starting position: {current_pos}")
    
    while current_pos['y'] > target_y:
        # Press Up
        mgba.press_buttons(["Up"])
        time.sleep(0.3) # Wait for movement
        
        new_pos = mgba.get_coordinates()
        if new_pos == current_pos:
            print(f"Blocked or battle triggered at {current_pos}!")
            # Take a screenshot to inspect
            img = mgba.take_screenshot()
            print("Screenshot taken.")
            break
        current_pos = new_pos
        print(f"Moved to: {current_pos}")

walk_up_to_row(10)
