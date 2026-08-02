import mgba
import time

print("Starting Western Gatehouse & Route 8 Complete Doorway Search...")

pos = mgba.get_coordinates()
print(f"Current Position on Route 8: {pos}")

# Step 1: Walk from (8, 16) -> Down 2 to (8, 18) -> Left 6 to (2, 18) -> Up 10 to (2, 8) -> Left 6 through Cut tree gap at (5, 8) to (-1, 8) / (39, 16) on Western Gatehouse Map
seq_to_west = [
    "Down", "Down",
    "Left", "Left", "Left", "Left", "Left", "Left",
    "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
    "Left", "Left", "Left", "Left", "Left", "Left", "sleep 1000"
]

mgba.press_buttons(seq_to_west)

pos_w = mgba.get_coordinates()
print(f"Position after entering Western Gatehouse map: {pos_w}")
s_w = mgba.take_screenshot()
print(f"Western Gatehouse map screenshot: {s_w}")

# Now on Western Gatehouse Map (around 39, 16 or 32, 16)
# Let's explore West along Row 16 / Row 21 to Col 25, Col 20, Col 15, Col 10, Col 5!
# Candidate 1: Col 25 Row 20 / Row 25
# Candidate 2: Col 35 Row 19
# Candidate 3: Col 20 Row 20
