import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting correct Safari Zone entry sequence...")
    
    # 1. We are currently in rules explanation. Let's press A 9 times to clear it and return to overworld.
    print("Clearing current rules explanation...")
    for i in range(1, 10):
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(1.1)
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Position in overworld (should be at 3, 4): {pos}")
    
    # 2. Talk to clerk again (Talk 1)
    print("Talk 1: Initiating conversation...")
    bridge.press_buttons(["Left", "sleep 300", "A", "sleep 1200"])
    time.sleep(2.0)
    
    # Select NO to "first time here?"
    print("Talk 1: Selecting NO...")
    bridge.press_buttons(["Down", "sleep 600", "A", "sleep 1000"])
    time.sleep(1.5)
    
    # Clear "Sorry, you're a regular here!" and end dialogue
    print("Talk 1: Clearing 'regular here' dialogue...")
    bridge.press_buttons(["A", "sleep 800"])
    time.sleep(2.0)
    
    # 3. Talk to clerk again (Talk 2 - should immediately offer the hunt!)
    print("Talk 2: Initiating conversation for the hunt...")
    bridge.press_buttons(["Left", "sleep 300", "A", "sleep 1200"])
    time.sleep(2.0)
    
    # Press A to select YES to "Would you like to join the hunt?"
    print("Talk 2: Selecting YES to join hunt...")
    bridge.press_buttons(["A", "sleep 800"])
    time.sleep(1.2)
    
    # Press A to advance "That'll be $500, please!"
    print("Talk 2: Advancing $500 payment...")
    bridge.press_buttons(["A", "sleep 800"])
    time.sleep(1.2)
    
    # Press A to advance "We only use special SAFARI BALLS!"
    print("Talk 2: Advancing special balls...")
    bridge.press_buttons(["A", "sleep 800"])
    time.sleep(1.2)
    
    # Press A to advance "I'll call you when your time is up!" and warp!
    print("Talk 2: Advancing time is up and warping...")
    bridge.press_buttons(["A", "sleep 800"])
    time.sleep(3.0)
    
    pos = get_pos()
    print(f"Final position after warp attempt: {pos}")

if __name__ == "__main__":
    main()
