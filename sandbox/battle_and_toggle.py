import mgba
import time
from PIL import Image

def is_dialogue_or_battle_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for white/cream pixels in dialogue area
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    return white_cream_pixels > 2500

def handle_trainer_battle():
    # Loop to handle a trainer battle by pressing A/B to fight and advance text
    battle_turns = 0
    while True:
        time.sleep(0.2)
        scr_file = mgba.take_screenshot()
        img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
        
        # Check if we are still in battle or text
        # If there's no dialogue box, wait a bit and check again. If still none, battle ended.
        if not is_dialogue_or_battle_open():
            time.sleep(0.5)
            if not is_dialogue_or_battle_open():
                print("No dialogue/battle detected. Battle must have ended!")
                break
                
        # Press A to fight, select move, and advance text
        mgba.press_buttons(["A"])
        battle_turns += 1
        if battle_turns > 120:  # Safety timeout
            print("Battle taking too long, safety exit.")
            break

def walk_step(direction, expected_coords, retries=10):
    for i in range(retries):
        if is_dialogue_or_battle_open():
            print("Dialogue or battle triggered! Handling...")
            handle_trainer_battle()
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
                
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Ensure any active menus are dismissed
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting from position:", pos)

# We are at (6, 11). Walk LEFT to (5, 11) to trigger the trainer battle!
if pos == {"x": 6, "y": 11}:
    print("Stepping LEFT to (5, 11) to face the trainer...")
    # This will trigger the trainer battle. walk_step will detect the battle and handle it!
    walk_step("Left", {"x": 5, "y": 11})
    pos = mgba.get_coordinates()

# Now walk around the trainer via Row 13 to (2, 11)
if pos == {"x": 5, "y": 11}:
    print("Walking around the trainer...")
    steps = [
        ("Down", {"x": 5, "y": 12}),
        ("Down", {"x": 5, "y": 13}),
        ("Left", {"x": 4, "y": 13}),
        ("Left", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
        ("Up", {"x": 2, "y": 12}),
        ("Up", {"x": 2, "y": 11}),
    ]
    if run_steps(steps):
        pos = mgba.get_coordinates()

# Stand at (2, 11) facing UP towards the switch at (2, 10) and toggle it
if pos == {"x": 2, "y": 11}:
    print("Standing at (2, 11). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Interacting with the switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    if is_dialogue_or_battle_open():
        print("Switch dialogue open! Toggling to State B...")
        mgba.press_buttons(["A"]) # Advance "A secret switch!"
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Select YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Dismiss "Pressed it!"
        time.sleep(1.5)
        print("Mansion state successfully toggled to State B!")
    else:
        print("Failed to open switch dialogue.")
        
print("Final coordinates after script:", mgba.get_coordinates())
