# Script to burn remaining Safari Zone steps safely and quickly in flat grass in Safari Zone Center
import mgba
import time

def main():
    print("=== BURNING SAFARI STEPS IN FLAT GRASS ===")
    steps = 0
    # Current pos: (0, 11). Move to (1, 11)
    mgba.press_buttons(["Right", "sleep 250"])
    
    # Alternate Up and Down at Column 1
    while True:
        pos = mgba.get_coordinates()
        if pos is None:
            # We are in dialogue or battle (shouldn't happen on flat grass, but safety first)
            mgba.press_buttons(["B", "sleep 200"])
            continue
            
        # Check if we warped to Gatehouse
        # Gatehouse coordinates are usually (3, 2) or (4, 2).
        # We check if we are no longer in the Northwest Compartment of Center.
        if not (0 <= pos['x'] <= 10 and 5 <= pos['y'] <= 20):
            print(f"Warp out detected! Current position: {pos}")
            break
            
        if pos['y'] == 11:
            mgba.press_buttons(["Down"])
        else:
            mgba.press_buttons(["Up"])
            
        time.sleep(0.15)
        steps += 1
        if steps >= 300:
            print("Safety limit of 300 steps reached.")
            break

if __name__ == '__main__':
    main()
