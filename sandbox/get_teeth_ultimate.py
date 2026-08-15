import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Clearing dialogue to enter Safari Zone...")
    # Press A to progress text
    for i in range(5):
        print(f"Pressing A ({i+1})...")
        bridge.press_buttons(["A", "sleep 1200"])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Position after dialogue clearance: {pos}")
    
    img = mgba.take_screenshot()
    print(f"Screenshot: {img}")

if __name__ == "__main__":
    main()
