import mgba
import time

print("Opening START menu...")
mgba.press_buttons(["Start", "sleep 500"])

print("Pressing Up 10 times to guarantee cursor is on POKéDEX...")
buttons = []
for i in range(10):
    buttons.append("Up")
    buttons.append("sleep 150")
mgba.press_buttons(buttons)
time.sleep(2.0)

print("Pressing Down once to go to POKéMON...")
mgba.press_buttons(["Down", "sleep 200"])

print("Pressing A to open POKéMON menu...")
mgba.press_buttons(["A", "sleep 800"])

mgba.take_screenshot()
print("POKéMON menu should be open now. Check the screen on the next turn!")
