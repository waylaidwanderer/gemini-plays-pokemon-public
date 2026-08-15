import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    # Make sure we are in the overworld and menus are closed
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 200"])
        
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 400"])
    
    # Align cursor to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 150"])
        
    # Select POKÉMON
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 800"])
    
    # Align party cursor to SHELLBY (slot 1)
    for _ in range(5):
        bridge.press_buttons(["Up", "sleep 150"])
        
    # Move to TRUFFLE (slot 2)
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
    
    # Let's test if STATS is the 1st, 2nd, or 3rd option in the pop-up menu.
    # To do this, let's select Option 1 (Down once, A) first.
    print("Opening Option 1...")
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 1500"])
    
    # Take screenshot of Option 1 result
    img1 = mgba.take_screenshot()
    print(f"Option 1 screenshot: {img1}")
    
    # Press B to close whatever Option 1 opened (either Stats screen or overworld dialog)
    bridge.press_buttons(["B", "sleep 400"])
    
    # Re-open TRUFFLE menu to test Option 2
    bridge.press_buttons(["A", "sleep 500"])
    
    # Select Option 2 (Down twice, A)
    print("Opening Option 2...")
    bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 1500"])
    
    # Take screenshot of Option 2 result
    img2 = mgba.take_screenshot()
    print(f"Option 2 screenshot: {img2}")
    
    # Press A to transition to moves screen if we are in Stats
    bridge.press_buttons(["A", "sleep 1500"])
    img_moves = mgba.take_screenshot()
    print(f"Moves page screenshot: {img_moves}")

if __name__ == "__main__":
    main()
