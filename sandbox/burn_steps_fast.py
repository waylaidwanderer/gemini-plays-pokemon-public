import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Global button count tracker to prevent exceeding 100 limit
button_press_count = 0

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        bridge.press_buttons(["sleep 50"])
    return None

def press_buttons_tracked(buttons):
    global button_press_count
    # Count buttons that are not sleeps
    real_buttons = [b for f in buttons for b in [f] if b != "sleep" and not b.startswith("sleep")]
    button_press_count += len(real_buttons)
    if button_press_count > 95:
        print(f"Approaching button limit! Count is {button_press_count}. Aborting script to prevent crash.")
        sys.exit(0)
    bridge.press_buttons(buttons)

def handle_battle():
    print("Wild battle detected! Escaping...")
    # Escapes from Safari Zone battle
    press_buttons_tracked(["B", "sleep 300", "B", "sleep 300"])
    escape_sequence = [
        "Down", "sleep 200",
        "Right", "sleep 200",
        "A", "sleep 1500"
    ]
    press_buttons_tracked(escape_sequence)
    for _ in range(3):
        press_buttons_tracked(["B", "sleep 200"])
    press_buttons_tracked(["sleep 500"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    press_buttons_tracked([direction])
    
    for _ in range(5):
        press_buttons_tracked(["sleep 100"])
        new_pos = get_pos()
        if new_pos is None:
            handle_battle()
            return None
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        # If we warped out, stop
        if pos[1] < 10 or pos[0] > 10:
            print(f"We have warped out of Safari Zone! Position is {pos}")
            sys.exit(0)
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}... Total Buttons: {button_press_count}")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            time.sleep(0.5)
            check_pos = get_pos()
            if check_pos is None:
                handle_battle()
                stuck_count = 0
                continue
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Stuck! Pressing B and retrying...")
                press_buttons_tracked(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            idx += 1
    return True

def main():
    print("=== RELIABLE STEP BURNING BY WALKING A CORRIDOR ===")
    
    pos = get_pos()
    print("Starting pos:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # We are inside Center Northwest Compartment.
    # Columns 1 to 5 on Row 11 are open grass.
    # Let's walk to Column 1 first if needed
    if pos[0] > 1 and pos[1] == 11:
        path_to_start = ["Left"] * (pos[0] - 1)
        if not run_path(path_to_start):
            print("Failed to align to Column 1")
            return
            
    # Now we walk back and forth between Column 1 and Column 5 (4 steps each way)
    # This will consume 8 steps per cycle, ensuring they are actual steps!
    cycle_path = ["Right"] * 4 + ["Left"] * 4
    
    print("Walking corridor to burn steps...")
    # Run cycles until we hit button limit
    while True:
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        if pos[1] < 10 or pos[0] > 10:
            print(f"We have warped out of Safari Zone! Position is {pos}")
            break
            
        if not run_path(cycle_path):
            print("Failed cycle path!")
            break

if __name__ == "__main__":
    main()
