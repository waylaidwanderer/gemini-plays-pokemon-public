import bridge

def burn_fast_safe():
    # Start at current position
    # Let's read current coordinates
    pos = bridge.get_coordinates()
    if pos is None:
        print("Could not get position.")
        return
    cx, cy = pos
    print(f"Starting at: ({cx}, {cy})")
    
    # We will burn exactly 20 steps (40 actions)
    # Each step is either Left or Right depending on where we are
    buttons = []
    curr_x = cx
    direction = "Right" if cx == 17 else "Left"
    
    for _ in range(20):
        if curr_x == 17:
            direction = "Right"
        elif curr_x == 21:
            direction = "Left"
            
        buttons.extend([direction, "sleep 150"])
        if direction == "Right":
            curr_x += 1
        else:
            curr_x -= 1
            
    print(f"Sending sequence of {len(buttons)} actions to burn 30 steps safely...")
    res = bridge.press_buttons(buttons)
    print(f"Response: {res}")
    print(f"New coordinates: {bridge.get_coordinates()}")

if __name__ == "__main__":
    burn_fast_safe()
