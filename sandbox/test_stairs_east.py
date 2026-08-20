import mgba
import time

def test_east_stairs():
    print("Testing eastern stairs at (18, 8) on 3F...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Move Down to row 6
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position after Down:", mgba.get_coordinates())
    
    # 2. Move Right along row 6 to column 18
    for col in range(13, 19):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print(f"Moved to column {col}:", mgba.get_coordinates())
        
    # 3. Move Down to row 8
    for row in range(7, 9):
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        print(f"Moved to row {row}:", mgba.get_coordinates())
        
    # 4. Wait for potential warp
    time.sleep(1.5)
    final_pos = mgba.get_coordinates()
    print("Final position after warp attempt:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    test_east_stairs()
