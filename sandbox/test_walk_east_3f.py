import mgba
import time

def test_walk():
    print("Testing walk East on 3F from (7, 11)...")
    for i in range(5):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Right {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle!")
            break
    mgba.take_screenshot()

test_walk()
