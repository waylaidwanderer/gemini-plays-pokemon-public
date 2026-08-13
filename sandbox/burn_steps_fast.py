# Script to burn remaining Safari Zone steps safely and quickly using the raw socket bridge.py
import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("=== BURNING SAFARI STEPS IN FLAT GRASS (SOCKET BRIDGE) ===")
    steps = 0
    # Current pos: (0, 11). Move to (1, 11)
    bridge.press_buttons(["Right", "sleep 250"])
    
    # Alternate Up and Down at Column 1
    while True:
        pos = get_pos()
        if pos is None:
            # We are in dialogue or battle (shouldn't happen on flat grass, but safety first)
            bridge.press_buttons(["B", "sleep 200"])
            continue
            
        # Check if we warped to Gatehouse
        # Gatehouse coordinates are usually (3, 2) or (4, 2).
        # We check if we are no longer in the Northwest Compartment of Center.
        if not (0 <= pos[0] <= 10 and 5 <= pos[1] <= 20):
            print(f"Warp out detected! Current position: {pos}")
            break
            
        if pos[1] == 11:
            bridge.press_buttons(["Down"])
        else:
            bridge.press_buttons(["Up"])
            
        # Sleep for a bit to let the step complete
        bridge.press_buttons(["sleep 150"])
        steps += 1
        if steps >= 300:
            print("Safety limit of 300 steps reached.")
            break

if __name__ == '__main__':
    main()
