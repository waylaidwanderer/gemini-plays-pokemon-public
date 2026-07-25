import mgba
import time

def main():
    print("Walking left along the northern corridor...")
    # Starting at (22, 7) on 1F
    # Target: (5, 7) (17 steps Left)
    
    for i in range(17):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Left", "sleep 320"])
        pos_after = mgba.get_coordinates()
        print(f"Step {i+1}: Before={pos_before}, After={pos_after}")
        
        # Check if coordinates didn't change (using GameState coords if we could,
        # but since mgba.get_coordinates() is unreliable, we check visually or if x remains 0 and we feel we might be blocked)
        # To be safe, let's take a screenshot after each step and check if we are in battle
        screenshot = mgba.take_screenshot()
        print(f"Saved screenshot: {screenshot}")
        
if __name__ == "__main__":
    main()
