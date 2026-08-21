import mgba
import time

print("First, dismissing any stuck 'Not quite yet!' textbox...")
mgba.press_buttons(["B"])
time.sleep(1.0)

print("1. Pressing A to interact with statue...")
mgba.press_buttons(["A"])
time.sleep(1.0) # wait for "A secret switch!"

print("2. Pressing A to advance text to 'Press it?'...")
mgba.press_buttons(["A"])
time.sleep(1.0) # wait for Yes/No menu

print("3. Pressing A to select 'Yes'...")
mgba.press_buttons(["A"])
time.sleep(1.0) # wait for "Who wouldn't?"

print("4. Pressing B to dismiss confirmation...")
mgba.press_buttons(["B"])
time.sleep(1.0) # wait for overworld

print("Verifying overworld control by walking Right to (3, 12)...")
mgba.press_buttons(["Right"])
time.sleep(0.35)

print("Checking final position:")
pos = mgba.get_coordinates()
print("Position:", pos)
mgba.take_screenshot()
