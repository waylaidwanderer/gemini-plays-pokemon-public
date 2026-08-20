import mgba
import time

def walk_step(direction, target_x, target_y, target_map=None):
    pos = mgba.get_coordinates()
    print(f"Standing at {pos}. Pressing {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    print(f"Now at {new_pos}. Target was ({target_x}, {target_y})")
    
    # Check if we reached target
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        return True
    else:
        print("Failed to reach target! Could be a battle, wall, or map transition.")
        return False

def go_to_stairs():
    path = [
        # 1. Walk Left to (1, 12), Down to (1, 13)
        ("Left", 1, 12),
        ("Down", 1, 13),
        # 2. Walk Right to (12, 13)
        ("Right", 2, 13),
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Right", 5, 13),
        ("Right", 6, 13),
        ("Right", 7, 13),
        ("Right", 8, 13),
        ("Right", 9, 13),
        ("Right", 10, 13),
        ("Right", 11, 13),
        ("Right", 12, 13),
        # 3. Walk Up to (12, 5)
        ("Up", 12, 12),
        ("Up", 12, 11),
        ("Up", 12, 10),
        ("Up", 12, 9),
        ("Up", 12, 8),
        ("Up", 12, 7),
        ("Up", 12, 6),
        ("Up", 12, 5),
        # 4. Walk Right to (18, 5)
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5),
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        # 5. Walk Up to (18, 2) stairs to trigger warp to 3F
        ("Up", 18, 4),
        ("Up", 18, 3),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not walk_step(direction, tx, ty):
            success = False
            break
            
    if success:
        # Step onto (18, 2) to trigger warp
        print("At (18, 3)! Stepping Up to stairs warp...")
        mgba.press_buttons(["Up"])
        time.sleep(1.2)
        print("Warp complete! New Position:", mgba.get_coordinates())
        
    mgba.take_screenshot()

go_to_stairs()
