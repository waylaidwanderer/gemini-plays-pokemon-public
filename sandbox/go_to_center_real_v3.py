# Master script to walk back to Gatehouse, exit to Fuchsia, and enter Pokémon Center from (22, 10)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_battle():
    print("Wild battle detected! Fleeing...")
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["B", "sleep 150"])
    print("Fled from battle.")
    time.sleep(0.5)

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction, "sleep 350"])
    
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    if new_pos != pos:
        return new_pos
        
    print("Position did not change. Waiting 3.0s to check if battle is starting...")
    time.sleep(3.0)
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
    elif new_pos == pos:
        print(f"Bumping/stuck at {pos} walking {direction}!")
        return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Step {idx}/{len(path)}: At {pos}, walking {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Clearing with B.")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Settled at {new_pos}")
                    return True
            idx += 1
    return True

def main():
    print("=== GO TO CENTER V3 ===")
    pos = get_pos()
    print("Initial Position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # 1. Walk from (22, 10) to Gatehouse exit in Center
    if pos[1] == 10 and pos[0] >= 15 and pos[0] <= 24:
        print("=== Step 1: Walking to Gatehouse ===")
        path_to_gatehouse = (
            ["Right"] * (28 - pos[0]) + # to (28, 10)
            ["Down"] * 12 +             # to (28, 22)
            ["Left"] * 13 +             # to (15, 22)
            ["Down"] * 3                # Gatehouse transition
        )
        if not run_path(path_to_gatehouse, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Gatehouse:", pos)

    # 2. Exit Gatehouse
    pos = get_pos()
    if pos is not None and pos[0] < 10 and pos[1] < 10:
        print("=== Step 2: Exiting Gatehouse ===")
        path_exit = ["Down"] * 3
        if not run_path(path_exit, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Fuchsia City:", pos)

    # 3. Fuchsia City to Pokémon Center
    pos = get_pos()
    if pos is not None and pos[0] == 18 and pos[1] == 4:
        print("=== Step 3: Fuchsia City to Pokémon Center ===")
        path_to_pc = (
            ["Down"] * 24 + # to (18, 28)
            ["Right"] * 1 + # to (19, 28)
            ["Up"] * 1      # PC transition
        )
        if not run_path(path_to_pc, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Pokémon Center:", pos)

if __name__ == "__main__":
    main()
