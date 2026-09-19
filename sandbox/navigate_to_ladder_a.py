import mgba
import time

def flee_battle():
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

print("Starting route from:", mgba.get_coordinates())

# Segment 1: (16, 7) -> (16, 5)
walk_to_target(16, 5)

# Segment 2: (16, 5) -> (9, 5)
walk_to_target(9, 5)

# Segment 3: (9, 5) -> (9, 3)
walk_to_target(9, 3)

# Segment 4: (9, 3) -> (3, 3)
walk_to_target(3, 3)

print("Pos at (3, 3):", mgba.get_coordinates())
