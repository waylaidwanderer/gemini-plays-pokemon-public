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

def use_dig_safe():
    print("Using DIG to warp out of Safari Zone...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Start", "sleep 500"])
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 250", "Down", "sleep 250", "A", "sleep 1000"]) # POKÉMON
    for _ in range(5):
        bridge.press_buttons(["Up", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "A", "sleep 800"]) # TRUFFLE (slot 2)
    bridge.press_buttons(["A", "sleep 4000"]) # Select DIG and wait for warp!

def main():
    pos = get_pos()
    print(f"Starting at: {pos}")
    
    if pos == (18, 24):
        # Walk Right 1 step to (19, 24)
        print("Walking Right to (19, 24)...")
        bridge.press_buttons(["Right", "sleep 500"])
        
    pos = get_pos()
    if pos == (19, 24):
        # Face DOWN towards the Gold Teeth at (19, 25)
        print("Facing DOWN towards Gold Teeth...")
        bridge.press_buttons(["Down", "sleep 500"])
        
        # Interact to pick up the Gold Teeth!
        print("Interacting to retrieve Gold Teeth...")
        bridge.press_buttons(["A", "sleep 1500"])
        
        # Clear textbox
        print("Clearing textboxes...")
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 250"])
            
        # Use DIG to exit back to Fuchsia City
        use_dig_safe()
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final Position: {pos}")
    
    # Take screenshot of final position
    img = mgba.take_screenshot()
    print(f"Screenshot: {img}")

if __name__ == "__main__":
    main()
