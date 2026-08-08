import mgba
import time

def explore():
    print("Starting exploration from current position...")
    # Get current coordinates
    coords = mgba.get_coordinates()
    print(f"Initial coordinates: {coords}")
    
    # Let's walk Up 4 steps to row 19
    print("Walking Up 4 steps...")
    mgba.press_buttons(["Up", "Up", "Up", "Up"])
    time.sleep(1)
    
    coords = mgba.get_coordinates()
    print(f"Coordinates after walking Up: {coords}")
    
    # Take a screenshot to verify
    img_path = mgba.take_screenshot()
    print(f"Screenshot taken at: {img_path}")
    
    # Try walking Left 5 steps to column 21
    print("Walking Left 5 steps...")
    mgba.press_buttons(["Left", "Left", "Left", "Left", "Left"])
    time.sleep(1)
    
    coords = mgba.get_coordinates()
    print(f"Coordinates after walking Left: {coords}")
    
    # Take another screenshot
    img_path = mgba.take_screenshot()
    print(f"Screenshot taken at: {img_path}")

if __name__ == "__main__":
    explore()
