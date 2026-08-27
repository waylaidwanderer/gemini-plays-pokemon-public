import mgba
import time

# Ensure we start fresh
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print(f"Initial position: {pos}")

# We are at (1, 12). Let's try to walk UP to (1, 11)
mgba.press_buttons(["Up"])
time.sleep(0.5)
pos = mgba.get_coordinates()
print(f"After Up: {pos}")

# Let's try to walk UP to (1, 10)
mgba.press_buttons(["Up"])
time.sleep(0.5)
pos = mgba.get_coordinates()
print(f"After Up Up: {pos}")

# Let's try to walk UP to (1, 9)
mgba.press_buttons(["Up"])
time.sleep(0.5)
pos = mgba.get_coordinates()
print(f"After Up Up Up: {pos}")

# Let's try to walk UP to (1, 8)
mgba.press_buttons(["Up"])
time.sleep(0.5)
pos = mgba.get_coordinates()
print(f"After Up Up Up Up: {pos}")

# Let's walk back down to (1, 11) or (1, 12) to be safe
pos = mgba.get_coordinates()
if pos["y"] < 11:
    print("Walking back down to Row 11...")
    for y in range(pos["y"], 11):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        
print("Final position:", mgba.get_coordinates())
