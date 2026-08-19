import mgba
import time

print("Opening start menu...")
mgba.press_buttons(["Start", "sleep 500"])

# Item is usually 2nd or 3rd option. Let's look at standard Red/Blue start menu:
# POKEDEX
# POKEMON
# ITEM
# ACE
# SAVE
# OPTION
# EXIT
# So "ITEM" is 3rd option. We press Down twice, then A.
mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 500"])

# Take screenshot of page 1
print("Page 1 screenshot...")
scr1 = mgba.take_screenshot()
print("Saved page 1:", scr1)

# Press Down 7 times to see page 2
print("Scrolling to page 2...")
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100"])
time.sleep(1)
scr2 = mgba.take_screenshot()
print("Saved page 2:", scr2)

# Exit bag and menu
print("Closing menu...")
mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])
