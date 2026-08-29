import mgba
import time
from PIL import Image, ImageChops

def is_in_battle():
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["Start"])
    time.sleep(0.25)
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()
    if bbox is None:
        return True
    else:
        mgba.press_buttons(["Start"])
        time.sleep(0.25)
        return False

def handle_battle_escape():
    print("ESCAPING BATTLE...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    # Handle battle if we didn't move and are in battle
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            # Retry
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    return pos_after['x'] == target_x and pos_after['y'] == target_y

# Simple non-destructive explorer
def main():
    print("mansion_3f_scanner: Probing reachable area...")
    visited = {}
    queue = [mgba.get_coordinates()]
    
    # We will do a manual BFS-like or step-by-step physical test
    # Let's write a simple script that explores a list of coordinates
    # and tests walkability of adjacent tiles.
    # To keep it extremely simple and 100% safe, let's just probe our immediate surroundings
    # and then walk to specific spots to probe.
    
    # Let's map out the Row 11, Row 12, Row 13 hallway.
    # From (1, 10):
    path = [
        ("Down", 1, 11),
        ("Down", 1, 12),
        ("Down", 1, 13),
        ("Right", 2, 13),
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Right", 5, 13),
        ("Right", 6, 13),
        ("Right", 7, 13),
        ("Right", 8, 13),
        ("Right", 9, 13),
    ]
    
    print("Walking down Row 13 to Column 9...")
    current_pos = mgba.get_coordinates()
    for direction, tx, ty in path:
        if current_pos['x'] == tx and current_pos['y'] == ty:
            continue
        success = step_one(direction, tx, ty)
        current_pos = mgba.get_coordinates()
        print(f"Moved {direction} to ({tx}, {ty}) -> {'SUCCESS' if success else 'FAILED'}. Current: {current_pos}")
        if not success:
            break
            
    # Now that we are at the rightmost reachable spot on Row 13,
    # let's probe Up, Down, Left, Right!
    pos = mgba.get_coordinates()
    print(f"Probing surroundings of {pos}...")
    for d, dx, dy in [("Up", 0, -1), ("Down", 0, 1), ("Left", -1, 0), ("Right", 1, 0)]:
        tx, ty = pos['x'] + dx, pos['y'] + dy
        mgba.press_buttons([d])
        time.sleep(0.4)
        pos_test = mgba.get_coordinates()
        if pos_test['x'] == tx and pos_test['y'] == ty:
            print(f"  Direction {d} to ({tx}, {ty}) is WALKABLE!")
            # Backtrack
            back_d = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
            mgba.press_buttons([back_d])
            time.sleep(0.4)
        else:
            if is_in_battle():
                handle_battle_escape()
            else:
                print(f"  Direction {d} to ({tx}, {ty}) is BLOCKED.")

if __name__ == "__main__":
    main()
