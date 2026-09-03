import mgba
import os

def cleanup_screenshots():
    if os.path.exists("screenshots"):
        for f in os.listdir("screenshots"):
            if f.startswith("screenshot_") and f.endswith(".png"):
                try:
                    os.remove(os.path.join("screenshots", f))
                except Exception:
                    pass

def escape_battle():
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 120"])
    mgba.press_buttons(["Down", "Right", "A", "sleep 350"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 120"])

def safe_walk(path, max_buttons=40):
    button_count = 0
    executed_steps = []
    
    for d in path:
        if button_count + 12 > max_buttons:
            print(f"Approaching budget ({button_count}/{max_buttons}), stopping safely.")
            break
            
        old_pos = mgba.get_coordinates()
        mgba.press_buttons([d, "sleep 180"])
        button_count += 1
        new_pos = mgba.get_coordinates()
        
        if old_pos == new_pos:
            escape_battle()
            button_count += 9
            # Retry step after battle escape
            old_pos = mgba.get_coordinates()
            mgba.press_buttons([d, "sleep 180"])
            button_count += 1
            new_pos = mgba.get_coordinates()
            if old_pos == new_pos:
                print(f"Physically blocked moving {d} at {old_pos}")
                break
                
        executed_steps.append((d, new_pos))
        
    return mgba.get_coordinates(), button_count
