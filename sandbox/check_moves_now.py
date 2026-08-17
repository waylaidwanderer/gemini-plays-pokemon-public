import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def check_moves_perfect():
    print("Opening start menu...")
    press_and_wait("Start", 0.5)
    
    print("Forcing cursor to top (POKEDEX)...")
    for _ in range(6):
        press_and_wait("Up", 0.2)
        
    print("Moving to POKEMON...")
    press_and_wait("Down", 0.25)
    press_and_wait("A", 0.8)
    
    print("Selecting SHELLBY (Slot 1)...")
    press_and_wait("A", 0.5)
    
    print("Selecting STATS...")
    press_and_wait("Down", 0.25)
    press_and_wait("A", 0.8)
    
    # Take screenshot of Page 1 of stats
    p1 = mgba.take_screenshot()
    print("Stats Page 1:", p1)
    
    # Switch to Page 2 of stats
    print("Switching to moves page...")
    press_and_wait("A", 0.8)
    
    # Take screenshot of Page 2 of stats
    p2 = mgba.take_screenshot()
    print("Stats Page 2 (Moves):", p2)
    
    # Exit back to overworld
    print("Exiting back to overworld...")
    for _ in range(5):
        press_and_wait("B", 0.3)
    print("Done!")

check_moves_perfect()
