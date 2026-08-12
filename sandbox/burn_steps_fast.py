import bridge
import time

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos
        bridge.press_buttons(["sleep 50"])
    return None

def main():
    print("=== BURNING STEPS SAFELY (MAX 50 BUTTONS) ===")
    
    # We will press a maximum of 40 buttons in this execution to be safe.
    for i in range(20):
        pos = get_pos()
        if pos is None:
            print("Warped out!")
            break
            
        print(f"Cycle {i}: At {pos}, walking Up...")
        bridge.press_buttons(["Up", "sleep 120"])
        
        pos = get_pos()
        if pos is None:
            print("Warped out!")
            break
            
        print(f"Cycle {i}: At {pos}, walking Down...")
        bridge.press_buttons(["Down", "sleep 120"])

if __name__ == "__main__":
    main()
