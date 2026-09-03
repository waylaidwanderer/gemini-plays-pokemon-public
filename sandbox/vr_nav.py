import mgba

def escape_battle():
    # Deterministic battle escape state machine
    # 1. Dismiss initial encounter / sendout text (press B 3 times)
    mgba.press_buttons(["B", "sleep 120", "B", "sleep 120", "B", "sleep 120"])
    # 2. Select RUN from battle menu (Down, Right, A)
    mgba.press_buttons(["Down", "Right", "A", "sleep 350"])
    # 3. Dismiss 'Got away safely' text (press B 3 times)
    mgba.press_buttons(["B", "sleep 120", "B", "sleep 120", "B", "sleep 120"])

def safe_walk(path, max_buttons=35):
    """Walks a path of directional strings with strict button budgeting and battle detection."""
    button_count = 0
    executed_steps = []
    
    for d in path:
        if button_count + 10 > max_buttons:
            print(f"Stopping early: approaching button budget ({button_count}/{max_buttons})")
            break
            
        old_pos = mgba.get_coordinates()
        mgba.press_buttons([d, "sleep 220"])
        button_count += 1
        new_pos = mgba.get_coordinates()
        
        if old_pos == new_pos:
            # Step didn't move; check if in battle
            escape_battle()
            button_count += 9
            new_pos = mgba.get_coordinates()
            if old_pos == new_pos:
                print(f"Blocked moving {d} at {old_pos}")
                break
                
        executed_steps.append((d, new_pos))
        
    return mgba.get_coordinates(), button_count
