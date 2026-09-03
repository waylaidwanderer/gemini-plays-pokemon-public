import mgba
import os

TOTAL_BUTTONS = 0
MAX_SCRIPT_BUTTONS = 80

def get_budget_remaining():
    global TOTAL_BUTTONS, MAX_SCRIPT_BUTTONS
    return max(0, MAX_SCRIPT_BUTTONS - TOTAL_BUTTONS)

def press_safe(buttons):
    global TOTAL_BUTTONS, MAX_SCRIPT_BUTTONS
    if not buttons:
        return
    # Count real button actions (excluding sleep)
    btn_count = sum(1 for b in buttons if not b.startswith("sleep"))
    if TOTAL_BUTTONS + btn_count > MAX_SCRIPT_BUTTONS:
        allowed = MAX_SCRIPT_BUTTONS - TOTAL_BUTTONS
        if allowed <= 0:
            return
        # truncate
        valid_buttons = []
        c = 0
        for b in buttons:
            if not b.startswith("sleep"):
                if c >= allowed:
                    break
                c += 1
            valid_buttons.append(b)
        mgba.press_buttons(valid_buttons)
        TOTAL_BUTTONS += c
    else:
        mgba.press_buttons(buttons)
        TOTAL_BUTTONS += btn_count

def cleanup_screenshots():
    if os.path.exists("screenshots"):
        for f in os.listdir("screenshots"):
            if f.startswith("screenshot_") and f.endswith(".png"):
                try:
                    os.remove(os.path.join("screenshots", f))
                except Exception:
                    pass

def escape_battle():
    if get_budget_remaining() < 10:
        return
    for _ in range(3):
        press_safe(["B", "sleep 120"])
    press_safe(["Down", "Right", "A", "sleep 350"])
    for _ in range(3):
        press_safe(["B", "sleep 120"])

def safe_walk(path, max_buttons=40):
    executed_steps = []
    
    for d in path:
        if get_budget_remaining() <= 0:
            print(f"Global budget exhausted ({TOTAL_BUTTONS}/{MAX_SCRIPT_BUTTONS}), stopping safely.")
            break
            
        old_pos = mgba.get_coordinates()
        press_safe([d, "sleep 180"])
        new_pos = mgba.get_coordinates()
        
        if old_pos == new_pos:
            escape_battle()
            # Retry step after battle escape
            old_pos = mgba.get_coordinates()
            press_safe([d, "sleep 180"])
            new_pos = mgba.get_coordinates()
            if old_pos == new_pos:
                print(f"Physically blocked moving {d} at {old_pos}")
                break
                
        executed_steps.append((d, new_pos))
        
    return mgba.get_coordinates(), TOTAL_BUTTONS
