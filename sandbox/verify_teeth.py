import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Verifying if Gold Teeth are in the Bag...")
    # Close Trainer Card and any menus
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 500"])
    
    # Align cursor to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 200"])
        
    # Select ITEM (Down twice, A)
    # We go POKÉDEX -> POKÉMON (Down 1) -> ITEM (Down 2)
    bridge.press_buttons(["Down", "sleep 250", "Down", "sleep 250", "A", "sleep 800"])
    
    # Take screenshot of the Bag items!
    img = mgba.take_screenshot()
    print(f"Bag items screenshot: {img}")
    
    # Close Bag and menu
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])

if __name__ == "__main__":
    main()
