import mgba
import time

def find_opening():
    print("Testing paths to find the fence opening...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk Right to (9, 10)
    for col in range(5, 10):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print("At:", mgba.get_coordinates())
        
    # 2. Try to walk Down along column 9
    print("Walking Down along column 9...")
    for row in range(11, 14):
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print(f"Moved Down to row {row}: {pos}")
        
        # Try to step Right at each row to see if we can pass column 10!
        print("Testing Right...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        test_pos = mgba.get_coordinates()
        print(f"Test Right at row {pos['y']}: {test_pos}")
        
        if test_pos['x'] > pos['x']:
            print(f"SUCCESS! Found opening at row {pos['y']}!")
            mgba.take_screenshot()
            return True
            
        # If blocked on Right, step back to column 9 (if we turned)
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    find_opening()
