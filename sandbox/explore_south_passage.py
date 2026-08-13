# Script to execute a short sequence of steps safely
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
    # Escape sequence
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["B", "sleep 150"])
    print("Fled from battle.")
    time.sleep(0.5)

def walk_path(directions):
    print(f"Starting walk_path with directions: {directions}")
    for i, d in enumerate(directions):
        pos = get_pos()
        if pos is None:
            handle_battle()
            pos = get_pos()
            if pos is None:
                print("Still in battle or menu. Aborting.")
                return False
                
        print(f"Step {i+1}: At {pos}, walking {d}")
        bridge.press_buttons([d, "sleep 350"])
        
        # Verify movement
        new_pos = get_pos()
        if new_pos is None:
            handle_battle()
            new_pos = get_pos()
            if new_pos is None:
                print("Still in battle or menu. Aborting.")
                return False
                
        if new_pos == pos:
            # We didn't move. Could be a battle transition delay, or a bump.
            print("Position did not change. Waiting 1.0s to check if battle is starting...")
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                new_pos = get_pos()
            elif new_pos == pos:
                print(f"BUMPED at {pos} walking {d}! Aborting path.")
                return False
                
        print(f"Successfully moved to {new_pos}")
    return True

if __name__ == "__main__":
    # Let's walk UP to (20, 20), then LEFT 8 steps to (12, 20), then DOWN 2 steps to (12, 22), then LEFT 4 steps to (8, 22).
    # That is: Up, Left*8, Down*2, Left*4
    path = ["Up"] + ["Left"] * 8 + ["Down"] * 2 + ["Left"] * 4
    walk_path(path)
