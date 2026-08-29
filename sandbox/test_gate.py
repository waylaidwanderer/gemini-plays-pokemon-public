import mgba
import time

def main():
    print("test_gate: Starting from current position...")
    pos = mgba.get_coordinates()
    print(f"Start coordinates: {pos}")
    
    # 1. Walk to (2, 13)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    pos = mgba.get_coordinates()
    print(f"At (2, 13)? Current: {pos}")
    
    # 2. Try to walk UP to (2, 12)
    print("Testing UP to (2, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    pos_after = mgba.get_coordinates()
    print(f"Position after trying UP: {pos_after}")
    
    # 3. If we succeeded, try to face UP and toggle the switch
    if pos_after['x'] == 2 and pos_after['y'] == 12:
        print("Succeeded! Facing UP towards switch...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        print("Toggling switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        print("Switch toggled!")
        
    pos_final = mgba.get_coordinates()
    print(f"Final position: {pos_final}")

if __name__ == "__main__":
    main()
