import mgba

print("=== PROBING EASTBOUND ROW 6 & UPPER HIGHWAY GAPS ===")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

for target_x in range(33, 46):
    curr = mgba.get_coordinates()
    while curr['x'] < target_x:
        mgba.press_buttons(["Right"])
        curr = mgba.get_coordinates()
    while curr['y'] < 6:
        mgba.press_buttons(["Down"])
        curr = mgba.get_coordinates()
        
    print(f"Testing at ({target_x}, {curr['y']})...")
    
    mgba.press_buttons(["Up"])
    pos_up = mgba.get_coordinates()
    if pos_up['y'] < curr['y']:
        print(f"SUCCESS! ASCENT FOUND AT ({target_x}, {curr['y']}) UP -> {pos_up}")
        c = pos_up
        while True:
            mgba.press_buttons(["Up"])
            c2 = mgba.get_coordinates()
            if c2['y'] < c['y']:
                c = c2
                print(f"  Climbed higher -> {c}")
            else:
                break
        for _ in range(15):
            mgba.press_buttons(["Right"])
            c_east = mgba.get_coordinates()
            print(f"  Top Highway East step -> {c_east}")

print("=== PROBE COMPLETE ===")
final_pos = mgba.get_coordinates()
print(f"Final pos: {final_pos}")
