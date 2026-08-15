import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    # Stand at (3, 4) in dialogue: "Hi! Is it your first time here?" with YES/NO
    # Press Down to highlight NO, then press A 8 times to buy ticket and warp!
    print("Beginning buy ticket sequence via NO...")
    
    # 1. Down
    bridge.press_buttons(["Down", "sleep 600"])
    time.sleep(0.4)
    
    # 2. A * 8
    for i in range(1, 9):
        print(f"Pressing A {i}/8...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(0.4)
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position after dialogue: {pos}")

if __name__ == "__main__":
    main()
