import mgba
import time

def walk_step(direction, target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Standing at {pos}. Pressing {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    print(f"Now at {new_pos}. Target was ({target_x}, {target_y})")
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        return True
    else:
        print("Failed to reach target!")
        return False

def test_row_6():
    # Current: (14, 5) on 2F
    # 1. Step Down to (14, 6)
    if not walk_step("Down", 14, 6):
        mgba.take_screenshot()
        return
        
    # 2. Walk Right to (18, 6) (4 steps Right)
    path = [
        ("Right", 15, 6),
        ("Right", 16, 6),
        ("Right", 17, 6),
        ("Right", 18, 6),
    ]
    for d, tx, ty in path:
        if not walk_step(d, tx, ty):
            break
            
    mgba.take_screenshot()

test_row_6()
