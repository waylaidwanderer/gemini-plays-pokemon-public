import mgba
import time

def main():
    print("Executing full loop traversal to return to southern area...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # 1. We are at (24, 15). Walk to (20, 12)
    # Path: Left x5, Up x2, Right
    # (24, 15) -> Left x5 -> (19, 15)
    # (19, 15) -> Up x2 -> (19, 13)
    # Wait, from (19, 13), we can go Left to (18, 13) -> (17, 13) -> Up to (17, 12) (wall).
    # To get to (20, 12) we go: Up from (19, 13) to (19, 12) -> Right to (20, 12).
    # Let's do this first block of moves:
    mgba.press_buttons(["Left", "Left", "Left", "Left", "Left"])
    time.sleep(1.5)
    mgba.press_buttons(["Up", "Up", "Right"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Pos after block 1: {pos}")
    
    # 2. From (20, 12), go to (14, 12) via Left spinner at (17, 10)
    # Path: Up, Up, Left, Left, Left
    mgba.press_buttons(["Up", "Up", "Left", "Left", "Left"])
    time.sleep(3.0) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Pos after block 2 (spin): {pos}")
    
    # 3. From (14, 12), go to (2, 9) via UP spinner at (12, 11)
    # Path: Up, Left, Left
    # Wait, (14, 12) -> Up to (14, 11) -> Left to (13, 11) -> Left to (12, 11) (UP spinner)
    mgba.press_buttons(["Up", "Left", "Left"])
    time.sleep(4.0) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Pos after block 3 (spin): {pos}")
    
    # 4. From (2, 9), go to (10, 12) via RIGHT spinner at (4, 11)
    # Path: Right, Down, Down, Right (onto 4, 11 spinner)
    # (2, 9) -> Right to (3, 9) -> Down to (3, 10) -> Down to (3, 11) -> Right to (4, 11) (spinner)
    mgba.press_buttons(["Right", "Down", "Down", "Right"])
    time.sleep(3.0) # Wait for spin to complete
    
    # Now we are at (8, 11). Go to (10, 12)
    # Path: Right, Right, Down
    mgba.press_buttons(["Right", "Right", "Down"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Pos before final spin: {pos}")
    
    # 5. From (10, 12), go to (15, 18) via DOWN spinner at (11, 14)
    # Path: Down, Down, Right
    mgba.press_buttons(["Down", "Down", "Right"])
    time.sleep(3.0) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Final pos: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
