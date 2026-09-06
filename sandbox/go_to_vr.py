import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    return p['x'], p['y']

def press(buttons):
    mgba.press_buttons(buttons)

def escape_battle():
    # Dismiss any text and try to run
    press(["B", "sleep 150", "B", "sleep 150", "A", "sleep 150", "B", "sleep 150"])
    press(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 400", "B", "sleep 200", "B", "sleep 150"])

def step_dir(d):
    ox, oy = get_pos()
    press([d, "sleep 180"])
    nx, ny = get_pos()
    if (nx, ny) == (ox, oy):
        # Could be battle, dialogue, or wall
        escape_battle()
        nx, ny = get_pos()
    return nx, ny

def walk_to(tx, ty, max_steps=60):
    steps = 0
    while steps < max_steps:
        x, y = get_pos()
        if x == tx and y == ty:
            return True
        if x < tx:
            d = "Right"
        elif x > tx:
            d = "Left"
        elif y < ty:
            d = "Down"
        elif y > ty:
            d = "Up"
        step_dir(d)
        steps += 1
    return False

def route22_to_gate():
    # Route 22 path from (39, 6):
    # From (39, 6) -> walk south to (33, 12)? Wait, let's look at Route 22 layout
    print("Navigating Route 22 from", get_pos())
    # Canonical route:
    # 1. From (39, 6..9) -> (33, 12)
    # (39, 6) -> Down to (39, 9) -> Left to (33, 9) -> Down to (33, 12)
    walk_to(39, 9)
    walk_to(33, 9)
    walk_to(33, 12)
    walk_to(31, 12)
    # North through tall grass
    walk_to(31, 8)
    walk_to(31, 5) # Upper highway
    walk_to(16, 5)
    # Hop ledge south
    walk_to(16, 7)
    step_dir("Down") # Hop ledge to row 8
    walk_to(16, 12)
    walk_to(5, 12)
    walk_to(5, 10)
    walk_to(11, 10)
    walk_to(11, 6)
    walk_to(8, 6)
    # Step into gatehouse
    press(["Up", "sleep 400", "Up", "sleep 400"])
    print("Entered gatehouse, pos:", get_pos())

if __name__ == "__main__":
    route22_to_gate()
