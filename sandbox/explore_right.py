import mgba
import time

def main():
    print("Testing movement to the Right along row 22...")
    for i in range(20):
        mgba.press_buttons(["Right", "sleep 300"])
        pos = mgba.get_coordinates()
        print(f"Step {i+1} - Right. Coordinates: {pos}")
        img = mgba.take_screenshot()
        print(f"Saved screenshot: {img}")

if __name__ == "__main__":
    main()
