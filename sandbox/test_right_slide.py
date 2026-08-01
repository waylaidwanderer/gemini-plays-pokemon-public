import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Backtracking from (18, 15) to (20, 11)...")
# We are at (18, 15)
move(["Left", "Left"]) # to (16, 15)
move(["Up"]) # to (16, 14)
move(["Up", "sleep 2000"]) # onto (16, 13) UP spinner -> spins to (16, 11)
move(["Right", "Right", "Right", "Right"]) # to (20, 11)

final_pos = mgba.get_coordinates()
print("Final backtracking position:", final_pos)
screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
