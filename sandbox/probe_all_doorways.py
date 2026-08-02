import mgba
import time

print("Starting Master Route 8 Doorway Probe...")

pos = mgba.get_coordinates()
print(f"Starting position: {pos}")

# Walk West along Row 20 to Column 13
# Current position: (19, 18)
# Step Down 2 to (19, 20), then Left 6 to (13, 20)
seq1 = ["Down", "Down", "Left", "Left", "Left", "Left", "Left", "Left", "sleep 300"]
mgba.press_buttons(seq1)

pos = mgba.get_coordinates()
print(f"Position after moving to (13, 20): {pos}")

s1 = mgba.take_screenshot()
print(f"Screenshot at (13, 20): {s1}")

# Walk Up to Row 15 to check (13, 15) doorway
seq2 = ["Up", "Up", "Up", "Up", "Up", "sleep 300"]
mgba.press_buttons(seq2)

pos = mgba.get_coordinates()
print(f"Position at doorway check: {pos}")

s2 = mgba.take_screenshot()
print(f"Screenshot at doorway: {s2}")
