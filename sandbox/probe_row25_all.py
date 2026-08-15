import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    # Try to RUN
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    return get_pos()

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
    bridge.press_buttons([direction, "sleep 450"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    if new_pos != pos:
        return new_pos
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    if new_pos != pos:
        return new_pos
    return handle_textbox_or_battle()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
            continue
        if pos == (tx, ty):
            break
        if pos[0] < tx:
            direction = "Right"
        elif pos[0] > tx:
            direction = "Left"
        elif pos[1] < ty:
            direction = "Down"
        elif pos[1] > ty:
            direction = "Up"
        new_pos = walk_step_robust(direction)
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                bridge.press_buttons(["B", "sleep 500"])
                stuck_count = 0
        else:
            stuck_count = 0
        time.sleep(0.4)

def try_move(direction):
    pos = get_pos()
    new_pos = walk_step_robust(direction)
    if new_pos == pos:
        return False, new_pos
    return True, new_pos

def main():
    print("PROBING ROW 25 FOR GAPS FROM COLUMN 20 DOWN TO 0...")
    gaps = []
    # Currently we are at (20, 24).
    # We will walk left along Row 24 to Column 0, and at each column, we try to walk DOWN.
    for col in range(20, -1, -1):
        print(f"Navigating to ({col}, 24)...")
        navigate_to(col, 24)
        current = get_pos()
        if current is None:
            current = handle_textbox_or_battle()
        if current[0] != col or current[1] != 24:
            print(f"Could not reach ({col}, 24), we are at {current}")
            continue
            
        print(f"Probing DOWN at ({col}, 24)...")
        success, new_p = try_move("Down")
        if success:
            print(f"!!! GAP FOUND AT COLUMN {col}! Walked to {new_p}")
            gaps.append(col)
            # Walk back up to Row 24
            walk_step_robust("Up")
        else:
            print(f"Column {col} is BLOCKED")
            
    print(f"PROBING COMPLETE. Gaps found at columns: {gaps}")

if __name__ == "__main__":
    main()
