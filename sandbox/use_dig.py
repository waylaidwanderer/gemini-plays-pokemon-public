import mgba
import time

def use_dig():
    print("Selecting TRUFFLE from GUSTY's cursor position (Down 4 times)...")
    
    # Cursor is currently on GUSTY (2nd). Press Down 4 times to reach TRUFFLE (6th).
    for _ in range(4):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        
    # Press A to select TRUFFLE
    print("Pressing A on TRUFFLE...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Cursor should be on DIG. Press A to execute DIG.
    print("Executing DIG...")
    mgba.press_buttons(["A"])
    time.sleep(5.0) # Wait for warp animation and outside overworld to load
    
    # Print the coordinates of where we land outside
    final_pos = mgba.get_coordinates()
    print("Coordinates after DIG:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    use_dig()
