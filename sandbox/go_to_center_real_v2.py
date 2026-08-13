# Script to walk back to Gatehouse, exit to Fuchsia, and check Pokémon Center PC
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
    print("=== GO TO CENTER V2 ===")
    
    pos = get_pos()
    print("Initial Position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # 1. Walk to Area 1 East transition to Center
    if pos[0] >= 1 and pos[1] >= 20: # inside Area 1 East
        print("=== Step 1: Walking to Center Transition ===")
        left_steps = pos[0]
        up_steps = pos[1] - 22
        path_to_center = (
            ["Left"] * left_steps +   # to (0, 24)
            ["Up"] * up_steps +       # to (0, 22)
            ["Left"] * 1              # Transition
        )
        if not run_path(path_to_center, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Center:", pos)

    # 2. Walk Center to Gatehouse Exit
    pos = get_pos()
    if pos is not None and pos[0] >= 25 and pos[1] <= 15: # inside Center near (29, 10)
        print("=== Step 2: Walking Center to Gatehouse ===")
        path_to_gatehouse = (
            ["Left"] * (pos[0] - 15) +  # to (15, 10)
            ["Down"] * 15               # to (15, 25) Gatehouse transition
        )
        if not run_path(path_to_gatehouse, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Gatehouse:", pos)

    # 3. Exit Gatehouse to Fuchsia City
    pos = get_pos()
    if pos is not None and pos[0] < 10 and pos[1] < 10: # inside Gatehouse at (4, 2)
        print("=== Step 3: Exiting Gatehouse ===")
        path_exit = (
            ["Down"] * 3 # to exit warp at (4, 5)
        )
        if not run_path(path_exit, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Fuchsia City:", pos)

    # 4. Fuchsia City to Pokémon Center
    pos = get_pos()
    if pos is not None and pos[0] == 18 and pos[1] == 4: # Fuchsia City at (18, 4)
        print("=== Step 4: Fuchsia City to Pokemon Center ===")
        path_to_pc = (
            ["Down"] * 24 + # to (18, 28)
            ["Right"] * 1 + # to (19, 28)
            ["Up"] * 1      # enter Pokemon Center
        )
        if not run_path(path_to_pc, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Pokemon Center:", pos)

if __name__ == "__main__":
    main()
