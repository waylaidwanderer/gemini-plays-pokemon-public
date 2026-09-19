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
    max_steps = 25
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

print("Starting direct path to Ladder A from:", mgba.get_coordinates())

# Segment 1: (16, 5) -> (13, 5) -> (13, 6)
walk_to_target(13, 5)
walk_to_target(13, 6)

# Segment 2: (13, 6) -> (12, 6) -> (11, 7) -> (6, 7)
walk_to_target(12, 6)
walk_to_target(11, 7)
walk_to_target(6, 7)

# Segment 3: (6, 7) -> (6, 6) -> (6, 5)
walk_to_target(6, 6)
walk_to_target(6, 5)

# Segment 4: (6, 5) -> (0, 5) -> (0, 3)
walk_to_target(0, 5)
walk_to_target(0, 3)

# Segment 5: Step Right onto Ladder A at (1, 3)!
step("Right")

print("Final position:", mgba.get_coordinates())
