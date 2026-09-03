import mgba

TOTAL_BUTTONS = 0
HARD_LIMIT = 50

def reset_budget():
    global TOTAL_BUTTONS
    TOTAL_BUTTONS = 0

def get_budget():
    global TOTAL_BUTTONS, HARD_LIMIT
    return HARD_LIMIT - TOTAL_BUTTONS

def press_counted(btn_list):
    global TOTAL_BUTTONS, HARD_LIMIT
    to_send = []
    for b in btn_list:
        if not b.startswith("sleep"):
            if TOTAL_BUTTONS >= HARD_LIMIT:
                break
            TOTAL_BUTTONS += 1
        to_send.append(b)
    if to_send:
        mgba.press_buttons(to_send)

def activate_strength():
    press_counted(["Start", "sleep 200", "Down", "sleep 100", "A", "sleep 300", "Down", "sleep 100", "Down", "sleep 100", "A", "sleep 200", "A", "sleep 400", "B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])

def escape_battle():
    press_counted(["B", "sleep 150", "Down", "Right", "A", "sleep 350", "B", "sleep 150", "B", "sleep 150"])

def safe_step(d):
    global TOTAL_BUTTONS, HARD_LIMIT
    if TOTAL_BUTTONS >= HARD_LIMIT:
        return mgba.get_coordinates()
    old_pos = mgba.get_coordinates()
    press_counted([d, "sleep 200"])
    new_pos = mgba.get_coordinates()
    
    if old_pos == new_pos:
        escape_battle()
        if TOTAL_BUTTONS < HARD_LIMIT:
            old_pos = mgba.get_coordinates()
            press_counted([d, "sleep 200"])
            new_pos = mgba.get_coordinates()
            if old_pos == new_pos:
                print(f"Blocked moving {d} at {old_pos}")
                return new_pos
                
    print(f"Step {d}: {old_pos} -> {new_pos} (used {TOTAL_BUTTONS}/{HARD_LIMIT})")
    return new_pos

def walk_path(path):
    reset_budget()
    for d in path:
        if TOTAL_BUTTONS >= HARD_LIMIT:
            print(f"Hard limit reached ({TOTAL_BUTTONS}/{HARD_LIMIT}), pausing cleanly.")
            break
        safe_step(d)
    return mgba.get_coordinates()
