import mgba
import time

def interact_and_screenshot(direction, label):
    # Stand at current position, face direction, press A, take screenshot, then press B
    print(f"Interacting {direction} from {mgba.get_coordinates()}...")
    # Turn first
    mgba.press_buttons([direction])
    time.sleep(0.4)
    # Press A
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    # Take screenshot
    screenshot_path = mgba.take_screenshot()
    print(f"Saved screenshot for {label} to {screenshot_path}")
    # Press B to dismiss
    mgba.press_buttons(["B"])
    time.sleep(0.4)

def main():
    # We are currently at (12, 11).
    # Let's test facing Down towards (12, 12)
    interact_and_screenshot("Down", "face_down_from_12_11")
    
    # Let's walk to (12, 10)
    print("Moving Up to (12, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Test facing Down towards (12, 11)
    interact_and_screenshot("Down", "face_down_from_12_10")
    
    # Test facing Up towards (12, 9)
    interact_and_screenshot("Up", "face_up_from_12_10")

if __name__ == "__main__":
    main()
