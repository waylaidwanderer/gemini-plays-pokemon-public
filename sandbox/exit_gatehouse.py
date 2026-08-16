import mgba
import time
import os

print("--- DIAGNOSING MOVEMENT STALL ---")

def step_action(btn, step_num):
    print(f"Step {step_num}: Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(0.5)
    screenshot_path = mgba.take_screenshot()
    pos = mgba.get_coordinates()
    print(f"Step {step_num} complete. Position: {pos}, Screenshot: {screenshot_path}")

# Take initial screenshot
initial_path = mgba.take_screenshot()
print(f"Initial Position: {mgba.get_coordinates()}, Screenshot: {initial_path}")

# Run sequence of actions
step_action("B", 1)
step_action("B", 2)
step_action("A", 3)
step_action("B", 4)
step_action("Left", 5)
step_action("Left", 6)
step_action("Down", 7)

print("Done diagnosing!")
