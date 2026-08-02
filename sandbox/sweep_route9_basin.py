import mgba

print("Starting Route 9 Row 14 Probe...")
start_pos = mgba.get_coordinates()
print(f"Start position: {start_pos}")

for i in range(10):
    pos = mgba.get_coordinates()
    print(f"\n--- Checking x={pos['x']}, y={pos['y']} ---")
    
    # Try UP
    mgba.press_buttons(["Up"])
    p_up = mgba.get_coordinates()
    if p_up['y'] < 14:
        print(f"!!! SUCCESS UP PASSAGE FOUND at x={pos['x']}! Moved to {p_up} !!!")
        mgba.take_screenshot()
        break
    
    # Try DOWN
    mgba.press_buttons(["Down"])
    p_dn = mgba.get_coordinates()
    if p_dn['y'] > 14:
        # Check if we can go further down
        mgba.press_buttons(["Down"])
        p_dn2 = mgba.get_coordinates()
        if p_dn2['y'] > 15:
            print(f"!!! SUCCESS DOWN PASSAGE FOUND at x={pos['x']}! Moved to {p_dn2} !!!")
            mgba.take_screenshot()
            break
        else:
            # Return to row 14
            mgba.press_buttons(["Up"])
            
    # Move Right to next tile
    mgba.press_buttons(["Right"])

end_pos = mgba.get_coordinates()
print(f"\nEnd position: {end_pos}")
