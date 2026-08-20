import mgba
import time

def enter_mansion():
    print("Executing final bypass route to Pokemon Mansion...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # We are at (10, 6). Bypassing Cooltrainer by walking Right, Up, Left
    path = [
        ("Right", 11, 6),
        ("Up", 11, 5),
        ("Up", 11, 4),
        ("Left", 10, 4),
        ("Left", 9, 4),
        ("Left", 8, 4),
        ("Left", 7, 4),
        ("Left", 6, 4),
    ]
    
    for d, tx, ty in path:
        print(f"At {mgba.get_coordinates()}. Moving {d} to ({tx}, {ty})...")
        mgba.press_buttons([d])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        if pos['x'] != tx or pos['y'] != ty:
            print(f"Blocked at ({tx}, {ty})! Current pos: {pos}")
            mgba.take_screenshot()
            return False
            
    # Now step UP onto the door at (6, 3) to warp inside
    print("At (6, 4). Stepping UP onto (6, 3) to enter Pokemon Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # Wait for warp
    
    final_pos = mgba.get_coordinates()
    print("Successfully entered! Inside coordinates:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    enter_mansion()
