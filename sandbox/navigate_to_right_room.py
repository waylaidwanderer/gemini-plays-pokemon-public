import mgba
import time

def print_pos(label):
    time.sleep(0.1)
    print(f"{label}: {mgba.get_coordinates()}")

# Start
print_pos("Start at B3F")

# 1. Walk Right to (10, 11)
mgba.press_buttons(["Right", "Right"])
time.sleep(0.5)
print_pos("At (10, 11)")

# 2. Walk Up onto UP spinner at (10, 10) -> spins to (10, 9)
mgba.press_buttons(["Up"])
time.sleep(1.0)
print_pos("After spinning to row 9")

# 3. Walk Left to (9, 9)
mgba.press_buttons(["Left"])
time.sleep(0.3)
print_pos("At (9, 9)")

# 4. Walk Left onto LEFT spinner at (8, 9) -> spins to (2, 9)
mgba.press_buttons(["Left"])
time.sleep(2.0)
print_pos("After spinning to left side stopper (2, 9)")

# 5. Walk Up to (2, 7)
mgba.press_buttons(["Up", "Up"])
time.sleep(0.5)
print_pos("At (2, 7)")

# 6. Walk Right to (5, 7)
mgba.press_buttons(["Right", "Right", "Right"])
time.sleep(0.5)
print_pos("At (5, 7)")

# 7. Walk Down to (5, 9)
mgba.press_buttons(["Down", "Down"])
time.sleep(0.5)
print_pos("At (5, 9)")

# 8. Walk Right to (7, 9)
mgba.press_buttons(["Right", "Right"])
time.sleep(0.5)
print_pos("At (7, 9)")

# 9. Walk Up to (7, 7)
mgba.press_buttons(["Up", "Up"])
time.sleep(0.5)
print_pos("At (7, 7)")

# 10. Walk Right to (13, 7)
mgba.press_buttons(["Right", "Right", "Right", "Right", "Right", "Right"])
time.sleep(0.8)
print_pos("At (13, 7)")

# 11. Walk Down onto DOWN spinner at (13, 10) -> spins DOWN to (13, 12), then Right to (14, 12)
mgba.press_buttons(["Down", "Down", "Down"])
time.sleep(2.0)
print_pos("After spinning to (14, 12)")

# 12. Walk Up to (14, 10)
mgba.press_buttons(["Up", "Up"])
time.sleep(0.5)
print_pos("At (14, 10)")

# 13. Walk Right to (19, 10)
mgba.press_buttons(["Right", "Right", "Right", "Right", "Right"])
time.sleep(0.8)
print_pos("At (19, 10) inside right room")

