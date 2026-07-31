import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.12)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.12)
        p2 = mgba.get_coordinates()
    return p1

def try_move(direction):
    p_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.2)
    p_after = wait_for_movement()
    if p_before != p_after:
        return p_after
    return None

# We are currently at B3F (21, 7)
print("Start Position:", mgba.get_coordinates())

# Let's explore the walkable coordinates using a simple flood fill / DFS in Python
visited = set()
queue = [mgba.get_coordinates()]
parent = {}

# Since we don't want to spin out of control on a spinner, let's only step onto normal tiles.
# But we can also just walk around and print what is adjacent to our current position.
# Let's do a safe 4-direction check around our current position (21, 7)
print("Adjacent check from (21, 7):")
for d in ["Up", "Down", "Left", "Right"]:
    p = try_move(d)
    if p:
        print(f"Can go {d} -> {p}")
        # walk back
        opp = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
        try_move(opp)
    else:
        print(f"Blocked {d}")

