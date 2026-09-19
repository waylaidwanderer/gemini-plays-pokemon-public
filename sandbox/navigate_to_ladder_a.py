import mgba
import time

def flee_battle():
    # If in wild battle, flee cleanly
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
    max_steps = 35
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

# Segment 1: (21, 4) -> (22, 4) -> (22, 2) -> (21, 2) -> (21, 1) -> (21, 0)
walk_to_target(22, 4)
walk_to_target(22, 2)
walk_to_target(21, 2)
walk_to_target(21, 0)

# Segment 2: Walk East along Row 0 to (24, 0) -> (27, 0) -> (29, 0)
walk_to_target(24, 0)
walk_to_target(27, 0)
walk_to_target(29, 0)

# Segment 3: Ascend down Eastern Corridor (29, 0) -> (29, 6) -> (27, 6) -> (25, 7) -> (29, 8)
walk_to_target(29, 6)
walk_to_target(27, 6)
walk_to_target(27, 7)
walk_to_target(25, 7)
walk_to_target(29, 8)

print("Pos after reaching Eastern Corridor (29, 8):", mgba.get_coordinates())
