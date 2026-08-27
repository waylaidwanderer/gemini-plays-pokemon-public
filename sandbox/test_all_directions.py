import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for GBC dialogue background (high white/cream pixel count)
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    return white_cream_pixels > 3000

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos == {"x": 2, "y": 11}:
    for direction in ["Up", "Right", "Down", "Left"]:
        print(f"Testing direction {direction}...")
        # Face the direction
        mgba.press_buttons([direction])
        time.sleep(0.45)
        
        # Check if facing actually moved us (if we moved, we must walk back)
        new_pos = mgba.get_coordinates()
        if new_pos != {"x": 2, "y": 11}:
            print(f"  Facing {direction} walked us to {new_pos}! Walking back...")
            # Walk back
            opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
            walk_step = opposite
            mgba.press_buttons([walk_step])
            time.sleep(0.45)
            # Turn to face without stepping? No, we can't turn without stepping unless blocked.
            # Wait, if we walked back, we are at (2,11). How do we face the target without stepping?
            # We can't! But we can just use the fact that the target is blocked, so walking into it will turn us facing it without moving us!
            # Yes! In Gen 1, if we walk towards a solid wall/statue, we don't move, we just turn to face it!
            # So if a direction is blocked, pressing that direction will face it without moving!
            # If a direction is open, pressing that direction will move us!
            continue
            
        # If we didn't move, it means the direction is blocked! (We faced it successfully).
        print(f"  Direction {direction} is blocked. Pressing A to check dialogue...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        if is_dialogue_open():
            print(f"  SUCCESS! Dialogue opened facing {direction}!")
            # Toggle it to State B
            mgba.press_buttons(["A"]) # Yes/No prompt
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Select YES
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            print("  Switch successfully toggled to State B!")
            break
        else:
            print(f"  No dialogue opened facing {direction}.")
            mgba.press_buttons(["B"])
            time.sleep(0.3)
