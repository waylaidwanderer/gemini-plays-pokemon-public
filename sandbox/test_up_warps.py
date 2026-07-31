import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.1)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.1)
        p2 = mgba.get_coordinates()
    return p1

# We are at B3F (2, 9)
print("Start Position:", mgba.get_coordinates())

# Walk to (19, 14)
print("Walking to (19, 14)...")
# Path from (2, 9) to (19, 14):
# Right 1, Down 4 to (3, 13)
# Right 1, Down 2 to (4, 15) -> spins to (8, 11)
# Right 2, Down 3 to (10, 14)
# Left 1 (spins to 9, 16)
# Right 2 (spins to 15, 17)
# Left 1 (spins to 14, 15)
# Right 1, Up 1 to (15, 14)
# Right 1 (spins to 16, 13)
# Right 3, Down 1 to (19, 14)
buttons = [
    "Right", "Down", "Down", "Down", "Down",
    "Right", "Down", "Down", # spins to (8, 11)
    "Right", "Right", "Down", "Down", "Down",
    "Left", # spins to (9, 16)
    "Right", "Right", # spins to (15, 17)
    "Left", # spins to (14, 15)
    "Right", "Up",
    "Right", # spins to (16, 13)
    "Right", "Right", "Right", "Down"
]

mgba.press_buttons(buttons)
pos = wait_for_movement()
print(f"Landed at: {pos}")

# Now we are at (19, 14). Let's walk UP 1 step to (19, 13)
print("Walking UP to (19, 13) to trigger warp...")
mgba.press_buttons(["Up"])
time.sleep(1.0)
pos = wait_for_movement()
print(f"Position: {pos}")

# If we didn't warp, walk Down to (19, 14), Right to (20, 14), and Up to (20, 13)
if pos['y'] == 13:
    print("Walking to (20, 14)...")
    mgba.press_buttons(["Down", "Right"])
    wait_for_movement()
    print("Walking UP to (20, 13) to trigger warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    pos = wait_for_movement()
    print(f"Position: {pos}")
