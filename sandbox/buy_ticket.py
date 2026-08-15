import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting reliable buy ticket sequence...")
    # Press A 13 times with very safe 1.0 second delays to ensure no inputs are dropped
    for i in range(1, 14):
        print(f"Pressing A {i}/13...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(1.0)
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position after dialogue: {pos}")

if __name__ == "__main__":
    main()
