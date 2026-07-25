import mgba
import time

def main():
    print("Testing rightward ledge jump on B2F Starting Platform...")
    # Currently at (24, 11)
    
    # Step 1: Walk Right to (28, 11)
    print("Walking Right to Column 28...")
    mgba.press_buttons(["Right", "sleep 300", "Right", "sleep 300", "Right", "sleep 300", "Right", "sleep 300"])
    
    pos = mgba.get_coordinates()
    print(f"Reached Column 28: {pos}")
    
    # Step 2: Try to jump Right over the ledge to Column 29
    print("Pressing Right to jump over the ledge...")
    mgba.press_buttons(["Right", "sleep 600"])
    
    pos_after = mgba.get_coordinates()
    print(f"Position after jump: {pos_after}")
    
    # Take a screenshot to verify
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
