import mgba
import time

def main():
    print("Systematic exploration of B2F Starting Platform...")
    # Current position is (26, 11).
    
    # Let's try column 27:
    print("Testing Column 27...")
    mgba.press_buttons(["Right", "sleep 300"]) # Move to (27, 11)
    pos = mgba.get_coordinates()
    print(f"Position at Col 27: {pos}")
    
    mgba.press_buttons(["Down", "sleep 600"]) # Try to jump Down
    pos_down = mgba.get_coordinates()
    print(f"Position after Down at Col 27: {pos_down}")
    
    if pos_down['y'] > 11:
        print("Success! Jumped Down on Column 27!")
        mgba.take_screenshot()
        return
        
    # If not jumped down, let's try column 28:
    print("Testing Column 28...")
    # If we are still at (27, 11), we walk Right to (28, 11)
    mgba.press_buttons(["Right", "sleep 300"])
    pos_28 = mgba.get_coordinates()
    print(f"Position at Col 28: {pos_28}")
    
    mgba.press_buttons(["Down", "sleep 600"]) # Try to jump Down
    pos_down_28 = mgba.get_coordinates()
    print(f"Position after Down at Col 28: {pos_down_28}")
    
    if pos_down_28['y'] > 11:
        print("Success! Jumped Down on Column 28!")
        mgba.take_screenshot()
        return
        
    # Let's take a screenshot to see where we ended up
    mgba.take_screenshot()
    print("Ended up at:", pos_down_28)

if __name__ == "__main__":
    main()
