import mgba
import time

def explore_west():
    print("Starting exploration west from (16, 28)...")
    for i in range(16):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        pos_after = mgba.get_coordinates()
        print(f"Step {i+1}: Tried Left from {pos_before} -> ended at {pos_after}")
        if pos_before == pos_after:
            print("Blocked! Taking screenshot...")
            screenshot = mgba.take_screenshot()
            print(f"Screenshot saved to: {screenshot}")
            break

if __name__ == "__main__":
    explore_west()
