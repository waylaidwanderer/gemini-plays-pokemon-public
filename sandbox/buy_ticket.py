import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    # Starting at (3, 5) inside Gatehouse
    # Move to (4, 2) which is in front of the gatekeeper clerk
    print("Moving to front of clerk at (4, 2)...")
    bridge.press_buttons(["Right", "sleep 400"])
    bridge.press_buttons(["Up", "sleep 400"])
    bridge.press_buttons(["Up", "sleep 400"])
    bridge.press_buttons(["Up", "sleep 400"])
    
    time.sleep(1.0)
    pos = get_pos()
    print(f"Position before speaking: {pos}")
    
    # Face UP and talk
    print("Facing UP and speaking to clerk...")
    bridge.press_buttons(["Up", "sleep 400"])
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Loop to buy ticket and transition
    print("Starting buy ticket sequence...")
    for i in range(1, 15):
        print(f"Pressing A {i}/15...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(1.0)
        
        pos = get_pos()
        print(f"Current Position: {pos}")
        if pos == (15, 25) or pos == (14, 25) or pos == (15, 26):
            print(f"SUCCESS! Warped into Safari Zone Center at: {pos}")
            return
            
    print("Completed presses, did not detect warp.")

if __name__ == "__main__":
    main()
