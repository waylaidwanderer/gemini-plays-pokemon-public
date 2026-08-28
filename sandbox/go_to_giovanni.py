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

def step_with_battle_handling(direction, expected_pos):
    start_pos = get_pos()
    print(f"Stepping {direction} from {start_pos} to {expected_pos}...")
    mgba.press_buttons([direction])
    
    start_wait = time.time()
    is_battle = False
    while (time.time() - start_wait) < 5.0:
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
            print(f"Successfully arrived at {final_pos}")
            return True
        time.sleep(0.1)
        
    if is_battle:
        if handle_battle_or_text():
            print("Successfully fled from battle!")
            # Let's wait and see our position
            final_pos = get_pos()
            print(f"Arrived at {final_pos} after fleeing.")
            return True
        else:
            print("Failed to flee!")
            return False
            
    print("Step failed or blocked!")
    return False

# Path to Giovanni's area
path = [
    ("Up", (19, 5)),
    ("Up", (19, 4)),
    ("Up", (19, 3)),
    ("Left", (18, 3)),
    ("Up", (18, 2)),
    ("Up", (18, 1))
]

print("Starting direct path to top-right of Gym...")
for d, target in path:
    curr = get_pos()
    if curr == target:
        print(f"Already at {target}, skipping step.")
        continue
    # If we got desynced or spun, let's stop and report
    # Wait, we can check if the step succeeds
    success = step_with_battle_handling(d, target)
    if not success:
        print("Path execution stopped due to failure or desync.")
        break
    # Check if we got spun to a different tile
    after = get_pos()
    if after != target:
        print(f"Spun/Redirected! We are at {after} instead of {target}. Stopping path.")
        break

print("Path execution finished. Current position:", get_pos())
