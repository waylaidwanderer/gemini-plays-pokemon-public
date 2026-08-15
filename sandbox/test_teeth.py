import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Testing interaction at (19, 24) facing DOWN...")
    
    # 1. Close any menus
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
        
    # 2. Walk to (19, 24) if not there (we are already there)
    pos = bridge.get_coordinates()
    print(f"Current Position: {pos}")
    
    # 3. Face DOWN
    bridge.press_buttons(["Down", "sleep 500"])
    
    # 4. Press A to interact
    bridge.press_buttons(["A", "sleep 1500"])
    
    # 5. Capture screenshot of dialogue / interaction result
    img = mgba.take_screenshot()
    print(f"Interaction screenshot: {img}")
    
    # 6. Press B 5 times to close dialogue
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])

if __name__ == "__main__":
    main()
