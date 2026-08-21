import mgba
import time

print("Interacting with Mewtwo statue at (2, 11)...")
mgba.press_buttons(["A"])
time.sleep(1.2) # wait for prompt

print("Pressing 'Yes'...")
mgba.press_buttons(["A"])
time.sleep(1.2) # wait for confirmation text

print("Dismissing confirmation...")
mgba.press_buttons(["B"])
time.sleep(0.5)

print("Verifying overworld control by walking Right to (3, 12)...")
mgba.press_buttons(["Right"])
time.sleep(0.35)

print("Checking final position:")
pos = mgba.get_coordinates()
print("Position:", pos)
mgba.take_screenshot()
