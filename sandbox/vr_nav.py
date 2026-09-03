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

def walk(directions):
    for d in directions:
        success, pos = step(d)
        if not success:
            print(f"Walk stopped at {pos}")
            return False, pos
    return True, get_pos()
