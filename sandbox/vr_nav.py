import mgba

def get_pos():
    return mgba.get_coordinates()

def step(d):
    old_pos = get_pos()
    mgba.press_buttons([d, "sleep 180"])
    new_pos = get_pos()
    if old_pos == new_pos:
        print(f"BLOCKED moving {d} at {old_pos}")
        return False, new_pos
    print(f"Step {d}: {old_pos} -> {new_pos}")
    return True, new_pos

def walk_strict(directions):
    for d in directions:
        success, pos = step(d)
        if not success:
            raise RuntimeError(f"Strict navigation failed moving {d} at {pos}")
    return get_pos()

def escape_battle_from_party():
    mgba.press_buttons(["B", "sleep 200", "Down", "sleep 150", "A", "sleep 350", "B", "sleep 200"])
