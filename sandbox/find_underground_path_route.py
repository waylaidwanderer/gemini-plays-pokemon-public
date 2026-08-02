import mgba
import time

print("Starting Master Route 8 Underground Path Search...")

pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

# Target 1: Walk to Col 9 (9, 16) -> Up to (9, 12)
# From (13, 16): Left 4 to (9, 16), then Up 4 to (9, 12)
seq1 = ["Left", "Left", "Left", "Left", "Up", "Up", "Up", "Up", "sleep 500"]
mgba.press_buttons(seq1)

pos1 = mgba.get_coordinates()
print(f"Pos after moving to (9, 12): {pos1}")
s1 = mgba.take_screenshot()
print(f"Screenshot 1: {s1}")

# Try stepping Up into (9, 11) doorway
mgba.press_buttons(["Up", "sleep 1000"])
pos_door = mgba.get_coordinates()
print(f"Pos after stepping Up into (9, 11): {pos_door}")

s_door = mgba.take_screenshot()
print(f"Screenshot door check: {s_door}")
