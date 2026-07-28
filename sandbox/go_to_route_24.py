import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.15)
        pos = mgba.get_coordinates()
        print(f"Moved {direction}. Now at {pos}")

# Starting at (9, 12)
print("Moving Right 11 steps to reach column 20...")
move("Right", 11)

print("Moving Up 13 steps to reach Route 24 transition...")
for i in range(13):
    mgba.press_buttons(["Up"])
    time.sleep(0.15)
    pos = mgba.get_coordinates()
    print(f"Step {i} Up. Position: {pos}")

print("Completed transition sequence. Taking screenshot...")
screenshot = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot}")
