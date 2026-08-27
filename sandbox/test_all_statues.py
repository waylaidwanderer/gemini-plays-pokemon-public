import mgba
import time
from PIL import Image

def is_battle():
    # Detect if we are in a battle screen by checking for the distinct black/white HP bar or battle menu
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    
    # Check if the text "FIGHT" or "PKMN" is in the bottom right area of the battle screen
    # Or simply if we have high-contrast elements in the middle of the screen (where sprites and HP bars are)
    # A simple way to check for battle is if we see the player's HP bar at (100..155, 80..95)
    # Let's count white/black pixels in the player HP area
    player_hp_area = img.crop((95, 75, 155, 95))
    black_or_white = 0
    for y in range(player_hp_area.height):
        for x in range(player_hp_area.width):
            r, g, b = player_hp_area.getpixel((x, y))[:3]
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
    return black_or_white > 800

def handle_any_menu_or_battle():
    time.sleep(0.15)
    if is_battle():
        print("Battle detected! Running away...")
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
        time.sleep(1.5)
        for _ in range(4):
            mgba.press_buttons(["B"])
            time.sleep(0.3)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
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

print("Running test_all_statues.py...")
pos = mgba.get_coordinates()
print("Starting search from:", pos)

# We want to test the statues on Column 3.
# Walk to (3, 11) via Row 11
if pos != {"x": 3, "y": 11}:
    print("Walking to (3, 11)...")
    # First walk down to Row 11 if we are at Row 10
    if pos["y"] == 10:
        walk_step("Down", {"x": pos["x"], "y": 11})
    pos = mgba.get_coordinates()
    # Now walk to Column 3
    if pos["x"] != 3:
        d = "Right" if 3 > pos["x"] else "Left"
        walk_step(d, {"x": 3, "y": 11})
    pos = mgba.get_coordinates()

# Now we are at (3, 11).
# Let's test the statue at (3, 10).
if pos == {"x": 3, "y": 11}:
    print("Testing (3, 10) from (3, 11) facing UP...")
    # To face UP, we must be at (3, 12) and walk UP to (3, 11)
    if run_steps([
        ("Down", {"x": 3, "y": 12}),
        ("Up", {"x": 3, "y": 11})
    ]):
        # Now facing UP!
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        # Check if dialogue is open
        scr_file = mgba.take_screenshot()
        img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
        cropped = img.crop((0, 104, 160, 144))
        # Let's save it to inspect
        cropped.save("cropped_test/mansion_switch_dialogue_UP_at_2_11.png")
        print("Pressed A at (3, 11) facing UP. Saved image to cropped_test/mansion_switch_dialogue_UP_at_2_11.png")
        mgba.press_buttons(["B"])
        time.sleep(0.3)

# Let's also test (3, 12) from (3, 13) facing UP
pos = mgba.get_coordinates()
if pos == {"x": 3, "y": 11}:
    if run_steps([
        ("Down", {"x": 3, "y": 12}),
        ("Down", {"x": 3, "y": 13}),
        ("Down", {"x": 3, "y": 14}),
        ("Up", {"x": 3, "y": 13})
    ]):
        # Now facing UP towards (3, 12) standing at (3, 13)
        print("Testing (3, 12) from (3, 13) facing UP...")
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        scr_file = mgba.take_screenshot()
        img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
        cropped = img.crop((0, 104, 160, 144))
        cropped.save("cropped_test/mansion_switch_dialogue_UP_at_1_13.png")
        print("Pressed A at (3, 13) facing UP. Saved image to cropped_test/mansion_switch_dialogue_UP_at_1_13.png")
        mgba.press_buttons(["B"])
        time.sleep(0.3)

# Let's also test (3, 12) from (2, 12) facing RIGHT
pos = mgba.get_coordinates()
if pos == {"x": 3, "y": 13} or pos == {"x": 3, "y": 12}:
    if run_steps([
        ("Down", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
        ("Up", {"x": 2, "y": 12})
    ]):
        # We are at (2, 12). Since Column 2 has no statue, we walked there.
        # Now, how do we face RIGHT?
        # We can walk from (1, 12) to (2, 12) by pressing Right!
        if run_steps([
            ("Left", {"x": 1, "y": 12}),
            ("Right", {"x": 2, "y": 12})
        ]):
            # Now facing RIGHT towards (3, 12) standing at (2, 12)
            print("Testing (3, 12) from (2, 12) facing RIGHT...")
            mgba.press_buttons(["A"])
            time.sleep(0.8)
            scr_file = mgba.take_screenshot()
            img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
            cropped = img.crop((0, 104, 160, 144))
            cropped.save("cropped_test/mansion_switch_dialogue_LEFT_at_1_13.png")
            print("Pressed A at (2, 12) facing RIGHT. Saved image to cropped_test/mansion_switch_dialogue_LEFT_at_1_13.png")
            mgba.press_buttons(["B"])
            time.sleep(0.3)

print("Statue test completed.")
