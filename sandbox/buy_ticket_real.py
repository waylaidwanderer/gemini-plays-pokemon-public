import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting real buy ticket sequence...")
    # Loop to press A and progress the dialog until we warp into Safari Zone Center at (15, 25)
    for i in range(1, 15):
        print(f"Pressing A {i}/15...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(1.0)
        
        pos = get_pos()
        print(f"Current Position: {pos}")
        if pos == (15, 25) or pos == (14, 25) or pos == (15, 26):
            print(f"SUCCESS! Warped into Safari Zone Center at: {pos}")
            return
            
    print("Completed all presses without detecting warp.")

if __name__ == "__main__":
    main()
