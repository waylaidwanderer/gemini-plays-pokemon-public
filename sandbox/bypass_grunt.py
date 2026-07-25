import mgba
import time

def main():
    print("Attempting to bypass the grunt by walking on row 10...")
    # Currently at (28, 11) facing Down
    
    # Step 1: Walk Up to (28, 10)
    print("Walking Up...")
    mgba.press_buttons(["Up", "sleep 300"])
    
    pos = mgba.get_coordinates()
    print(f"Position at (28, 10): {pos}")
    
    # Step 2: Walk Right 3 steps to (31, 10)
    print("Walking Right...")
    mgba.press_buttons(["Right", "sleep 300", "Right", "sleep 300", "Right", "sleep 300"])
    
    pos_after = mgba.get_coordinates()
    print(f"Final Position: {pos_after}")
    
    # Take a screenshot to verify
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
