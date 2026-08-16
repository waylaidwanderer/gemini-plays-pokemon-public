import mgba
import time

def press_and_screenshot(btn, label, delay=0.8):
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

print("--- INSPECTING BAG ITEMS ---")
# Open Start menu
press_and_screenshot("Start", "start_menu")

# Select ITEM (third option: Down, Down, A)
mgba.press_buttons(["Down"])
time.sleep(0.3)
mgba.press_buttons(["Down"])
time.sleep(0.3)
press_and_screenshot("A", "item_menu_open")

# Scroll down 15 times, taking a screenshot each time
for i in range(15):
    press_and_screenshot("Down", f"bag_scroll_{i+1}", delay=0.5)

# Exit bag back to overworld
print("Exiting bag...")
mgba.press_buttons(["B"])
time.sleep(0.5)
mgba.press_buttons(["B"])
time.sleep(0.5)
mgba.press_buttons(["B"])
time.sleep(0.5)

print("Bag inspection complete!")
