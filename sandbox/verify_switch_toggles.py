import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # We are already at (3, 5). Let's face LEFT just in case.
    print("Facing LEFT...")
    mgba.press_buttons(["Left"])
    time.sleep(1.0)
    
    print("Toggling switch with generous delays...")
    
    # 1. Interact
    print("Step 1: Interact...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 2. Page 2
    print("Step 2: Page 2...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 3. Choose Yes on prompt
    print("Step 3: Choose Yes...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 4. Page 3
    print("Step 4: Page 3...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 5. Page 4
    print("Step 5: Page 4...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 6. Clear residual
    print("Step 6: Clear...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    print("Switch toggle sequence completed.")
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
