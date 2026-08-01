import mgba

def probe_basin():
    print("=== MASTER BASIN PROBE STARTING ===")
    start_pos = mgba.get_coordinates()
    print(f"Start position: {start_pos}")

    found_north = []
    found_south = []

    # Current position is (28, 15)
    # We will probe columns 28 through 39
    for col in range(28, 40):
        pos = mgba.get_coordinates()
        curr_x = pos['x']
        
        # Navigate horizontally to target col on Row 15
        if curr_x < col:
            mgba.press_buttons(["Right"] * (col - curr_x))
        elif curr_x > col:
            mgba.press_buttons(["Left"] * (curr_x - col))
            
        pos = mgba.get_coordinates()
        if pos['x'] != col or pos['y'] != 15:
            print(f"Col {col}: Could not reach (col, 15), current pos is {pos}")
            continue

        # Probe North (Up)
        mgba.press_buttons(["Up"]) # to (col, 14)
        pos_after_up1 = mgba.get_coordinates()
        
        if pos_after_up1['y'] == 14:
            # Try stepping Up into Row 13
            mgba.press_buttons(["Up"])
            pos_after_up2 = mgba.get_coordinates()
            if pos_after_up2['y'] < 14:
                print(f"*** NORTH GAP FOUND AT COL {col}: {pos_after_up2} ***")
                found_north.append((col, pos_after_up2))
                # Return to Row 15
                mgba.press_buttons(["Down", "Down"])
            else:
                # Bumped at Row 13, return to Row 15
                mgba.press_buttons(["Down"])
        else:
            print(f"Col {col}: Up into Row 14 blocked, pos {pos_after_up1}")

        # Probe South (Down)
        mgba.press_buttons(["Down"])
        pos_after_down = mgba.get_coordinates()
        if pos_after_down['y'] != 15 or pos_after_down['x'] != col:
            print(f"*** SOUTH DOORWAY/WARP FOUND AT COL {col}: {pos_after_down} ***")
            found_south.append((col, pos_after_down))

    print("\n=== PROBE RESULTS SUMMARY ===")
    print(f"North Gaps: {found_north}")
    print(f"South Warps/Passages: {found_south}")

if __name__ == "__main__":
    probe_basin()
