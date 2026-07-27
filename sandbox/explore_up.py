import mgba

print("Walking Left and Up to explore...")
# From (25, 8):
# Left 2 times to (23, 8)
# Up 4 times to (23, 4)
mgba.press_buttons(["Left", "Left", "Up", "Up", "Up", "Up"])

pos = mgba.get_coordinates()
print(f"Current position: {pos}")
screenshot = mgba.take_screenshot()
print(f"Captured screenshot: {screenshot}")
