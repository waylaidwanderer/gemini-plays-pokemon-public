import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_battle_or_text():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    p1 = img.getpixel((240, 380))
    p2 = img.getpixel((100, 380))
    p3 = img.getpixel((380, 380))
    cream = (247, 231, 214)
    return (p1 == cream and p2 == cream and p3 == cream)

def handle_battle_or_text():
    print("  Battle/Text detected! Clearing...")
    time.sleep(1.0)
    for _ in range(4):
        mgba.press_buttons(["A"])
        time.sleep(0.4)
    
    # Select RUN
    mgba.press_buttons(["Down"])
    time.sleep(0.15)
    mgba.press_buttons(["Right"])
    time.sleep(0.15)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    return not check_battle_or_text()

def step_with_battle_handling_and_retry(direction, expected_pos):
    max_retries = 5
    for attempt in range(max_retries):
        start_pos = get_pos()
        print(f"Attempt {attempt+1}: Stepping {direction} from {start_pos} to {expected_pos}...")
        mgba.press_buttons([direction])
        
        start_wait = time.time()
        is_battle = False
        
        while (time.time() - start_wait) < 10.0:
            if check_battle_or_text():
                is_battle = True
                break
            pos = get_pos()
            if pos != start_pos:
                time.sleep(0.5)
                if check_battle_or_text():
                    is_battle = True
                    break
                final_pos = get_pos()
                if final_pos == expected_pos:
                    print(f"Successfully arrived at {final_pos}")
                    return True
                else:
                    print(f"Spun/Redirected to {final_pos}!")
                    return False
            time.sleep(0.1)
            
        if is_battle:
            if handle_battle_or_text():
                print("Successfully fled from battle!")
                after_pos = get_pos()
                if after_pos == expected_pos:
                    print(f"Arrived at {expected_pos} after battle.")
                    return True
                elif after_pos == start_pos:
                    print("Ended up back at starting position. Retrying...")
                    time.sleep(0.5)
                    continue
                else:
                    print(f"Spun/Redirected to {after_pos} after battle!")
                    return False
            else:
                print("Failed to flee!")
                return False
                
        print("Step failed or blocked!")
        return False
    print("Max retries exceeded!")
    return False

# Path from (15, 6) to (2, 1)
path = [
    ("Left", (14, 6)),
    ("Left", (13, 6)),
    ("Up", (13, 5)),
    ("Up", (13, 4)),
    ("Left", (12, 4)),
    ("Left", (11, 4)),
    ("Up", (11, 3)),
    ("Left", (10, 3)),
    ("Up", (10, 2)),
    ("Left", (9, 2)),
    ("Left", (8, 2)),
    ("Left", (7, 2)),
    ("Left", (6, 2)),
    ("Left", (5, 2)),
    ("Left", (4, 2)),
    ("Up", (4, 1)),
    ("Left", (3, 1)),
    ("Left", (2, 1))
]

print("Starting direct path from (15, 6) to top-left of Gym...")
for d, target in path:
    curr = get_pos()
    if curr == target:
        continue
    success = step_with_battle_handling_and_retry(d, target)
    if not success:
        print("Path execution stopped due to failure or desync.")
        break

print("Path execution finished. Current position:", get_pos())
