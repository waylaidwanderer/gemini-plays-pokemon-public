import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Executing final TRUFFLE menu options probe...")
    # Close any menus
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 600"])
    
    # Align cursor to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 300"])
        
    # Select POKÉMON (Down once, A) - do it very slowly to ensure no lag eats the buttons!
    bridge.press_buttons(["Down", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Align party cursor to SHELLBY (slot 1) - do it slowly!
    for _ in range(5):
        bridge.press_buttons(["Up", "sleep 450"])
        
    # Move to TRUFFLE (slot 2)
    bridge.press_buttons(["Down", "sleep 450"])
    bridge.press_buttons(["A", "sleep 800"])
    
    # Take screenshot of TRUFFLE's pop-up options
    img_options = mgba.take_screenshot()
    print(f"TRUFFLE options pop-up: {img_options}")
    
    # Press B to cancel pop-up and return to party list
    bridge.press_buttons(["B", "sleep 500"])
    
    # Let's test the 3 options on TRUFFLE one by one by selecting them and taking screenshots!
    
    # Test Option 0 (A directly)
    print("Testing Option 0...")
    bridge.press_buttons(["A", "sleep 600"]) # Opens TRUFFLE menu
    bridge.press_buttons(["A", "sleep 1500"]) # Selects Option 0
    img_opt0 = mgba.take_screenshot()
    print(f"Option 0 result: {img_opt0}")
    bridge.press_buttons(["B", "sleep 600"]) # Back to party list
    
    # Test Option 1 (Down once, A)
    print("Testing Option 1...")
    bridge.press_buttons(["A", "sleep 600"]) # Opens TRUFFLE menu
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 1500"]) # Selects Option 1
    img_opt1 = mgba.take_screenshot()
    print(f"Option 1 result: {img_opt1}")
    bridge.press_buttons(["B", "sleep 600"]) # Back to party list
    
    # Test Option 2 (Down twice, A)
    print("Testing Option 2...")
    bridge.press_buttons(["A", "sleep 600"]) # Opens TRUFFLE menu
    bridge.press_buttons(["Down", "sleep 400", "Down", "sleep 400", "A", "sleep 1500"]) # Selects Option 2
    img_opt2 = mgba.take_screenshot()
    print(f"Option 2 result: {img_opt2}")
    
    # If Option 2 opened Stats screen, let's press A to transition to Moves page
    bridge.press_buttons(["A", "sleep 1500"])
    img_moves = mgba.take_screenshot()
    print(f"Moves page: {img_moves}")

if __name__ == "__main__":
    main()
