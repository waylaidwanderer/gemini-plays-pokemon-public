import mgba
import time

def main():
    print("Navigating to (11, 19) southern area...")
    # Current pos: (1, 7)
    # 1. Walk to (4, 15) RIGHT spinner
    # (1, 7) -> Down x2 -> (1, 9) -> Right x2 -> (3, 9) -> Down x4 -> (3, 13) -> Right to (4, 13) -> Down x2 to (4, 15) (spinner)
    buttons = ["Down", "Down", "Right", "Right", "Down", "Down", "Down", "Down", "Right", "Down", "Down"]
    mgba.press_buttons(buttons)
    time.sleep(3) # Wait for spin to (8, 13)
    
    pos = mgba.get_coordinates()
    print(f"Pos after spin 1: {pos}")
    
    # 2. Walk to (11, 14) DOWN spinner
    # (8, 13) -> Right x2 -> (10, 13) -> Down to (10, 14) -> Right to (11, 14) (spinner)
    mgba.press_buttons(["Right", "Right", "Down", "Right"])
    time.sleep(3) # Wait for spin to (15, 18)
    
    pos = mgba.get_coordinates()
    print(f"Pos after spin 2: {pos}")
    
    # 3. Walk to (13, 18) LEFT spinner -> spins to (11, 19)
    # (15, 18) -> Left x2 to (13, 18) (spinner)
    mgba.press_buttons(["Left", "Left"])
    time.sleep(3) # Wait for spin to (11, 19)
    
    pos = mgba.get_coordinates()
    print(f"Pos at (11, 19): {pos}")
    
    # 4. Now explore Left along row 19!
    # Let's walk Left 10 steps to see how far we can go and take a screenshot
    mgba.press_buttons(["Left"] * 10)
    time.sleep(2)
    
    pos = mgba.get_coordinates()
    print(f"Final position: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
