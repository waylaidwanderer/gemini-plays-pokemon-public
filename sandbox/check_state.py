import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("CURRENT POSITION:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

p = check_pos()

if p == {"x": 7, "y": 11}:
    # Walk Left to (2, 11)
    print("Walking Left to (2, 11)...")
    steps = [
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Left", {"x": 4, "y": 11}),
        ("Left", {"x": 3, "y": 11}),
        ("Left", {"x": 2, "y": 11}),
    ]
    for d, expected in steps:
        mgba.press_buttons([d])
        time.sleep(0.55)
        # Handle wild battle if any
        scr = mgba.take_screenshot()
        from PIL import Image
        img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
        black_or_white = 0
        total_pixels = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img.getpixel((x, y))
                total_pixels += 1
                if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                    black_or_white += 1
        if black_or_white / total_pixels > 0.90:
            print("Battle detected during walking! Stopping script.")
            exit(1)
            
        p = check_pos()
        if p != expected:
            print(f"Failed to reach {expected}, actual: {p}")
            exit(1)
            
    # From (2, 11), walk DOWN to (2, 12)
    print("Walking Down to (2, 12)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.55)
    p = check_pos()
    
    if p == {"x": 2, "y": 12}:
        # Face UP
        print("Facing UP towards switch...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Press A to open switch dialogue
        print("Pressing A...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Capture screenshot of dialogue
        scr = mgba.take_screenshot()
        # Save dialogue screenshot to inspect
        img_dialogue = Image.open(scr)
        img_dialogue.save("mansion_switch_dialogue_open.png")
        print("Saved mansion_switch_dialogue_open.png!")
        
        # Press A to select YES (this toggles the switch)
        print("Pressing A on YES...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        
        # Capture screenshot of result
        scr2 = mgba.take_screenshot()
        img_dialogue2 = Image.open(scr2)
        img_dialogue2.save("mansion_switch_dialogue_step2.png")
        print("Saved mansion_switch_dialogue_step2.png!")
        
        # Press A to dismiss result
        print("Dismissing result...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Capture final screen
        scr3 = mgba.take_screenshot()
        img_dialogue3 = Image.open(scr3)
        img_dialogue3.save("mansion_switch_dialogue_final.png")
        print("Saved mansion_switch_dialogue_final.png!")
        
else:
    print("Not starting at (7, 11)")
