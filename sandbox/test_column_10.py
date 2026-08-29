import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print(f"test_column_10: Start coordinates: {pos}")
    
    # We are at (7, 14)
    # Walk to (6, 14) -> (6, 9)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    for y in range(13, 8, -1):
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
    # Walk Right to (9, 9)
    for x in range(7, 10):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
    # Walk Down to (9, 10)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    
    pos = mgba.get_coordinates()
    print(f"Standing at: {pos}")
    
    # Try to walk Right to (10, 10)
    print("Testing RIGHT to (10, 10)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    pos_after = mgba.get_coordinates()
    print(f"After RIGHT: {pos_after}")
    
if __name__ == "__main__":
    main()
