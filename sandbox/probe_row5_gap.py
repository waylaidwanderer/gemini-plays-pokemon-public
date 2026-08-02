import mgba

print("Probing Row 5 ledge for UP gap from x=25 down to x=20...")
for x in range(25, 19, -1):
    pos = mgba.get_coordinates()
    print(f"Testing at pos={pos}")
    
    # Try UP
    mgba.press_buttons(["Up"])
    p_up = mgba.get_coordinates()
    if p_up['y'] < 6:
        print(f"*** FOUND UP PASSAGE AT x={pos['x']}! New pos: {p_up} ***")
        mgba.take_screenshot()
        break
        
    # Step Left
    mgba.press_buttons(["Left"])

print("Probe finished. Final pos:", mgba.get_coordinates())
