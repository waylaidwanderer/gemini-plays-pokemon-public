import mgba
import time

# Script to check items in bag
print("Pressing Start...")
mgba.press_buttons(["Start", "sleep 300"])
time.sleep(0.5)

print("Moving Up to ITEM...")
mgba.press_buttons(["Up", "sleep 150", "Up", "sleep 150", "A", "sleep 300"])
time.sleep(0.5)

print("Taking first screenshot of inventory...")
img1 = mgba.take_screenshot()
img1.save("inventory_page1.png")

# Let's scroll down to see more items
print("Scrolling down...")
mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150"])
time.sleep(0.8)

print("Taking second screenshot of inventory...")
img2 = mgba.take_screenshot()
img2.save("inventory_page2.png")

# Close menu to return to overworld
print("Closing menu...")
mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])
print("Done checking inventory!")
