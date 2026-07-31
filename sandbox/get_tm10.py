import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.15)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.15)
        p2 = mgba.get_coordinates()
    return p1

print("Start Position:", mgba.get_coordinates())

# Executing the steps to reach the spinner at (4, 22)
moves = ["Down", "Right", "Right", "Right", "Up", "Up", "Up"]

for idx, move in enumerate(moves):
    mgba.press_buttons([move])
    pos = wait_for_movement()
    print(f"Step {idx+1} ({move}):", pos)

# Take a screenshot to see where we ended up
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
