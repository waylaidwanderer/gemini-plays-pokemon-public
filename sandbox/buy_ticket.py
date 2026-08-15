import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting diagnostic buy ticket sequence...")
    
    # 1. Close Trainer Card and Start Menu first if they are open
    print("Closing menus with B...")
    bridge.press_buttons(["B", "sleep 800", "B", "sleep 800"])
    time.sleep(2.0)
    
    # Verify we are at (3, 4) in the overworld
    pos = get_pos()
    print(f"Position in overworld: {pos}")
    if pos != (3, 4):
        print("Not at (3, 4).")
        return
        
    # Talk to the clerk
    print("Initiating talk by pressing Left then A...")
    bridge.press_buttons(["Left", "sleep 300", "A", "sleep 1200"])
    time.sleep(2.0)
    
    # Press A 14 times with extremely safe 1.5 second pauses
    # and print screenshot/text status after each press!
    for i in range(1, 15):
        print(f"\n--- Press {i}/14 ---")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(1.5)
        
        pos = get_pos()
        print(f"Position after press {i}: {pos}")
        if pos is not None and pos != (3, 4):
            print(f"Warp detected! Current position: {pos}")
            return
            
    print("Finished 14 presses. Did not warp.")

if __name__ == "__main__":
    main()
