import sys
import time
import os
import mgba

def get_pos():
    pos = mgba.get_coordinates()
    if pos is None:
        return None
    return pos['x'], pos['y']

def walk_step(direction):
    mgba.press_buttons([direction, "sleep 350"])

def main():
    print("=== TESTING COLUMN 37 VERTICAL CONNECTION ===")
    
    # We are currently at (18, 21) facing DOWN
    # Step 1: Walk UP Column 18 to Row 9 (12 steps Up)
    print("Step 1: Walking UP Column 18 to Row 9...")
    mgba.press_buttons(["Up"] * 12 + ["sleep 1000"])
    time.sleep(2.0)
    
    # Step 2: Walk RIGHT along Row 9 to Column 37 (19 steps Right)
    print("Step 2: Walking RIGHT along Row 9 to Column 37...")
    mgba.press_buttons(["Right"] * 19 + ["sleep 1000"])
    time.sleep(2.0)
    
    # Step 3: Walk DOWN Column 37 to Row 31 (22 steps Down)
    print("Step 3: Walking DOWN Column 37 to Row 31...")
    mgba.press_buttons(["Down"] * 22 + ["sleep 1000"])
    time.sleep(2.0)
    
    # Step 4: Walk LEFT along Row 31 to Column 19 (18 steps Left)
    print("Step 4: Walking LEFT along Row 31 to Column 19...")
    mgba.press_buttons(["Left"] * 18 + ["sleep 1000"])
    time.sleep(2.0)
    
    # Step 5: Walk UP Column 19 to Row 27 to enter building
    print("Step 5: Entering Pokemon Center...")
    mgba.press_buttons(["Up", "Up", "Up", "Up", "sleep 1000"])
    time.sleep(2.0)
    
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
