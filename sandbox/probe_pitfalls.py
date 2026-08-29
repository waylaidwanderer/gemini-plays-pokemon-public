import mgba
import time

def is_in_battle():
    # If the coordinate reads B1F or 1F, we fell, but let's check coordinate changes
    return False

def move_test(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"probe: Pressing '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    # Check if we fell (y is no longer 3, 4, 5, 6, 7 on 3F)
    # Wait, 1F coordinates might have different values or we warp
    # In any case, if pos_after is completely different or we fell:
    if pos_after['y'] > 18 or pos_after['y'] < 0:
        print(f"probe: FELL THROUGH PITFALL! Current pos: {pos_after}")
        return pos_after
        
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 2:
        if pos_before == pos_after:
            print("probe: BUMPED into wall/rubble.")
            return None
        # Try to step again if we turned
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after

def test_all():
    # We start at (27, 3)
    pos = mgba.get_coordinates()
    print(f"Starting test_all from {pos}")
    
    # 1. Walk Left to (25, 3)
    pos = move_test("Left", 26, 3)
    if not pos: return
    pos = move_test("Left", 25, 3)
    if not pos: return
    
    # Test LEFT to (24, 3)
    print("Testing (24, 3)...")
    if move_test("Left", 24, 3):
        print("Succeeded walking onto (24, 3)!")
        return
        
    # Test UP to (25, 2)
    print("Testing (25, 2)...")
    if move_test("Up", 25, 2):
        print("Succeeded walking onto (25, 2)!")
        return
        
    # 2. Walk Down to (25, 4)
    pos = move_test("Down", 25, 4)
    if not pos: return
    
    # Test LEFT to (24, 4)
    print("Testing (24, 4)...")
    if move_test("Left", 24, 4):
        print("Succeeded walking onto (24, 4)!")
        return
        
    # 3. Walk Down to (25, 5)
    pos = move_test("Down", 25, 5)
    if not pos: return
    
    # Test LEFT to (24, 5)
    print("Testing (24, 5)...")
    if move_test("Left", 24, 5):
        print("Succeeded walking onto (24, 5)!")
        return
        
    # Test DOWN to (25, 6)
    print("Testing (25, 6)...")
    if move_test("Down", 25, 6):
        print("Succeeded walking onto (25, 6)!")
        return
        
    # 4. Walk Right to (27, 5)
    pos = move_test("Right", 26, 5)
    if not pos: return
    pos = move_test("Right", 27, 5)
    if not pos: return
    
    # Walk Up to (27, 4) then (27, 3)
    pos = move_test("Up", 27, 4)
    if not pos: return
    pos = move_test("Up", 27, 3)
    if not pos: return
    
    # Test RIGHT to (28, 3)
    print("Testing (28, 3)...")
    if move_test("Right", 28, 3):
        print("Succeeded walking onto (28, 3)!")
        return
        
    # 5. Walk Down to (27, 5)
    pos = move_test("Down", 27, 4)
    if not pos: return
    pos = move_test("Down", 27, 5)
    if not pos: return
    
    # Walk Right to (28, 5)
    pos = move_test("Right", 28, 5)
    if not pos: return
    
    # Walk Down to (28, 6)
    pos = move_test("Down", 28, 6)
    if not pos: return
    
    # Test LEFT to (27, 6)
    print("Testing (27, 6)...")
    if move_test("Left", 27, 6):
        print("Succeeded walking onto (27, 6)!")
        return
        
    # 6. Walk Down to (28, 7)
    pos = move_test("Down", 28, 7)
    if not pos: return
    
    # Test LEFT to (27, 7)
    print("Testing (27, 7)...")
    if move_test("Left", 27, 7):
        print("Succeeded walking onto (27, 7)!")
        return
        
    # Test DOWN to (28, 8)
    print("Testing (28, 8)...")
    if move_test("Down", 28, 8):
        print("Succeeded walking onto (28, 8)!")
        return
        
    print("All tests completed. No pitfall found in the immediate area!")

if __name__ == "__main__":
    test_all()
