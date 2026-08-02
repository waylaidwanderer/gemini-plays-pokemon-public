import mgba
import time

print("Starting Western Gatehouse Map Exhaustive Doorway Probe...")

pos = mgba.get_coordinates()
print(f"Current Position: {pos}")

# Step 1: Walk from (9, 16) to (13, 16) -> (13, 12) -> (6, 8) -> (5, 8) Cut tree gap into Western Gatehouse map
seq_to_west = [
    "Right", "Right", "Right", "Right",
    "Up", "Up", "Up", "Up",
    "Left", "Left", "Left",
    "Up", "Up", "Up", "Up",
    "Left", "Left", "Left", "Left", "Left", "Left", "sleep 1000"
]
mgba.press_buttons(seq_to_west)

pos_west = mgba.get_coordinates()
print(f"Position after entering Western Gatehouse map: {pos_west}")
s_west = mgba.take_screenshot()
print(f"Western Gatehouse map screenshot: {s_west}")
