import mgba
import time

def main():
    print("Testing movement to the Left...")
    for i in range(8):
        mgba.press_buttons(["Left", "sleep 300"])
        pos = mgba.get_coordinates()
        # Since mgba.get_coordinates() can sometimes return 0,0, let's take a screenshot too
        print(f"Step {i+1} - Left. Coordinates: {pos}")
        img = mgba.take_screenshot()
        print(f"Saved screenshot: {img}")

if __name__ == "__main__":
    main()
