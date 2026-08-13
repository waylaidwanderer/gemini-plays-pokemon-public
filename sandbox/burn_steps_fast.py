# Robust script to burn remaining Safari Zone steps safely and quickly in flat grass in Safari Zone Center
import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
    bridge.press_buttons([direction])
    bridge.press_buttons(["sleep 300"])
    new_pos = get_pos()
    if new_pos is None:
        return None
    if new_pos != pos:
        return new_pos
    bridge.press_buttons(["sleep 500"])
    return get_pos()

def main():
    print("=== BURNING SAFARI STEPS IN FLAT GRASS (ROBUST) ===")
    steps = 0
    
    # Alternate Up and Down at Column 1
    while True:
        pos = get_pos()
        if pos is None:
            # We are in dialogue or battle (shouldn't happen on flat grass, but safety first)
            bridge.press_buttons(["B", "sleep 200"])
            continue
            
        # Check if we warped to Gatehouse
        if not (0 <= pos[0] <= 10 and 5 <= pos[1] <= 20):
            print(f"Warp out detected! Current position: {pos}")
            break
            
        # Determine direction dynamically
        direction = "Down" if pos[1] < 12 else "Up"
        
        new_pos = walk_step_robust(direction)
        if new_pos is None:
            continue
            
        steps += 1
        if steps >= 300:
            print("Safety limit of 300 steps reached.")
            break

if __name__ == '__main__':
    main()
