import mgba
import time

print("Interacting with the switch...")
mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "A", "sleep 500", "A"])
time.sleep(1.0)

coords = mgba.get_coordinates()
print(f"Coords after toggle: {coords}")

screenshot = mgba.take_screenshot()
print(f"Screenshot: {screenshot}")
