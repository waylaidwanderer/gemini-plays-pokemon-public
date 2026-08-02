import mgba
import time

print("Starting Western Gatehouse & Route 8 Complete Doorway Search...")

pos = mgba.get_coordinates()
print(f"Current Position on Route 8: {pos}")

# Walk from (14, 17) to Cut tree gap at (5, 8) -> enter Western Gatehouse map
# Path: Up 5 to (14, 12) -> Left 1 to (13, 12) -> Left 3 to (10, 12) -> Up 4 through Col 12 gap to (6, 8) -> Left 7 to (-1, 8) / (39, 16)
seq_to_west = [
    "Up", "Up", "Up", "Up", "Up",
    "Left", "Left", "Left", "Left",
    "Up", "Up", "Up", "Up",
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "sleep 1000"
]

mgba.press_buttons(seq_to_west)

pos_w = mgba.get_coordinates()
print(f"Position after entering Western Gatehouse map: {pos_w}")
s_w = mgba.take_screenshot()
print(f"Western Gatehouse map screenshot: {s_w}")

# Let's test probing candidate doorway coordinates on Western Gatehouse map:
# Candidate 1: Col 25 Row 20 / Row 25
# Candidate 2: Col 35 Row 19
# Candidate 3: Col 20 Row 20
