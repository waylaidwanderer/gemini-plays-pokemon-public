import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    # We are inside the Gatehouse at (3, 4) in dialogue.
    # Press A 12 times with pauses to buy the ticket and warp into the Safari Zone!
    print("Beginning buy ticket sequence...")
    for i in range(1, 13):
        print(f"Pressing A {i}/12...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(0.4)
        
    # Wait for the transition to finish
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position after dialogue: {pos}")

if __name__ == "__main__":
    main()
