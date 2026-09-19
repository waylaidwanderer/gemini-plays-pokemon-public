import mgba
import time

def flee_battle():
    # Down -> Right -> A, wait, B, B
    print("Wild battle encountered! Escaping...")
    mgba.press_buttons([
        "Down", "sleep 150",
        "Right", "sleep 150",
        "A", "sleep 1500",
        "B", "sleep 300",
        "B", "sleep 300"
    ])

def step(d):
    before = mgba.get_coordinates()
    mgba.press_buttons([d, "sleep 300"])
    after = mgba.get_coordinates()
    if before == after:
        flee_battle()
        after = mgba.get_coordinates()
    print(f"Step {d}: {before} -> {after}")
    return after

def walk_to_target(target_x, target_y):
    max_steps = 30
    for _ in range(max_steps):
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        if cx == target_x and cy == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
        if cx < target_x:
            step("Right")
        elif cx > target_x:
            step("Left")
        elif cy < target_y:
            step("Down")
        elif cy > target_y:
            step("Up")
    return False

print("Starting route to Ladder A from:", mgba.get_coordinates())

# Segment 1: (5, 3) -> (9, 3) -> (9, 5) -> (13, 5) -> (13, 6) -> (13, 8) -> (13, 9)
walk_to_target(9, 3)
walk_to_target(9, 5)
walk_to_target(13, 5)
walk_to_target(13, 6)
walk_to_target(13, 8)
walk_to_target(13, 9)

# Segment 2: (13, 9) -> (0, 9)
walk_to_target(0, 9)

# Segment 3: (0, 9) -> (0, 3)
walk_to_target(0, 3)

# Segment 4: Step Right onto Ladder A at (1, 3)!
step("Right")

print("Final position:", mgba.get_coordinates())
