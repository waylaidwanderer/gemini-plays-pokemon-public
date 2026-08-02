import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting slide test from:", pos)

if pos['x'] == 10 and pos['y'] == 14:
    # Walk Right onto (11, 14) DOWN spinner
    print("Stepping onto (11, 14) DOWN spinner...")
    pos = move(["Right"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Position after slide from (11, 14):", pos)

mgba.take_screenshot()
