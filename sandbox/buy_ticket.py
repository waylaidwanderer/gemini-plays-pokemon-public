import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting exact 14 A presses to warp from YES/NO prompt...")
    # Press A 14 times with safe 1.1 second delays to ensure warp
    for i in range(1, 15):
        print(f"Pressing A {i}/14...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(1.1)
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position after dialogue: {pos}")

if __name__ == "__main__":
    main()
