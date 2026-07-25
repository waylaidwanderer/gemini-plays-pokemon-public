import mgba
import time

def press_walk(direction, count=1):
    for _ in range(count):
        mgba.press_buttons([direction, "sleep 350"])

def main():
    print("Testing interactive ladder at B1F (25, 15)...")
    # Currently at (24, 30) on B1F
    
    # Step 1: Walk Right 1 step to (25, 30)
    press_walk("Right", 1)
    
    # Step 2: Walk Up 14 steps to (25, 16)
    print("Walking Up to (25, 16) south of the ladder...")
    press_walk("Up", 14)
    
    # We should now be at (25, 16) facing UP
    img_before = mgba.take_screenshot()
    print(f"Screenshot at (25, 16): {img_before}")
    
    # Step 3: Press A to interact with the ladder at (25, 15)
    print("Pressing A to climb...")
    mgba.press_buttons(["A", "sleep 600"])
    
    img_after = mgba.take_screenshot()
    print(f"Screenshot after A: {img_after}")

if __name__ == "__main__":
    main()
