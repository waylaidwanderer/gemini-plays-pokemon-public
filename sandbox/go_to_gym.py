import mgba
from PIL import Image

# Start from (23, 26)
# Walk right to column 27, then walk up
actions = ["Right", "Right", "Right", "Right"]
for _ in range(20):
    actions.append("Up")

mgba.press_buttons(actions)
pos = mgba.get_coordinates()
print(f"Ended at position: {pos}")
screenshot = mgba.take_screenshot()
print(f"Screenshot saved to: {screenshot}")
