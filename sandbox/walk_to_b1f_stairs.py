# -*- coding: utf-8 -*-
import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(action):
    pos = mgba.get_coordinates()
    x, y = pos['x'], pos['y']
    mgba.press_buttons([action])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos == {'x': x, 'y': y}:
        flee_battle()
        mgba.press_buttons([action])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
    return new_pos

def walk_to_b1f():
    # We are at (26, 11).
    # Path to (22, 7) stairs:
    path = [
        ("Left", 25, 11),
        ("Up", 25, 10),
        ("Left", 24, 10),
        ("Left", 23, 10),
        ("Up", 23, 9),
        ("Up", 23, 8),
        ("Up", 23, 7),
        ("Left", 22, 7) # Step Left onto the stairs at (22, 7) to warp!
    ]
    
    for action, tx, ty in path:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Testing step: {action} to ({tx}, {ty}), Current: ({x}, {y})")
        pos = walk_step(action)
        # Warp check: if we warped, our position will change drastically (we'll land on B1F East)
        if pos != {'x': x, 'y': y} and pos != {'x': tx, 'y': ty}:
            print(f"WARPED! Landed at: {pos}")
            return
            
    print("Path completed. Final position:", pos)

walk_to_b1f()
