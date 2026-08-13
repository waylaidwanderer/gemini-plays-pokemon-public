import mgba
import time

def get_pos():
    for _ in range(4):
        pos = mgba.get_coordinates()
        if pos is not None:
            return pos
        # If None, we might be in battle or dialogue. Press B to dismiss or escape
        mgba.press_buttons(["B", "sleep 100"])
    return None

def burn_steps():
    print("=== BURNING SAFARI STEPS ROBUSTLY ===")
    steps_taken = 0
    
    # We are standing at (12, 20).
    # We will alternate moving Left to (11, 20) and Right to (12, 20).
    while True:
        pos = get_pos()
        if pos is None:
            # We are in battle or dialogue! Let's handle it
            print("Position is None. Handling dialogue or battle...")
            # Press A/B to progress dialogue or escape battle
            mgba.press_buttons(["B", "sleep 150"])
            # Try escaping battle
            mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 500"])
            continue
            
        # Check if we warped to the Gatehouse.
        # Gatehouse maps are NOT Safari Zone, and their coordinates are usually around (3, 2) or (4, 2).
        # In Fuchsia Safari Gatehouse, coordinates are (4, 2) or similar.
        # Let's verify we are still on the Southern Plateau: x between 10 and 14, y between 19 and 21.
        if not (10 <= pos['x'] <= 14 and 19 <= pos['y'] <= 21):
            print(f"Warp detected! Current position: {pos}. Exiting loop.")
            break
            
        # Determine direction based on current x
        if pos['x'] == 12:
            direction = "Left"
        else:
            direction = "Right"
            
        print(f"Step {steps_taken}: at {pos}, walking {direction}")
        mgba.press_buttons([direction])
        time.sleep(0.15)
        steps_taken += 1
        
        if steps_taken >= 200:
            print("Safety limit of 200 steps reached. Exiting.")
            break

if __name__ == '__main__':
    burn_steps()
