import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    # Progress text/dialog with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 200"])
    return get_pos()

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
    bridge.press_buttons([direction, "sleep 450"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    return new_pos

def main():
    pos = get_pos()
    print(f"Starting exhaust_steps run from: {pos}")
    
    # We want to do exactly 80 steps of back-and-forth walking
    # Row 24 between Column 19 and 21.
    for i in range(40):
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            
        # Check if warped to Gatehouse
        if pos is not None and pos[0] < 10 and pos[1] < 10:
            print(f"Warp detected during loop! Position: {pos}")
            break
            
        # Walk Left to (19, 24)
        while pos is not None and pos[0] > 19:
            pos = walk_step_robust("Left")
            if pos is None:
                pos = handle_textbox_or_battle()
                
        # Check warp again
        if pos is not None and pos[0] < 10 and pos[1] < 10:
            print(f"Warp detected during loop! Position: {pos}")
            break
            
        # Walk Right to (21, 24)
        while pos is not None and pos[0] < 21:
            pos = walk_step_robust("Right")
            if pos is None:
                pos = handle_textbox_or_battle()
                
        if i % 10 == 0:
            print(f"Loop {i}: Current Position: {pos}")
            
    pos = get_pos()
    print(f"End of exhaust_steps run. Current Position: {pos}")
    
    img = mgba.take_screenshot()
    print(f"Screenshot: {img}")

if __name__ == "__main__":
    main()
