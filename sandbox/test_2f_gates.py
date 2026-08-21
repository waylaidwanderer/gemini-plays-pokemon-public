import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

# Clear menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# 1. Walk from current (9, 11) on 3F to West stairs at (7, 10) on 3F
path_3f = [
    (9, 10),
    (8, 10),
    (7, 10)
]

print("Walking to West stairs on 3F...")
if mgba.get_coordinates()['x'] == 9 and mgba.get_coordinates()['y'] == 11:
    # Walk Up, Left, Left
    mgba.press_buttons(["Up", "sleep 400", "Left", "sleep 400", "Left"])
    time.sleep(2.0) # wait for warp
    print("Arrived on 2F. Position:", get_pos())
    mgba.take_screenshot()
    
    # 2. On 2F (State B), try to walk to (15, 11) directly along row 11
    # We are at (7, 11). We want to walk Right to (15, 11).
    print("Attempting to walk Right from (7, 11) to (15, 11) on 2F...")
    for i in range(8):
        pos_before = get_pos()
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos_after = get_pos()
        print(f"Step {i+1}: from {pos_before} to {pos_after}")
        if pos_before == pos_after:
            print("Blocked!")
            break
            
    print("Final position on 2F:", get_pos())
    mgba.take_screenshot()
else:
    print("Not at starting position (9, 11). Current:", get_pos())
