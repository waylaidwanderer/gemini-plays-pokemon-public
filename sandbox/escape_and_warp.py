import mgba
import time

def escape_and_toggle():
    print("Escaping from battle at (3, 12)...")
    # Cursor is on FIGHT. Down, Right, A to run.
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(3.0) # Wait for escape animation
    
    # Press B to make sure we are back on overworld
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Overworld position after escape:", pos)
    
    if pos['x'] == 3 and pos['y'] == 12:
        print("Walking Left to (2, 12)...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        
        curr = mgba.get_coordinates()
        print("Position after Left:", curr)
        
        if curr['x'] == 2 and curr['y'] == 12:
            print("Facing Up and toggling switch at (2, 11) to State A...")
            # We are at (2, 12). Press Up to face Up, then A to toggle
            mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "A", "sleep 500", "B"])
            time.sleep(1.0)
            
            final_pos = mgba.get_coordinates()
            print("Final position:", final_pos)
            mgba.take_screenshot()
            return True
            
    print("Could not complete. Coordinates are:", pos)
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    escape_and_toggle()
