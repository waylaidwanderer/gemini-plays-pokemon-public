import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Beginning buy ticket sequence from catch them!...")
    for i in range(1, 10):
        print(f"Pressing A {i}/9...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(0.4)
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position after dialogue: {pos}")

if __name__ == "__main__":
    main()
