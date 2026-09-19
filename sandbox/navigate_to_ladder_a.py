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

def walk_to(target_x, target_y):
    max_steps = 20
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

print("Starting from:", mgba.get_coordinates())

# Waypoint 1: (16, 3) -> (16, 5)
walk_to(16, 3)
walk_to(16, 5)

# Waypoint 2: (9, 5)
walk_to(9, 5)

# Waypoint 3: (9, 3)
walk_to(9, 3)

# Waypoint 4: (5, 3)
walk_to(5, 3)

# Waypoint 5: (5, 5)
walk_to(5, 5)

# Waypoint 6: (0, 5)
walk_to(0, 5)

# Waypoint 7: (0, 3)
walk_to(0, 3)

# Waypoint 8: Step Right onto Ladder A at (1, 3)
step("Right")

print("Final position:", mgba.get_coordinates())
