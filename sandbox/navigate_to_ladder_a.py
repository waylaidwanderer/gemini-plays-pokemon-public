import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
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

print("Starting route from:", mgba.get_coordinates())

# Waypoint 1: (9, 3)
walk_to_target(9, 3)

# Waypoint 2: (9, 5)
walk_to_target(9, 5)

# Waypoint 3: (13, 5) -> (13, 6) -> (12, 6)
walk_to_target(13, 5)
walk_to_target(13, 6)
walk_to_target(12, 6)

print("Pos after reaching (12, 6):", mgba.get_coordinates())
