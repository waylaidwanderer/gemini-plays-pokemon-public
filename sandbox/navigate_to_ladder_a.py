import mgba
import time

def flee_battle():
    # If a wild battle triggers, select RUN
    print("Wild encounter! Escaping...")
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
            print(f"Arrived at waypoint ({target_x}, {target_y})")
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

# Waypoint 1: (16, 5)
walk_to_target(16, 5)

# Waypoint 2: (16, 7)
walk_to_target(16, 7)

# Waypoint 3: (18, 7)
walk_to_target(18, 7)

# Waypoint 4: (18, 9)
walk_to_target(18, 9)

print("Pos at Row 9 highway entrance:", mgba.get_coordinates())
