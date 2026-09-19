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

print("Starting route to Ladder A from:", mgba.get_coordinates())

# Segment 1: (24, 4) -> (24, 2) -> (22, 2) -> (22, 4) -> (21, 4) -> (21, 5) -> (20, 5) -> (20, 6) -> (22, 7) -> (22, 8) -> (27, 8)
walk_to_target(24, 2)
walk_to_target(22, 2)
walk_to_target(22, 4)
walk_to_target(21, 4)
walk_to_target(21, 5)
walk_to_target(20, 5)
walk_to_target(20, 6)
walk_to_target(22, 7)
walk_to_target(22, 8)
walk_to_target(27, 8)

print("Pos after reaching Eastern Corridor (27, 8):", mgba.get_coordinates())
