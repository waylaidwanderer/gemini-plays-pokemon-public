import mgba
import os

TOTAL_BUTTONS = 0
HARD_LIMIT = 40

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

def escape_battle_strict():
    global TOTAL_BUTTONS, HARD_LIMIT
    if TOTAL_BUTTONS >= HARD_LIMIT - 6:
        return
    press_counted(["B", "sleep 120", "B", "sleep 120"])
    press_counted(["Down", "Right", "A", "sleep 350"])
    press_counted(["B", "sleep 120", "B", "sleep 120"])

def step(d):
    global TOTAL_BUTTONS, HARD_LIMIT
    if TOTAL_BUTTONS >= HARD_LIMIT:
        return mgba.get_coordinates()
    old_pos = mgba.get_coordinates()
    press_counted([d, "sleep 180"])
    new_pos = mgba.get_coordinates()
    if old_pos == new_pos:
        escape_battle_strict()
        if TOTAL_BUTTONS < HARD_LIMIT:
            old_pos = mgba.get_coordinates()
            press_counted([d, "sleep 180"])
            new_pos = mgba.get_coordinates()
    print(f"Step {d}: {old_pos} -> {new_pos} (used {TOTAL_BUTTONS}/{HARD_LIMIT})")
    return new_pos

def walk_path(path):
    for d in path:
        if TOTAL_BUTTONS >= HARD_LIMIT:
            print(f"Hard limit reached ({TOTAL_BUTTONS}/{HARD_LIMIT}), pausing cleanly.")
            break
        step(d)
    return mgba.get_coordinates()
