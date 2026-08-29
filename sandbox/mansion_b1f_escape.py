import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_real_battle():
    # To check if we are in a real battle:
    # 1. Take screenshot
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    # Check if there is the word "FIGHT" or the battle menu.
    # In GBC battle screen, the bottom-right corner of the menu contains "RUN".
    # Let's check if the battle menu background is white/cream and if the cursor is present.
    # Actually, if we are in battle, the coordinates won't change when we try to walk.
    # Let's use a simpler check: if we try to move and get_coordinates() doesn't change,
    # and pressing B doesn't help, we try the flee sequence.
    return False

def flee_from_battle():
    print("  Attempting to flee from battle...")
    # Press B a few times to clear any text
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    
    # Press Down, Right, A to select RUN
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.5)
    
    # Press B to clear "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def step_safe(direction, expected):
    max_retries = 3
    for attempt in range(max_retries):
        curr = get_pos()
        print(f"Step: {direction} from {curr} to {expected} (Attempt {attempt+1})")
        mgba.press_buttons([direction])
        
        # Wait up to 1.5s for coordinate to update
        start_wait = time.time()
        success = False
        while (time.time() - start_wait) < 1.5:
            pos = get_pos()
            if pos == expected:
                success = True
                break
            time.sleep(0.1)
            
        if success:
            print(f"  Reached {expected}")
            # Wait a bit for screen/movement to finish
            time.sleep(0.3)
            return True
            
        # If we didn't reach the expected position, we might be in a battle/textbox
        print("  Did not reach expected position. Checking for battle/text...")
        
        # Let's try to press B to clear any text or menu
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        
        # Try to flee just in case we are in a battle
        flee_from_battle()
        
        # Check if we are now at the expected position (maybe we moved during battle and now we are there)
        pos = get_pos()
        if pos == expected:
            print(f"  Arrived at {expected} after clearing battle/text.")
            return True
            
    print(f"  Failed to step {direction} to {expected}!")
    return False

# Path from current position (27, 6)
path = [
    ("Up", (27, 5)),
    ("Up", (27, 4)),
    ("Up", (27, 3)),
    ("Up", (27, 2)),
    ("Up", (27, 1)),
    ("Left", (26, 1)),
    ("Left", (25, 1)),
    ("Left", (24, 1)),
    ("Left", (23, 1)),
    ("Left", (22, 1)),
    ("Left", (21, 1)),
    ("Down", (21, 2)),
    ("Down", (21, 3)),
    ("Down", (21, 4)),
    ("Down", (21, 5)),
    ("Down", (21, 6)),  # Let's go to row 6 to be extremely safe!
    ("Right", (22, 6))  # Walk Right into the bottom of the staircase!
]

print("Starting robust escape sequence...")
success = True
for direction, target in path:
    curr = get_pos()
    if curr == target:
        continue
    
    # Adjust direction dynamically if we got shifted
    dx = abs(curr[0] - target[0])
    dy = abs(curr[1] - target[1])
    if dx + dy != 1:
        print(f"Warning: Off-path! At {curr}, next target is {target}")
        if curr[0] < target[0]: direction = "Right"
        elif curr[0] > target[0]: direction = "Left"
        elif curr[1] < target[1]: direction = "Down"
        elif curr[1] > target[1]: direction = "Up"
        else:
            continue
            
    res = step_safe(direction, target)
    if not res:
        print(f"Path failed at {target}!")
        success = False
        break

print("Robust escape sequence finished. Final position:", get_pos())
