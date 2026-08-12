import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def burn_robust():
    direction = "Right"
    step_count = 0
    max_steps = 95 # Strict limit to avoid exceeding emulator harness button press limits
    
    while step_count < max_steps:
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        cx, cy = pos
        # Check if we were warped back to the gatehouse (or any other map)
        if cy != 24 or cx < 17 or cx > 21:
            print(f"Warp detected! Exited pocket. Current position: ({cx}, {cy})")
            break
            
        # Adjust direction at the boundaries
        if cx == 17:
            direction = "Right"
        elif cx == 21:
            direction = "Left"
            
        print(f"Step {step_count}: At ({cx}, {cy}), walking {direction}")
        bridge.press_buttons([direction, "sleep 150"])
        step_count += 1

if __name__ == "__main__":
    burn_robust()
