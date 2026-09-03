import mgba

class CollisionError(Exception):
    pass

def get_pos():
    return mgba.get_coordinates()

def handle_battle():
    # Advance battle text and escape
    mgba.press_buttons([
        "B", "sleep 200", "B", "sleep 200",
        "Down", "sleep 100", "Right", "sleep 100",
        "A", "sleep 350", "B", "sleep 200", "B", "sleep 200"
    ])

def step(d, raise_on_blocked=True):
    old_pos = get_pos()
    mgba.press_buttons([d, "sleep 220"])
    new_pos = get_pos()
    if old_pos == new_pos:
        handle_battle()
        new_pos = get_pos()
        if old_pos == new_pos:
            if raise_on_blocked:
                raise CollisionError(f"Blocked moving {d} at {old_pos}")
            return False, new_pos
    print(f"Step {d}: {old_pos} -> {new_pos}")
    return True, new_pos

def walk(directions):
    for d in directions:
        success, _ = step(d, raise_on_blocked=True)
    return get_pos()
