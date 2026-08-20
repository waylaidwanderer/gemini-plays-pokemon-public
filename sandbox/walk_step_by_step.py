import mgba
import time

route = [
    ("Right", 17, 4),
    ("Right", 18, 4),
    ("Down", 18, 5),
    ("Down", 18, 6),
    ("Left", 17, 6),
    ("Left", 16, 6),
    ("Left", 15, 6),
    ("Left", 14, 6),
    ("Left", 13, 6),
    ("Left", 12, 6),
    ("Left", 11, 6),
    ("Left", 10, 6),
    ("Left", 9, 6),
    ("Left", 8, 6),
    ("Left", 7, 6),
    ("Left", 6, 6),
    ("Left", 5, 6),
    ("Left", 4, 6),
    ("Left", 3, 6),
    ("Down", 3, 7),
    ("Down", 3, 8),
    ("Down", 3, 9),
    ("Down", 3, 10),
    ("Down", 3, 11),
    ("Down", 3, 12),
    ("Left", 2, 12),
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
