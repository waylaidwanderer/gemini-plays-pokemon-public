import mgba
import time

print("Dismissing 'Not quite yet!'...")
mgba.press_buttons(["B"])
time.sleep(1.0)

print("Interacting with switch...")
mgba.press_buttons(["A"])
time.sleep(1.2) # wait for text to scroll and Yes/No menu to appear

print("Selecting 'Yes'...")
mgba.press_buttons(["A"])
time.sleep(1.2) # wait for "Who wouldn't?" text

print("Dismissing 'Who wouldn't?'...")
mgba.press_buttons(["B"])
time.sleep(0.5)

print("Finished!")
mgba.take_screenshot()
