import mgba
import time
import numpy as np
from PIL import Image

def test_sequence():
    img0 = mgba.take_screenshot(as_image=True)
    arr0 = np.array(img0)
    print("Initial screenshot captured.")

    # Try pressing B multiple times with real-time delays and button clearing
    for i in range(5):
        mgba.clear_buttons()
        time.sleep(0.1)
        res = mgba.press_buttons(["B"])
        time.sleep(0.2)
        mgba.clear_buttons()
        time.sleep(0.1)
        
        img = mgba.take_screenshot(as_image=True)
        arr = np.array(img)
        diff = np.sum(arr0 != arr)
        print(f"Step {i+1} (B): diff = {diff}")
        if diff > 0:
            print("Visual change detected after B!")
            img.save("escape_success.png")
            return True

    # If B didn't change anything, try Down, Down, A (selecting CANCEL)
    seq = ["Down", "Down", "A"]
    for step_name in seq:
        mgba.clear_buttons()
        time.sleep(0.1)
        res = mgba.press_buttons([step_name])
        time.sleep(0.2)
        mgba.clear_buttons()
        time.sleep(0.1)
        
        img = mgba.take_screenshot(as_image=True)
        arr = np.array(img)
        diff = np.sum(arr0 != arr)
        print(f"Step ({step_name}): diff = {diff}")
        if diff > 0:
            print(f"Visual change detected after {step_name}!")
            img.save("escape_success.png")
            return True

    # If that didn't change anything, try A (confirming DEPOSIT)
    for i in range(3):
        mgba.clear_buttons()
        time.sleep(0.1)
        res = mgba.press_buttons(["A"])
        time.sleep(0.2)
        mgba.clear_buttons()
        time.sleep(0.1)
        
        img = mgba.take_screenshot(as_image=True)
        arr = np.array(img)
        diff = np.sum(arr0 != arr)
        print(f"Step {i+1} (A): diff = {diff}")
        if diff > 0:
            print("Visual change detected after A!")
            img.save("escape_success.png")
            return True

    print("No visual change across tested sequences.")
    return False

if __name__ == "__main__":
    test_sequence()
