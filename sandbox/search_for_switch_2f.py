import mgba
import time

def check_dialogue():
    # Capture screen or check if text appeared.
    # Since we can't read RAM directly, let's take a screenshot and analyze pixels,
    # or we can simply check if pressing B changes the screen, or we can look at the screen text log
    # wait, we can just press A, sleep, then try to step. If we are in a dialogue,
    # stepping will fail. But even better, we can press B and see if the screen changes.
    # Let's use mgba.take_screenshot() to see if there is a text box border at the bottom!
    # In Red/Blue, a text box has a black border at the bottom of the screen (row 12-17).
    # Let's write a simple check: we can press A, sleep 0.5s, then check if we are in a text box.
    # Actually, if we interact with a switch, the text "A secret switch!" appears.
    # Let's press A. If we see a text box, we can read the screen pixels using Pillow!
    pass

def interact_and_verify(x, y, direction):
    print(f"Testing at ({x}, {y}) facing {direction}...")
    # Face the direction
    mgba.press_buttons([direction])
    time.sleep(0.3)
    
    # Press A
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Check if a dialogue opened by taking a screenshot and checking pixels of the textbox
    screenshot_path = mgba.take_screenshot()
    from PIL import Image
    img = Image.open(screenshot_path)
    # The Game Boy screen is 160x144.
    # The textbox is at the bottom, rows 112 to 143.
    # Specifically, the border is at y=112 (black line).
    # Let's check some pixels in the textbox area to see if it's open.
    # Actually, a simpler way: if we press B, and our position doesn't change,
    # we can see if there is text.
    # Let's check if the pixel at (80, 120) is white and (80, 112) is black.
    # In the standard emulator, let's print some pixel colors or just press B.
    # Wait, if we interact with the switch, the textbox says "A secret switch!".
    # Let's just press B to dismiss and check if it was a real switch by observing if gates changed!
    # Wait! If we toggle a switch, the gates globally change state!
    # So we can check if the gate at (4, 11) is still closed.
    # If the gate at (4, 11) opened, then we successfully toggled the switch!
    # Let's check the coordinates of (4, 11) to see if we can step into it!
    # That is the absolute best verification!
    
    # Try to step into (4, 11)
    # But wait, we don't want to walk away yet. Let's just check if a textbox is open.
    # If a textbox is open, we can press B to close it.
    # Let's press B twice to be safe.
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    mgba.press_buttons(["B"])
    time.sleep(0.3)

def walk_to(target_x, target_y):
    pos = mgba.get_coordinates()
    while pos['x'] != target_x or pos['y'] != target_y:
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        if dx > 0: step = "Right"
        elif dx < 0: step = "Left"
        elif dy > 0: step = "Down"
        elif dy < 0: step = "Up"
        else: break
        
        mgba.press_buttons([step])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print(f"Blocked trying to walk to ({target_x}, {target_y})")
            return False
        pos = new_pos
    return True

# Walkable tiles in the 2F West pocket:
# Columns 1, 2, 3 (except machines)
# Rows 10, 11, 12, 13, 14, 15
walkable_tiles = [
    (2, 11), (3, 11), (1, 11),
    (1, 10), (2, 10),
    (1, 12), (2, 12),
    (1, 13), (2, 13), (3, 13),
    (1, 14), (2, 14),
    (1, 15), (2, 15), (3, 15)
]

for tile in walkable_tiles:
    tx, ty = tile
    print(f"Navigating to {tile}...")
    if walk_to(tx, ty):
        # Face all 4 directions and press A
        for d in ["Up", "Down", "Left", "Right"]:
            # Check if there is a solid tile in that direction to interact with
            # (no point pressing A against empty open floor, though we can)
            interact_and_verify(tx, ty, d)
            # Check if (4, 11) gate opened
            # We can test this by walking to (3, 11) and trying to step Right to (4, 11)
            # Let's do that at the end of each tile test to see if we unlocked it!
            pos_before_test = mgba.get_coordinates()
            # Walk to (3, 11)
            walk_to(3, 11)
            # Try to step Right to (4, 11)
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            pos_now = mgba.get_coordinates()
            if pos_now['x'] == 4 and pos_now['y'] == 11:
                print(f"SUCCESS!!! Gate opened! Toggled at {tile} facing {d}!")
                # Walk back to (3, 11) to keep state clean
                mgba.press_buttons(["Left"])
                time.sleep(0.4)
                break
            # Return to tile to continue
            walk_to(tx, ty)

print("Search complete.")
