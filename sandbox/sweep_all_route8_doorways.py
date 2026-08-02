import mgba
import time

print("Starting Master Route 8 Overworld Doorway Sweep...")

pos = mgba.get_coordinates()
print(f"Starting position on Route 8 overworld: {pos}")

# We are at (19, 18) on Route 8
# Let's test moving to candidate doorway at (9, 11)
# Route from (19, 18):
# Left 6 to (13, 18) -> Up 6 to (13, 12) -> Left 4 to (9, 12) -> Up 1 to (9, 11)
seq_9_11 = [
    "Left", "Left", "Left", "Left", "Left", "Left",
    "Up", "Up", "Up", "Up", "Up", "Up",
    "Left", "Left", "Left", "Left",
    "Up", "sleep 1000"
]

mgba.press_buttons(seq_9_11)
p1 = mgba.get_coordinates()
print(f"Position after sequence to (9, 11): {p1}")
s1 = mgba.take_screenshot()
print(f"Screenshot at (9, 11) check: {s1}")
