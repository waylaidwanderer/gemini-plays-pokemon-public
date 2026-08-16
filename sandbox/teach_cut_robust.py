import mgba
import time

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(1.0)

print("Selecting ITEM...")
mgba.press_buttons(["Down", "Down", "A"])
time.sleep(1.0)

print("Selecting Slot 2 (HM01)...")
mgba.press_buttons(["Down", "A"])
time.sleep(1.0)

print("Choosing USE...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting TRUFFLE...")
mgba.press_buttons(["Down", "A"])
time.sleep(1.5)

print("Pressing A to clear 'ABLE to learn'...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print("Pressing A to choose YES to forget a move...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print("Pressing A to select SCRATCH to forget...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print("Pressing A to clear 'forgot SCRATCH'...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print("Pressing A to clear 'And...'...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print("Pressing A to clear 'learned CUT'...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print("Closing remaining menus...")
mgba.press_buttons(["B", "B", "B"])
time.sleep(1.0)

scr = mgba.take_screenshot()
print("Screenshot after teaching CUT:", scr)
