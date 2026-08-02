import mgba
import time

print("Starting Cerulean House North Exit Probe...")

pos = mgba.get_coordinates()
print(f"Current Position: {pos}")

# Step 1: From (12, 16), walk Right 1 to (13, 16), then Up 1 into (13, 15) doorway
mgba.press_buttons(["Right", "Up", "sleep 1000"])

p_in = mgba.get_coordinates()
print(f"Position inside building (13, 15): {p_in}")
s_in = mgba.take_screenshot()
print(f"Inside screenshot: {s_in}")

# Let's test walking Up along Col 2, Col 3, Col 4, Col 5 to check top wall tiles (y=0, y=1, y=2)
# Walk Up to (2, 3), then Up to test (2, 2) / (2, 1) / (2, 0)
mgba.press_buttons(["Up", "Up", "Up", "sleep 300"])
p_test1 = mgba.get_coordinates()
print(f"Position after Up test: {p_test1}")

s_test1 = mgba.take_screenshot()
print(f"Test 1 screenshot: {s_test1}")
