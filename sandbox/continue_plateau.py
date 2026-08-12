import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_battle_and_run():
    print("Wild battle detected! Running away...")
    # Press B a few times to dismiss first text
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 200"])
    # Press Down, Right, A to run
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
    # Press B to dismiss "Got away safely!"
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle_and_run()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change (up to 750 ms)
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            return None
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    # If we are stuck, we assume it's a battle because there are no wall obstacles on our path!
    handle_battle_and_run()
    # Retry walking
    print(f"Retrying: walking {direction}...")
    bridge.press_buttons([direction])
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            return None
        if new_pos != pos:
            return new_pos
    return pos

def walk_to_plateau_continue():
    # Dismiss the "Got away safely!" screen
    print("Dismissing 'Got away safely!' screen...")
    bridge.press_buttons(["B", "sleep 500"])
    
    # Path from (4, 20) to (6, 16)
    path = []
    path.extend(["Right"] * 2) # to (6, 20)
    path.extend(["Up"] * 4)   # to (6, 16) (climb West Stairs and walk north on Plateau)

    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle_and_run()
            continue
            
        print(f"Step {idx}: Standing at {pos}. Walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            handle_battle_and_run()
            continue
            
        if new_pos == pos:
            stuck_count += 1
            print(f"Still stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked! Exiting.")
                return False
        else:
            stuck_count = 0
            idx += 1
            
    print(f"SUCCESS! Reached plateau coordinates: {get_pos()}")
    return True

if __name__ == "__main__":
    walk_to_plateau_continue()
