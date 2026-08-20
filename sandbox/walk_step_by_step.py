import mgba
import time

route = [
    ("Up", 26, 4),
    ("Up", 26, 3),
    ("Left", 25, 3),
    ("Left", 24, 3),
    ("Left", 23, 3),
    ("Left", 22, 3),
    ("Left", 21, 3),
    ("Down", 21, 4),
    ("Down", 21, 5), # Gate (21, 5) is OPEN in State B!
    ("Down", 21, 6),
    ("Down", 21, 7),
    ("Down", 21, 8),
    ("Down", 21, 9),
    ("Down", 21, 10),
    ("Down", 21, 11),
    ("Down", 21, 12),
    ("Down", 21, 13),
    ("Down", 21, 14),
    ("Right", 22, 14),
    ("Right", 23, 14),
    ("Right", 24, 14),
]

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
    walk_route(route)
