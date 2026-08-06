import mgba

def probe():
    start_pos = mgba.get_coordinates()
    print("Start position:", start_pos)
    
    # Ensure we are at Row 5
    if start_pos['y'] == 7:
        mgba.press_buttons(["Up", "sleep 150", "Up", "sleep 150"])
    
    current = mgba.get_coordinates()
    print("At Row 5:", current)
    
    for c in range(current['x'], 0, -1):
        curr_pos = mgba.get_coordinates()
        print(f"\n--- Testing column x={curr_pos['x']} ---")
        
        # Test Down 1
        mgba.press_buttons(["Down", "sleep 150"])
        p1 = mgba.get_coordinates()
        print(f"Step Down 1 -> {p1}")
        if p1['y'] > 12 or p1['x'] != curr_pos['x'] or p1['y'] < 3:
            print(f"=== WARP DETECTED at {p1} ===")
            mgba.take_screenshot()
            return
            
        # Test Down 2
        mgba.press_buttons(["Down", "sleep 150"])
        p2 = mgba.get_coordinates()
        print(f"Step Down 2 -> {p2}")
        if p2['y'] > 12 or p2['x'] != curr_pos['x'] or p2['y'] < 3:
            print(f"=== WARP DETECTED at {p2} ===")
            mgba.take_screenshot()
            return
            
        # Return to Row 5 and move Left
        mgba.press_buttons(["Up", "sleep 150", "Up", "sleep 150", "Left", "sleep 150"])

probe()
