import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_battle_or_text():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    # Check pixels in the text box area at the bottom
    # Text box has white/cream background (247, 231, 214) or (255, 255, 255)
    # The GBC emulator window is 480x432. The text box is at the bottom (y=300 to 420).
    # Let's check multiple points along y=380.
    cream_points = 0
    for x in [100, 240, 380]:
        p = img.getpixel((x, 380))
        # cream/white color
        if p[0] > 230 and p[1] > 210 and p[2] > 190:
            cream_points += 1
    return cream_points == 3

def handle_battle_or_text():
    print("  Battle or Textbox detected! Attempting to clear/flee...")
    time.sleep(1.0)
    # Press A a few times to clear any initial text (like "Wild PONYTA appeared!" or "Go! SHELLBY!")
    for _ in range(5):
        mgba.press_buttons(["A"])
        time.sleep(0.4)
    
    # Try to flee: select RUN in the bottom-right
    # From top-left (FIGHT): Down, Right, A
    print("  Selecting RUN...")
    mgba.press_buttons(["Down"])
    time.sleep(0.15)
    mgba.press_buttons(["Right"])
    time.sleep(0.15)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    # Press B to make sure we clear the "Got away safely!" text
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    if check_battle_or_text():
        print("  Still in battle/textbox! Trying B...")
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        if check_battle_or_text():
            print("  STILL in battle/textbox! Aborting.")
            return False
    return True

def step_with_battle_handling(direction, expected_pos):
    max_retries = 5
    for attempt in range(max_retries):
        start_pos = get_pos()
        print(f"Step: {direction} from {start_pos} to {expected_pos} (Attempt {attempt+1})")
        mgba.press_buttons([direction])
        
        start_wait = time.time()
        is_battle = False
        while (time.time() - start_wait) < 5.0:
            if check_battle_or_text():
                is_battle = True
                break
            pos = get_pos()
            if pos != start_pos:
                time.sleep(0.5) # Wait for screen to stabilize
                if check_battle_or_text():
                    is_battle = True
                    break
                final_pos = get_pos()
                if final_pos == expected_pos:
                    print(f"  Successfully reached {final_pos}")
                    return True
                else:
                    print(f"  Derailed! Spun/Redirected to {final_pos}")
                    return False
            time.sleep(0.1)
            
        if is_battle:
            if handle_battle_or_text():
                print("  Successfully fled from battle!")
                after_pos = get_pos()
                if after_pos == expected_pos:
                    print(f"  Arrived at {expected_pos} after battle.")
                    return True
                elif after_pos == start_pos:
                    print("  Returned to start position after battle. Retrying...")
                    time.sleep(0.5)
                    continue
                else:
                    print(f"  Derailed to {after_pos} after battle!")
                    return False
            else:
                print("  Failed to handle battle!")
                return False
                
        print("  Step timed out or blocked!")
        return False
    print("  Max retries exceeded!")
    return False

# Plan from current position (23, 5)
path = [
    ("Right", (24, 5)),
    ("Right", (25, 5)),
    ("Right", (26, 5)),
    ("Up", (26, 4)),
    ("Up", (26, 3)),
    ("Up", (26, 2)),
    ("Up", (26, 1)),
    ("Left", (25, 1)),
    ("Left", (24, 1)),
    ("Left", (23, 1)),
    ("Left", (22, 1)),
    ("Left", (21, 1)),
    ("Down", (21, 2)),
    ("Down", (21, 3)),
    ("Down", (21, 4)),
    ("Down", (21, 5)),
    ("Right", (22, 5))
]

print("Starting automated escape from B1F East...")
success = True
for direction, target in path:
    curr = get_pos()
    if curr == target:
        print(f"Already at target {target}, skipping.")
        continue
    # If we are completely off path, let's stop and print
    # But wait, if we are next to the target, we can step. Let's just make sure.
    dx = abs(curr[0] - target[0])
    dy = abs(curr[1] - target[1])
    if dx + dy != 1:
        print(f"Warning: Current position {curr} is not adjacent to target {target}!")
        # Let's adjust direction dynamically if possible
        if curr[0] < target[0]: direction = "Right"
        elif curr[0] > target[0]: direction = "Left"
        elif curr[1] < target[1]: direction = "Down"
        elif curr[1] > target[1]: direction = "Up"
        else:
            print("Already at target!")
            continue
            
    res = step_with_battle_handling(direction, target)
    if not res:
        print(f"Failed to reach {target}. Aborting path.")
        success = False
        break

print("Script finished. Final position:", get_pos())
