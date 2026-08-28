import mgba
import time

print("Opening Trainer Card...")
# Press Start
mgba.press_buttons(["Start"])
time.sleep(0.6)

# Press A on player name (first option)
mgba.press_buttons(["A"])
time.sleep(1.2)

# Take screenshot of Trainer Card
img1 = mgba.take_screenshot()
print("Trainer Card screenshot taken:", img1)

# Press B to close Trainer Card
mgba.press_buttons(["B"])
time.sleep(0.6)

# Press Down, Down to BAG, then A
mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "A"])
time.sleep(1.2)

# Take screenshot of Bag
img2 = mgba.take_screenshot()
print("Bag screenshot 1 taken:", img2)

# Scroll down to see the rest of the Bag
for _ in range(5):
    mgba.press_buttons(["Down"])
    time.sleep(0.2)
    
# Take screenshot of Bag bottom
img3 = mgba.take_screenshot()
print("Bag screenshot 2 taken:", img3)

# Close Bag and Menu
mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
time.sleep(0.6)

print("Status check complete.")
