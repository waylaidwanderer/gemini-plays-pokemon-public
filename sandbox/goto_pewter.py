import mgba
import time

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    print(f"Position before step: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(1.0) # wait for animation
    pos_after = mgba.get_coordinates()
    print(f"Position after step: {pos_after}")
    return pos_before, pos_after

# Try to walk Right 5 times to reach column 8
for i in range(5):
    print(f"--- Step Right {i+1} ---")
    before, after = walk_step("Right")
    # If coordinates didn't change, we might be blocked or in a battle
    if before == after:
         print("Warning: Position did not change. Checking screen or retrying...")
         # Take a screenshot to help debug
         mgba.take_screenshot()
         break
