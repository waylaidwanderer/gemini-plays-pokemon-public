import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

print("--- TEACHING CUT TO TRUFFLE ---")
# Currently at overworld (26, 15) facing UP/DOWN.
# Let's open start menu
press_and_screenshot("Start", "start_menu")

# Select ITEM (third option: Down, Down, A)
press_and_screenshot("Down", "item_down_1")
press_and_screenshot("Down", "item_down_2")
press_and_screenshot("A", "item_menu")

# Now we need to find HM01 in the bag.
# Let's write a loop that scrolls DOWN and presses A, checking if it is HM01.
# Usually, HM01 is near the top or bottom of the bag.
# Let's do a loop where we scroll down and look at the item names.
# Wait! Instead of scrolls, we can just press Down and A on each item to see its name,
# or we can write a script that scrolls and takes screenshots, but we can do a simpler way:
# Let's scroll down to look for HM01.
# Let's scroll Down and press A to see if it is HM01 (if it's HM01, it will show options "USE", "TOSS").
# Actually, HM01 cannot be tossed, only USED.
# Let's scroll through the items.
# Let's run a script that scrolls down, presses A on each slot, and if it's an HM, it will show "USE".
# Let's test the items one-by-one!
