import mgba
import time

def run():
    print("--- PROBING WESTWARD CROSSINGS ---")
    
    # We are currently at (24, 30).
    # Let's walk UP to Row 25. That is 5 steps UP.
    print("Walking up 5 steps to Row 25...")
    for i in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    pos = mgba.get_coordinates()
    print("Reached position:", pos)
    
    # Try to walk LEFT 3 steps (from 24 to 21)
    print("Attempting to walk LEFT...")
    for i in range(3):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
    pos = mgba.get_coordinates()
    print("Position after walking LEFT:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
