import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print(f"test_column_10: Starting from {pos}")
    
    # 1. Walk Left to (5, 14)
    if pos['x'] == 6 and pos['y'] == 14:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        
    pos = mgba.get_coordinates()
    # 2. Walk Up Column 5 to (5, 10)
    if pos['x'] == 5 and pos['y'] == 14:
        for y in range(13, 9, -1):
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            
    pos = mgba.get_coordinates()
    # 3. Walk Right to (6, 10)
    if pos['x'] == 5 and pos['y'] == 10:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
    pos = mgba.get_coordinates()
    # 4. Walk Up to (6, 9)
    if pos['x'] == 6 and pos['y'] == 10:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
    pos = mgba.get_coordinates()
    # 5. Walk Right to (9, 9)
    if pos['y'] == 9 and pos['x'] < 9:
        for x in range(pos['x'] + 1, 10):
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            
    pos = mgba.get_coordinates()
    # 6. Walk Down to (9, 10)
    if pos['x'] == 9 and pos['y'] == 9:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        
    pos = mgba.get_coordinates()
    print(f"Standing at: {pos}")
    
    # 7. Try to walk Right to (10, 10)
    print("Testing RIGHT to (10, 10)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    pos_after = mgba.get_coordinates()
    print(f"After RIGHT: {pos_after}")

if __name__ == "__main__":
    main()
