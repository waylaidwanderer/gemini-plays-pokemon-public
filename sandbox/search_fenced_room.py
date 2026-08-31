import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Fled battle safely.")

def get_dir(curr, target):
    if target[0] > curr['x']: return "Right"
    if target[0] < curr['x']: return "Left"
    if target[1] > curr['y']: return "Down"
    if target[1] < curr['y']: return "Up"
    return None

def walk_to_target(target):
    while True:
        pos = mgba.get_coordinates()
        if pos['x'] == target[0] and pos['y'] == target[1]:
            print(f"Reached target {target}")
            break
            
        direction = get_dir(pos, target)
        if not direction:
            break
            
        print(f"Current: ({pos['x']}, {pos['y']}) | Moving {direction} to target {target}")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()
                time.sleep(0.5)

def main():
    # Path from (17, 6) to the fenced room entrance at (25, 13):
    path_to_entrance = [
        (17, 5), (18, 5), (19, 5), (20, 5), (21, 5),
        (21, 4), (21, 3),
        (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
        (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10), (26, 11), (26, 12),
        (25, 12),
        (25, 13) # entrance gate
    ]
    
    # Grid of tiles inside the fenced room to systematically search:
    fenced_tiles = [
        (25, 14), (26, 14), (27, 14), (28, 14),
        (28, 15), (27, 15), (26, 15), (25, 15),
        (25, 16), (26, 16), (27, 16), (28, 16)
    ]
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # 1. Walk to the fenced room entrance
    print("Walking to fenced room entrance...")
    for target in path_to_entrance:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. Map transition occurred early!")
            return
            
    # 2. Walk on every tile inside the fenced room
    print("Searching inside the fenced room...")
    for target in fenced_tiles:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful! Found the stairs!")
            return
            
    print("Finished search. No warp found inside the fenced room. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
