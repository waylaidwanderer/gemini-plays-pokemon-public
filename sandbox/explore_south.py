import mgba
import time

def explore():
    print("Starting exploration...")
    pos = mgba.get_coordinates()
    print(f"Initial coordinates: {pos}")
    
    # Walk left 8 steps to Saffron Road (column 17)
    buttons = ["Left"] * 8
    mgba.press_buttons(buttons)
    
    pos = mgba.get_coordinates()
    print(f"Coordinates after walking left: {pos}")
    
    # Capture screenshot
    screenshot_file = mgba.take_screenshot()
    print(f"Screenshot taken: {screenshot_file}")

if __name__ == "__main__":
    explore()
