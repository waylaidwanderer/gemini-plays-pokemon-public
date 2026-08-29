import mgba
import time

def move_test(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"probe: Pressing '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 4:
        if pos_before == pos_after:
            print("probe: BUMPED. Retrying...")
            # Dismiss potential battle screen
            mgba.press_buttons(["B"])
            time.sleep(0.5)
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after

def main():
    # We are at (17, 6) on 3F East facing Left
    print("go_to_3f_finish: Starting...")
    
    # Dismiss "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    # 1. Walk Left to (10, 6)
    for x in range(16, 9, -1):
        move_test("Left", x, 6)
        
    # 2. Walk DOWN Column 10 to (10, 10)
    for y in [7, 8, 9, 10]:
        move_test("Down", 10, y)
        
    # 3. Walk LEFT Row 10 to (1, 10)
    for x in range(9, 0, -1):
        move_test("Left", x, 10)
        
    # 4. Walk down to (1, 12) and right to (2, 12)
    move_test("Down", 1, 11)
    move_test("Down", 1, 12)
    move_test("Right", 2, 12)
    
    # 5. Toggle switch to State A
    print("At switch. Toggling to State A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 6. Walk back to (1, 10)
    move_test("Left", 1, 12)
    move_test("Up", 1, 11)
    move_test("Up", 1, 10)
    
    # 7. Walk back to Column 10 Row 10
    for x in range(2, 11):
        move_test("Right", x, 10)
        
    # 8. Walk back UP to Row 6
    for y in [9, 8, 7, 6]:
        move_test("Up", 10, y)
        
    # 9. Walk RIGHT Row 6 to (19, 6)
    for x in range(11, 20):
        move_test("Right", x, 6)
        
    # 10. Walk UP Column 19 to Row 4
    for y in [5, 4]:
        move_test("Up", 19, y)
        
    # 11. Walk RIGHT to (20, 4) and UP to (20, 3)
    move_test("Right", 20, 4)
    move_test("Up", 20, 3)
    
    # 12. Walk RIGHT to (26, 3)
    for x in range(21, 27):
        move_test("Right", x, 3)
        
    # 13. Walk DOWN to (26, 5)
    move_test("Down", 26, 4)
    move_test("Down", 26, 5)
    
    # 14. Test DOWN to (26, 6) in State A!
    print("Testing (26, 6) in State A...")
    pos_down = move_test("Down", 26, 6)
    if pos_down:
        print(f"Succeeded stepping into (26, 6)! Pos: {pos_down}")
    else:
        print("(26, 6) is still solid in State A.")
        
    # 15. Walk UP to (26, 3) -> LEFT to (22, 3) and test stairs (22, 2) in State A!
    pos = mgba.get_coordinates()
    if pos['y'] == 5:
        move_test("Up", 26, 4)
        move_test("Up", 26, 3)
        for x in range(25, 21, -1):
            move_test("Left", x, 3)
        print("Testing stairs at (22, 2) in State A...")
        pos_up = move_test("Up", 22, 2)
        if pos_up:
            print(f"Succeeded stepping onto stairs (22, 2)! Pos: {pos_up}")
        else:
            print("Stairs (22, 2) are still solid/blocked in State A.")

if __name__ == "__main__":
    main()
