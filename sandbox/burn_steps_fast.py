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
    print("=== BURNING STEPS FROM (19, 24) ===")
    
    # Walk back and forth between Up and Down
    # We start at (19, 24).
    # Up goes to (19, 23).
    # Down goes to (19, 24).
    
    while True:
        pos = get_pos()
        if pos is None:
            # We warped out of Safari Zone!
            print("Warped out!")
            break
            
        print(f"At {pos}, walking Up...")
        bridge.press_buttons(["Up", "sleep 150"])
        
        pos = get_pos()
        if pos is None:
            print("Warped out!")
            break
            
        print(f"At {pos}, walking Down...")
        bridge.press_buttons(["Down", "sleep 150"])

if __name__ == "__main__":
    main()
