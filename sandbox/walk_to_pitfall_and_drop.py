import mgba
import time

def main():
    print("Starting probe down Column 26...")
    for step in range(12):
        pos = mgba.get_coordinates()
        print(f"Step {step}: Current Position: {pos}")
        
        # Check if we dropped (x, y should change drastically or map transition)
        # On 1F East, our Y would be different or map transition detected.
        # But even if coordinates are identical, we might see it in screenshot.
        
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print(f"Final Position: {pos}")
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
