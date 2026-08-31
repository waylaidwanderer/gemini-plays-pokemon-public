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

def probe_room_for_stairs():
    # We are at (26, 14).
    # Let's try stepping onto all coordinates in this bottom-right room (fenced area)
    # Columns 24 to 28, Rows 10 to 18.
    # We will walk a grid pattern and if we warp to B1F, we will break and succeed!
    start_pos = mgba.get_coordinates()
    print("Start position:", start_pos)
    
    # Coordinates to visit/test:
    # 1. Row 14, 15, 16: Column 25, 26, 27
    # 2. Row 10, 11, 12: Column 24, 25, 26
    
    test_tiles = [
        # First, let's explore Row 15, 16, 17, 18 on Columns 25, 26, 27
        ("Down", 26, 15),
        ("Down", 26, 16),
        ("Down", 26, 17), # Test Row 17!
        ("Down", 26, 18), # Test Row 18!
        ("Left", 25, 18),
        ("Right", 26, 18),
        ("Right", 27, 18),
        # Go back Up
        ("Up", 27, 17),
        ("Up", 27, 16),
        ("Up", 27, 15),
        ("Up", 27, 14),
        # Explore Upper area of the room via Column 25
        ("Left", 26, 14),
        ("Left", 25, 14),
        ("Up", 25, 13),
        ("Up", 25, 12),
        ("Up", 25, 11),
        ("Up", 25, 10),
        # Test Column 26 in Upper area
        ("Right", 26, 10),
        ("Down", 26, 11), # Test (26, 11)
        ("Down", 26, 12), # Test (26, 12)
        # Test Column 24
        ("Up", 26, 11),
        ("Up", 26, 10),
        ("Left", 25, 10),
        ("Left", 24, 10),
        ("Down", 24, 11),
        ("Down", 24, 12),
        ("Down", 24, 13)
    ]
    
    for action, tx, ty in test_tiles:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Testing step: {action} to ({tx}, {ty}), Current: ({x}, {y})")
        
        # If we successfully warp to B1F, we will land at some B1F coordinates
        # B1F East coordinates are around (26, 14) or B1F map landing.
        # But we can detect if the map changed or if we are no longer in our testing list.
        # A warp always takes ~1-2 seconds and places us on the B1F landing.
        # Let's check if our coordinates changed drastically or if we warped.
        # Let's detect if we are no longer in our start floor.
        # We can also check if we hit a warp by observing if the coordinates don't match tx, ty but changed from x, y.
        pos = walk_step(action)
        if pos != {'x': x, 'y': y} and pos != {'x': tx, 'y': ty}:
            print(f"WARPED! Landed at: {pos}")
            return
            
    print("Room probing complete.")

probe_room_for_stairs()
