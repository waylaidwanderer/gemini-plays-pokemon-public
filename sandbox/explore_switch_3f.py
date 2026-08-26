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

if p == {"x": 1, "y": 10}:
    # Walk DOWN Column 1 to Row 13
    steps = [
        ("Down", {"x": 1, "y": 11}),
        ("Down", {"x": 1, "y": 12}),
        ("Down", {"x": 1, "y": 13}),
    ]
    for d, expected in steps:
        mgba.press_buttons([d])
        time.sleep(0.55)
        # Handle battle if any
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
            print("Battle detected during walking! Stopping script to let player run.")
            exit(1)
            
        p = check_pos()
        if p != expected:
            print(f"Failed to reach {expected}, actual: {p}")
            exit(1)
            
    # Now we are at (1, 13).
    # Let's test facing UP from (1, 13) towards (1, 12).
    print("At (1, 13). Facing UP towards (1, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Save screenshot of dialogue
    scr = mgba.take_screenshot()
    from PIL import Image
    img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
    img.save("mansion_switch_dialogue_UP_at_1_13.png")
    print("Saved mansion_switch_dialogue_UP_at_1_13.png")
    
    # Let's check if the dialogue opened by looking for the black border of the text box
    # In GBC mode, the dialogue box has a dark gray/black border at y=112 (or y=113)
    # Let's check a few pixels on y=112 to see if they are black
    border_pixels_black = True
    for x in range(20, 140, 10):
        r, g, b = img.getpixel((x, 112))
        # Black border pixel check
        if r > 60 or g > 60 or b > 60:
            border_pixels_black = False
            break
            
    if border_pixels_black:
        print("Genuine dialogue box border detected! Toggling switch to State B...")
        # Select YES (A, sleep, A)
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        # Dismiss result
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        print("Successfully toggled switch to State B!")
    else:
        print("No genuine dialogue box detected facing UP from (1, 13).")
        
        # Let's try facing LEFT from (1, 13) towards (0, 13)
        print("Facing LEFT from (1, 13) towards (0, 13)...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        scr = mgba.take_screenshot()
        img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
        img.save("mansion_switch_dialogue_LEFT_at_1_13.png")
        
        border_pixels_black = True
        for x in range(20, 140, 10):
            r, g, b = img.getpixel((x, 112))
            if r > 60 or g > 60 or b > 60:
                border_pixels_black = False
                break
        if border_pixels_black:
            print("Genuine dialogue box border detected facing LEFT! Toggling...")
            mgba.press_buttons(["A"])
            time.sleep(1.5)
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            print("Successfully toggled switch to State B!")
        else:
            print("No genuine dialogue box detected facing LEFT.")
            
else:
    print("Not starting at (1, 10)")
