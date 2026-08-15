import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to RUN
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    
    # Clear post-flee text
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
        
    pos = get_pos()
    print(f"Coordinates after battle handling: {pos}")
    return pos

def main():
    print("Running out Safari steps on Row 23 (Columns 2-17)...")
    
    # We will walk Left and Right on Row 23 between Column 2 and Column 17.
    direction = "Left" # Start by walking Left since we are at (17, 23)
    
    while True:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                continue
                
        # If we warped back to the Gatehouse (usually x near 3-4, y near 3-5)
        if pos[0] <= 10 and pos[1] <= 5:
            print(f"Successfully warped out of Safari Zone! Position: {pos}")
            break
            
        print(f"Current Position: {pos}. Walking {direction}...")
        
        # Check boundary to change direction
        if pos[0] >= 17 and direction == "Right":
            direction = "Left"
        elif pos[0] <= 3 and direction == "Left":
            direction = "Right"
            
        # Take a step robustly
        bridge.press_buttons([direction, "sleep 400"])
        time.sleep(0.3)
        
    print("Step depletion sequence finished.")

if __name__ == "__main__":
    main()
