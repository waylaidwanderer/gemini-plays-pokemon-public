import mgba
import time

def walk_route(path):
    print("Starting step-by-step walk...")
    # Dismiss any text box first
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    for direction, tx, ty in path:
        pos = mgba.get_coordinates()
        print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] != tx or new_pos['y'] != ty:
            print(f"INTERRUPTED! Expected ({tx}, {ty}), but ended at {new_pos}.")
            mgba.take_screenshot()
            return False
            
    print("Successfully completed the route!")
    return True

if __name__ == "__main__":
    # We are at (19, 5) on 3F.
    route = [
        ("Up", 19, 4),
        ("Up", 19, 3),
        ("Right", 20, 3),
        ("Right", 21, 3),
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Down", 25, 4),
        ("Down", 25, 5),
        ("Down", 25, 6),
        ("Down", 25, 7),
        ("Down", 25, 8),
        ("Down", 25, 9),
        ("Down", 25, 10),
        ("Down", 25, 11),
        ("Down", 25, 12),
        ("Down", 25, 13),
        ("Down", 25, 14),
        ("Left", 24, 14),
    ]
    walk_route(route)
