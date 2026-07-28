import mgba
import time

def main():
    print("Testing warp by walking Up to (25, 14)...")
    # Current position is (25, 15)
    mgba.press_buttons(["Up", "sleep 500"])
    
    pos = mgba.get_coordinates()
    print(f"Position after Up: {pos}")
    
    # Check if we transitioned
    # Let's take a screenshot
    screenshot = mgba.take_screenshot()
    print(f"Screenshot taken: {screenshot}")
    
if __name__ == "__main__":
    main()
