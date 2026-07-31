import mgba
import time

def main():
    print("Escaping to columns 19-20 via UP spinner at (16, 18)...")
    # Current pos: (15, 18)
    # Step Right onto (16, 18) spinner
    mgba.press_buttons(["Right"])
    time.sleep(3) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Position after spin: {pos}")
    
    # Walk Right to (19, 13)
    mgba.press_buttons(["Right", "Right", "Right"])
    time.sleep(1)
    
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
