import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is not None:
        return pos[0], pos[1]
    return None

def main():
    print("Testing paths...")
    # Walk back to (19, 28)
    # Current is (16, 32)
    # Walk Right 3 to (19, 32)
    # Walk Up 4 to (19, 28)
    for _ in range(3):
        bridge.press_buttons(["Right"])
        time.sleep(0.5)
    for _ in range(4):
        bridge.press_buttons(["Up"])
        time.sleep(0.5)
        
    pos = get_pos()
    print("At:", pos)
    if pos != (19, 28):
        print("Failed to return to (19, 28)")
        return
        
    # Test Left on Row 28
    print("Testing Left on Row 28...")
    # We are at (19, 28). Let's try walking Left.
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
    pos28 = get_pos()
    print("Position after Left on Row 28:", pos28)
    
    if pos28 == (18, 28):
        # We can walk left on row 28! Let's try walking further left
        print("Walking further left on Row 28...")
        for _ in range(10):
            bridge.press_buttons(["Left"])
            time.sleep(0.5)
        print("Position after walking left on Row 28:", get_pos())
    else:
        # Go back to (19, 28)
        bridge.press_buttons(["Right"])
        time.sleep(0.5)
        
        # Test Left on Row 29
        print("Testing Left on Row 29...")
        bridge.press_buttons(["Down", "Left"])
        time.sleep(0.6)
        pos29 = get_pos()
        print("Position after Left on Row 29:", pos29)
        # return to (19, 28)
        bridge.press_buttons(["Right", "Up"])
        time.sleep(0.6)
        
        # Test Left on Row 30
        print("Testing Left on Row 30...")
        bridge.press_buttons(["Down", "Down", "Left"])
        time.sleep(0.6)
        pos30 = get_pos()
        print("Position after Left on Row 30:", pos30)
        # return to (19, 28)
        bridge.press_buttons(["Right", "Up", "Up"])
        time.sleep(0.6)

if __name__ == "__main__":
    main()
