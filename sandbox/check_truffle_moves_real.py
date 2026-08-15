import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Executing TRUFFLE verification...")
    # Clear any menus
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 500"])
    
    # Align cursor to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 250"])
        
    # Select POKÉMON
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"])
    
    # Align party cursor to SHELLBY (slot 1) - do it SLOWLY!
    for _ in range(5):
        bridge.press_buttons(["Up", "sleep 400"])
        
    # Move to TRUFFLE (slot 2)
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 800"])
    
    # Take screenshot of TRUFFLE's pop-up options
    img_options = mgba.take_screenshot()
    print(f"TRUFFLE options screenshot: {img_options}")
    
    # Let's select Option 2 (Down twice, A) to open STATS
    bridge.press_buttons(["Down", "sleep 400", "Down", "sleep 400", "A", "sleep 1500"])
    img_stats = mgba.take_screenshot()
    print(f"TRUFFLE Stats page 1: {img_stats}")
    
    # Press A to go to page 2 (moves page)
    bridge.press_buttons(["A", "sleep 1500"])
    img_moves = mgba.take_screenshot()
    print(f"TRUFFLE Moves page: {img_moves}")

if __name__ == "__main__":
    main()
