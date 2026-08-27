import mgba
import time

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting search at:", pos)

# We want to explore walkable tiles around (18, 6).
# Let's try walking in various directions and logging where we succeed.
def try_move(direction, expected):
    mgba.press_buttons([direction])
    time.sleep(0.4)
    p = mgba.get_coordinates()
    if p == expected:
        # success, walk back
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([opposite])
        time.sleep(0.4)
        return True
    return False

print("At (18, 6):")
print("  Up to (18, 5):", try_move("Up", {"x": 18, "y": 5}))
print("  Down to (18, 7):", try_move("Down", {"x": 18, "y": 7}))
print("  Left to (17, 6):", try_move("Left", {"x": 17, "y": 6}))
print("  Right to (19, 6):", try_move("Right", {"x": 19, "y": 6}))

# Let's walk to (19, 6) if possible
if walk_step := try_move("Right", {"x": 19, "y": 6}):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    print("Moved to (19, 6). Testing from (19, 6):")
    print("  Down to (19, 7):", try_move("Down", {"x": 19, "y": 7}))
    print("  Right to (20, 6):", try_move("Right", {"x": 20, "y": 6}))
    # Walk back to (18, 6)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)

# Let's walk to (17, 6) if possible
if walk_step := try_move("Left", {"x": 17, "y": 6}):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Moved to (17, 6). Testing from (17, 6):")
    print("  Down to (17, 7):", try_move("Down", {"x": 17, "y": 7}))
    print("  Left to (16, 6):", try_move("Left", {"x": 16, "y": 6}))
    # Walk back to (18, 6)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)

print("Exploration finished.")
