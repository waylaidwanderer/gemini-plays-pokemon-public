import mgba
import time

# We are at (10, 12) on B3F
print("Start Position:", mgba.get_coordinates())

# Walk Up to (10, 11)
mgba.press_buttons(["Up"])
time.sleep(0.5)
print("At (10, 11):", mgba.get_coordinates())

# Step Up onto (10, 10) UP spinner
print("Stepping UP onto (10, 10) spinner...")
mgba.press_buttons(["Up"])

# Let's monitor the position every 0.5 seconds for 8 seconds to see the exact slide path!
for i in range(16):
    time.sleep(0.5)
    print(f"Time {0.5 * (i+1)}s: {mgba.get_coordinates()}")

# Take screenshot at the end
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
