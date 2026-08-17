import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def use_surf_perfect():
    print("Step 0: Pressing B to close any open menu...")
    press_and_wait("B", 0.5)
    
    print("Step 1: Pressing Start to open menu...")
    press_and_wait("Start", 0.5)
    
    print("Step 2: Pressing Up 6 times to force POKEDEX...")
    for _ in range(6):
        press_and_wait("Up", 0.2)
        
    print("Step 3: Moving to POKEMON...")
    press_and_wait("Down", 0.25)
    press_and_wait("A", 0.8)
    
    print("Step 4: Selecting SHELLBY...")
    press_and_wait("A", 0.5)
    
    print("Step 5: Selecting SURF...")
    press_and_wait("A", 0.8)
    
    print("Step 6: Clearing textbox...")
    press_and_wait("A", 0.8)
    
    # Verify by taking a screenshot
    img = mgba.take_screenshot()
    print(f"Surf execution complete! Verification screenshot: {img}")

use_surf_perfect()
