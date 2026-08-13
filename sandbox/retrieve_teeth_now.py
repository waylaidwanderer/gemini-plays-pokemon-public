# Script to return from southern ground of Area 3 to Area 2 (North) at (8, 35)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# Reverse path from (19, 24) to (27, 0)
REVERSE_PATH = [
    "Right", "Right", # to (21, 24)
    "Up", "Up", "Up", "Up", "Up", "Up", # to (21, 18)
    "Right", "Right", "Right", "Right", # to (25, 18)
    "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", # to (25, 2)
    "Right", # to (26, 2)
    "Up", "Up", # to (27, 0)
    "Up" # transition to Area 2 (North)
]

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

def main():
    print("=== RETRIEVE TEETH: PART 1 (RETURN TO AREA 2 NORTH) ===")
    pos = get_pos()
    print(f"Starting position: {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    idx = 0
    stuck_count = 0
    while idx < len(REVERSE_PATH):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        d = REVERSE_PATH[idx]
        is_transition = (idx == len(REVERSE_PATH) - 1)
        
        print(f"Step {idx}/{len(REVERSE_PATH)}: At {pos}, walking {d}")
        new_pos = walk_step_robust(d)
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Pressing B.")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if is_transition:
                print("Transitioning map...")
                time.sleep(1.5)
                new_pos = get_pos()
                print(f"Transition complete. Settled position: {new_pos}")
            idx += 1
            
    print("Part 1 finished successfully!")

if __name__ == "__main__":
    main()
