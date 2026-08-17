import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def cut_bush_check():
    print("Step 1: Walking UP 2 steps to (41, 11) facing the bush at (41, 10)...")
    press_and_wait("Up", 0.3)
    press_and_wait("Up", 0.3)
    
    print("Step 2: Opening Start Menu...")
    press_and_wait("Start", 0.5)
    
    print("Step 3: Resetting cursor to POKEDEX...")
    for _ in range(6):
        press_and_wait("Up", 0.2)
        
    print("Step 4: Opening POKEMON menu...")
    press_and_wait("Down", 0.25)
    press_and_wait("A", 0.8)
    
    # Take screenshot of the party list to see TRUFFLE's slot
    img = mgba.take_screenshot()
    print(f"Party list screenshot: {img}")

cut_bush_check()
