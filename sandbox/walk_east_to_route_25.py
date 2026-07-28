import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        print(f"Pressing {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.3)
        # Capture screenshot to see intermediate state
        img = mgba.take_screenshot()
        print(f"Step {i} taken. Screenshot: {img}")

# Starting at (14, 4) on Route 24
print("Walking East to Route 25...")
move("Right", 6)

print("Finished walking. Capturing final screenshot...")
final_img = mgba.take_screenshot()
print(f"Final Screenshot: {final_img}")
