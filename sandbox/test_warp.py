import mgba
import time

def main():
    pos1 = mgba.get_coordinates()
    print("Initial Position:", pos1)
    
    print("Stepping Up to (5, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for potential warp transition
    
    pos2 = mgba.get_coordinates()
    print("Position after Up:", pos2)
    
    # Let's take a screenshot to see what's on screen
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
