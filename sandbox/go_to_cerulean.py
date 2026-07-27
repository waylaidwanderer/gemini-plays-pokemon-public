import mgba

print("Walking back to Cerulean City...")
# From (25, 6):
# Left 2 times to (23, 6)
# Down 2 times to (23, 8)
# Left 23 times to (0, 8) to transition to Cerulean City
mgba.press_buttons(["Left", "Left", "Down", "Down"] + ["Left"] * 23)

pos = mgba.get_coordinates()
print(f"Current position: {pos}")
screenshot = mgba.take_screenshot()
print(f"Captured screenshot: {screenshot}")
