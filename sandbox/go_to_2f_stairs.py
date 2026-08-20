import mgba
import time

def walk_step(direction, target_x, target_y):
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
        print("Failed to reach target! Could be a battle or obstacle.")
        return False

def go_to_stairs():
    path = [
        # 1. Walk Up to (6, 11)
        ("Up", 6, 12),
        ("Up", 6, 11),
        # 2. Walk Right to (11, 11)
        ("Right", 7, 11),
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11),
        ("Right", 11, 11),
        # 3. Walk Up to (11, 5)
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        # 4. Walk Right to (18, 5)
        ("Right", 12, 5),
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5),
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        # 5. Walk Up to (18, 3)
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
