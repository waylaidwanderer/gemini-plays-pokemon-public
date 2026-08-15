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
    print("Running out Safari steps on Row 23...")
    
    # We will walk Left and Right on Row 23 between Column 2 and Column 25.
    direction = "Right"
    
    while True:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                # Still in dialogue or battle? Let's check if we warped to the Gatehouse.
                # Gatehouse coordinates are usually x around 3-4, y around 3-5.
                # But when dialogue "Ding-dong! Time's up!" is active, coordinates will be None.
                # So we continue clearing it.
                continue
                
        # If we warped back to the Gatehouse (x <= 10 and y >= 3)
        if pos[0] <= 10 and pos[1] <= 5:
            print(f"Successfully warped out of Safari Zone! Position: {pos}")
            break
            
        print(f"Current Position: {pos}. Walking {direction}...")
        
        # Check boundary to change direction
        if pos[0] >= 25 and direction == "Right":
            direction = "Left"
        elif pos[0] <= 3 and direction == "Left":
            direction = "Right"
            
        # Take a step robustly
        bridge.press_buttons([direction, "sleep 400"])
        time.sleep(0.3)
        
    print("Step depletion sequence finished.")

if __name__ == "__main__":
    main()
