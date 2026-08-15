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
    print("Talking to Gatekeeper clerk...")
    # Walk to (3, 2)
    # Since we are at (3, 5), walk UP 3 steps
    bridge.press_buttons(["Up", "sleep 450", "Up", "sleep 450", "Up", "sleep 450"])
    
    # Talk to clerk (A)
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Yes to "join the hunt for 500?" (A)
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Progress dialogue text:
    # "That'll be 500 please!" (A or B)
    # "We only use special SAFARI BALLS." (A or B)
    # "ACE received 30 SAFARI BALLS!" (A or B)
    # "We'll call you when you run out of time or SAFARI BALLS!" (A or B)
    # "Best of luck!" (A or B)
    for _ in range(8):
        bridge.press_buttons(["A", "sleep 800"])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Position after Gatekeeper transaction: {pos}")
    
    img = mgba.take_screenshot()
    print(f"Screenshot: {img}")

if __name__ == "__main__":
    main()
