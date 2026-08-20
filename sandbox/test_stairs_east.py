import mgba
import time

def walk_west_and_test_stairs():
    print("Walking west from (18, 8) to (7, 11) on 3F...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # 1. Walk Up to row 6
    mgba.press_buttons(["Up", "Up"])
    time.sleep(0.5)
    print("Position after Up:", mgba.get_coordinates())
    
    # 2. Walk Left along row 6 to column 11
    for col in range(17, 10, -1):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        print(f"Moved Left to column {col}:", mgba.get_coordinates())
        
    # 3. Walk Down along column 11 to row 11
    for row in range(7, 12):
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        print(f"Moved Down to row {row}:", mgba.get_coordinates())
        
    # 4. Walk Left through gate to (7, 11)
    for col in range(10, 6, -1):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        print(f"Moved Left to column {col}:", mgba.get_coordinates())
        
    # We should be at (7, 11). Let's turn UP and step UP onto stairs at (7, 10)
    print("At (7, 11). Turning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Stepping UP onto (7, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # Wait for warp
    
    final_pos = mgba.get_coordinates()
    print("Position after warp attempt:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    walk_west_and_test_stairs()
