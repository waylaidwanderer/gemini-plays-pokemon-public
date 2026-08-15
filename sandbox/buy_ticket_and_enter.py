import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Advancing dialogue to purchase Safari Zone ticket...")
    
    # We are at "Welcome to the SAFARI ZONE!"
    # Press A to advance
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Next text: "For just ¥500, you can catch all the POKéMON..."
    # Press A to advance
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Next text: "Would you like to join the hunt?" [YES/NO]
    # Select YES by pressing A
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Next text: "That'll be ¥500, please!..."
    # Press A to advance
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Next text: "Here are 30 SAFARI BALLS!..."
    # Press A to advance
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Next text: "We'll call you when you run out of time..."
    # Press A to advance and trigger the walk-in transition
    bridge.press_buttons(["A", "sleep 4000"])
    
    # Let's check our position after transition!
    pos = get_pos()
    print(f"Position after transition: {pos}")
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot taken: {screenshot}")

if __name__ == "__main__":
    main()
