import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def use_surf_from_option():
    print("Step 1: Pressing Up 4 times to move from OPTION to POKEMON...")
    for _ in range(4):
        press_and_wait("Up", 0.25)
        
    print("Step 2: Pressing A to enter POKEMON menu...")
    press_and_wait("A", 0.8)
    
    print("Step 3: Selecting SHELLBY...")
    press_and_wait("A", 0.5)
    
    print("Step 4: Selecting SURF...")
    press_and_wait("A", 0.8)
    
    print("Step 5: Clearing textbox...")
    press_and_wait("A", 0.8)
    
    # Verify by taking a screenshot
    img = mgba.take_screenshot()
    print(f"Surf execution complete! Verification screenshot: {img}")

use_surf_from_option()
