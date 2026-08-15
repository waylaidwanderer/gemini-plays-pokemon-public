import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting ultra-reliable buy ticket sequence via NO...")
    
    # 1. Down to highlight NO
    print("Pressing Down...")
    bridge.press_buttons(["Down", "sleep 600"])
    time.sleep(1.0)
    
    # 2. A to select NO
    print("Pressing A to select NO...")
    bridge.press_buttons(["A", "sleep 600"])
    time.sleep(1.0)
    
    # 3. A to clear "regular here!"
    print("Pressing A to clear dialogue...")
    bridge.press_buttons(["A", "sleep 600"])
    time.sleep(1.0)
    
    # 4. A to talk again
    print("Pressing A to talk again...")
    bridge.press_buttons(["A", "sleep 600"])
    time.sleep(1.5) # Wait extra long for YES/NO menu transition
    
    # 5. A to select YES to join hunt
    print("Pressing A to join hunt...")
    bridge.press_buttons(["A", "sleep 600"])
    time.sleep(1.0)
    
    # 6. A to advance "$500"
    print("Pressing A to advance $500...")
    bridge.press_buttons(["A", "sleep 600"])
    time.sleep(1.0)
    
    # 7. A to advance "special..."
    print("Pressing A to advance special balls...")
    bridge.press_buttons(["A", "sleep 600"])
    time.sleep(1.0)
    
    # 8. A to advance "time is up"
    print("Pressing A to advance time is up...")
    bridge.press_buttons(["A", "sleep 600"])
    time.sleep(1.0)
    
    # 9. A to warp into Safari Zone
    print("Pressing A to warp...")
    bridge.press_buttons(["A", "sleep 600"])
    time.sleep(2.0)
    
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
