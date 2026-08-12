import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # First press B a few times to dismiss text
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 200"])
    # Press Down, Right, A to run
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1000"])
    # Press B to dismiss any leftover text
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def go_to_surf_under():
    print("=== EXECUTING ROBUST UNDERGROUND GROUND-LEVEL SURF ROUTE ===")
    
    # Path starting from (14, 20)
    # We are currently at (14, 20)
    # The remaining steps of the path from (14, 20) are:
    # Walk Left from (14, 20) to (3, 20) -> 11 steps Left
    # Walk Up from (3, 20) to (3, 12) -> 8 steps Up
    # Walk Right from (3, 12) to (11, 12) -> 8 steps Right
    # Walk Up from (11, 12) to (11, 11) -> 1 step Up
    
    path = []
    path.extend(["Left"] * 11)  # To (3, 20)
    path.extend(["Up"] * 8)     # To (3, 12)
    path.extend(["Right"] * 8)  # To (11, 12)
    path.extend(["Up"])         # To (11, 11) (Secret House!)

    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        print(f"Step {idx}: Standing at {pos}. Walking {path[idx]}...")
        walk_step(path[idx])
        
        new_pos = get_pos()
        if new_pos is None:
            # We might have transitioned or entered a battle. Let's wait a moment and check again
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                # Still None, likely a battle or transition!
                # Let's check if we transitioned to the Secret House by checking if we can run away
                # If we are in the Secret House, there are no wild battles, but we can't get coordinates if it's a dialog.
                # Let's do a run_away check or just wait
                run_away()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Bumping/blocked. Stuck count: {stuck_count}")
            if stuck_count > 3:
                # Try a tiny adjustment or just exit
                print("Path blocked. Exiting.")
                return False
        else:
            stuck_count = 0
            # Check if we transitioned maps (large coordinate jump or inside Secret House coordinates)
            if new_pos[0] < 5 and new_pos[1] > 5 and new_pos[1] < 10:
                print(f"SUCCESS! Transitioned inside the Secret House at {new_pos}!")
                return True
                
            dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
            if dist > 5:
                print(f"SUCCESS! Map Transition Detected to {new_pos}")
                return True
            idx += 1
            
    return True

if __name__ == "__main__":
    go_to_surf_under()
