import mgba
import time

route = [
    ("Left", 18, 4),
    ("Left", 17, 4),
    ("Up", 17, 3),
    ("Left", 16, 3),
    ("Left", 15, 3),
    ("Left", 14, 3),
    ("Left", 13, 3),
    ("Left", 12, 3),
    ("Left", 11, 3),
    ("Left", 10, 3),
    ("Left", 9, 3),
    ("Left", 8, 3),
    ("Left", 7, 3),
    ("Left", 6, 3),
    ("Left", 5, 3),
    ("Left", 4, 3),
    ("Left", 3, 3),
    ("Down", 3, 4),
    ("Down", 3, 5),
    ("Down", 3, 6),
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
