import mgba
import time

# We are at (18, 8) on 3F in State A.
# Route to the balcony gate:
# 1. Up to (18, 7)
# 2. Right to (23, 7)
# 3. Down to (23, 11)
# 4. Right to (25, 11)
# 5. Down to (25, 14)
# 6. Left to (21, 14)
# 7. Down to (21, 15)
# 8. Left to (20, 15)
# 9. Down to (20, 17)

actions = [
    "Up",
    "Right", "Right", "Right", "Right", "Right",
    "Down", "Down", "Down", "Down",
    "Right", "Right",
    "Down", "Down", "Down",
    "Left", "Left", "Left", "Left",
    "Down",
    "Left",
    "Down", "Down"
]

print("Executing moves to reach the balcony gate...")
mgba.press_buttons(actions)
time.sleep(0.5)

# Take screenshot to verify
scr = mgba.take_screenshot()
coords = mgba.get_coordinates()
print(f"Current coordinates: {coords}")
print(f"Screenshot saved to: {scr}")
