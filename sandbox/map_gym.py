import mgba
import time

def move_and_report(path):
    for btn in path:
        print(f"Pressing {btn}...")
        mgba.press_buttons([btn])
        time.sleep(0.5)
        pos = mgba.get_coordinates()
        print(f"Current Position: {pos}")
        screenshot = mgba.take_screenshot()
        print(f"Screenshot saved.")

# We are at (5, 16). Let's walk UP up to 5 steps to explore the vertical corridor.
move_and_report(["Up", "Up", "Up", "Up", "Up"])
