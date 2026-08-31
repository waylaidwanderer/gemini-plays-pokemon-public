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
    print("Fleeing current battle first...")
    flee_battle_safe()
    
    # We are currently at (26, 12) on 1F East.
    # The entrance to the fenced room is at (25, 13) or (25, 12) -> (25, 13) -> (25, 14).
    # Let's explore the fenced room systematic coordinates:
    path = [
        # Walk to entrance
        (25, 12),
        # Step into the fenced room via gate
        (25, 13),
        # Go deeper
        (25, 14), (26, 14), (27, 14), (28, 14),
        (28, 15), (27, 15), (26, 15), (25, 15),
        (25, 16), (26, 16), (27, 16), (28, 16)
    ]
    
    print("Walking systematic exploration of 1F East fenced room...")
    for target in path:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Warp check: did our coordinates change drastically or did we disappear?
        # A map transition will load a new screen and usually reset coordinates or change them.
        # But we can also look at the return value of get_coordinates().
        # In Pokémon, B1F East stairs land the player at a specific coordinate.
        # Let's print our coordinate after each successful step.
        print("Currently at:", pos_after)
        
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
