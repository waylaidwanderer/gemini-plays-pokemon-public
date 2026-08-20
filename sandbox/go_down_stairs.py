import mgba
import time

def go_down():
    print("Starting robust stair descent script...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    for attempt in range(30):
        pos = mgba.get_coordinates()
        print(f"Attempt {attempt + 1}: Current pos: {pos}")
        
        # Try to step Left
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == 6 and new_pos['y'] == 11:
            print("Successfully stepped Left to (6, 11)!")
            
            # Now step Down onto stairs at (6, 12)
            print("Stepping Down onto stairs at (6, 12)...")
            mgba.press_buttons(["Down"])
            time.sleep(2.0) # wait for warp
            
            warp_pos = mgba.get_coordinates()
            print("Position after warp attempt:", warp_pos)
            mgba.take_screenshot()
            return True
            
        # If we didn't move, the NPC is probably blocking us.
        # Press B to pass a turn/allow movement and sleep
        print("Blocked. Pressing B to let NPC move...")
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        
    print("Failed to walk Left after 30 attempts.")
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    go_down()
