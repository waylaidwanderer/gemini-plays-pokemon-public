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

def walk_to(target_x, target_y):
    max_steps = 30
    for _ in range(max_steps):
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        if cx == target_x and cy == target_y:
            print(f"Arrived at ({target_x}, {target_y})")
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

# Starting at (16, 7)
print("Starting pos:", mgba.get_coordinates())

# Segment 1: (16, 7) -> (16, 5)
walk_to(16, 5)

# Segment 2: (16, 5) -> (21, 5)
# Note: (17, 5) and (18, 5) are rock! Must go via (16, 3) or (16, 6) -> (19, 6) -> (19, 5)!
# Let's check: (16, 5) -> (16, 3) -> (18, 3) -> (19, 3) -> (20, 3) -> (20, 5) -> (21, 5)
walk_to(16, 3)
walk_to(20, 3)
walk_to(20, 5)
walk_to(21, 5)

print("Pos after reaching (21, 5):", mgba.get_coordinates())
