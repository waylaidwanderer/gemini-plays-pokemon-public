import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def burn():
    print("Starting step burner in the isolated pocket of Safari Zone Center Row 24...")
    
    # We will walk back and forth between Column 17 and Column 21
    step_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            # Maybe a transition or dialog, wait a bit
            time.sleep(1.0)
            continue
            
        cx, cy = pos
        # If we are no longer in Safari Zone Center at row 24, we must have been warped!
        if cy != 24 or cx < 17 or cx > 21:
            print(f"Map transition or warp detected! Current position: ({cx}, {cy})")
            break
            
        # Decide next direction
        if cx == 17:
            direction = "Right"
        elif cx == 21:
            direction = "Left"
        else:
            # If we are in between, we can continue in the same direction or default to Right
            # Let's check if we were moving left or right, or just read position and move towards the other end
            # To be simple and robust, if we are at 18, 19, 20: we can check the previous position or just walk Right until we hit 21, then Left.
            # Actually, let's just alternate: if cx < 21, walk Right. If cx == 21, we will walk Left.
            # Wait, if we are at 18, walking Right takes us to 19.
            # If we are at 19, walking Right takes us to 20.
            # If we are at 20, walking Right takes us to 21.
            # If we are at 21, we walk Left to 20.
            # Wait! If we are at 20 and walk Left, we are at 19. If we then run the logic "if cx < 21 walk Right", we would walk Right back to 20!
            # That would cause us to oscillate between 20 and 21 forever!
            # To avoid this, let's keep track of our desired direction in a variable!
            pass

def burn_robust():
    direction = "Right"
    step_count = 0
    
    while True:
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
