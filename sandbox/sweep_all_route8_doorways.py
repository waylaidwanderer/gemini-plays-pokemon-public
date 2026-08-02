import mgba

def try_step(direction):
    mgba.press_buttons([direction, "sleep 100"])
    return mgba.get_coordinates()

def main():
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    exits = []
    
    # Sweep x from 28 to 53 along y=14 and y=15
    for y in [14, 15]:
        for x in range(28, 54):
            # Nav to (x, y)
            c = mgba.get_coordinates()
            while c['x'] < x:
                nxt = try_step("Right")
                if nxt == c: break
                c = nxt
            while c['x'] > x:
                nxt = try_step("Left")
                if nxt == c: break
                c = nxt
            while c['y'] < y:
                nxt = try_step("Down")
                if nxt == c: break
                c = nxt
            while c['y'] > y:
                nxt = try_step("Up")
                if nxt == c: break
                c = nxt
            
            c = mgba.get_coordinates()
            if c['x'] != x or c['y'] != y:
                continue
                
            # Test all 4 directions
            for d in ["Up", "Left", "Down", "Right"]:
                nxt = try_step(d)
                if nxt['x'] != x or nxt['y'] != y:
                    if nxt['x'] < 28 or nxt['x'] > 53 or nxt['y'] < 14 or nxt['y'] > 15:
                        print(f"!!! EXIT FOUND !!! From ({x}, {y}) dir {d} -> {nxt}")
                        exits.append((x, y, d, nxt))
                    # Step back to (x, y)
                    c = mgba.get_coordinates()
                    while c['x'] < x: try_step("Right"); c = mgba.get_coordinates()
                    while c['x'] > x: try_step("Left"); c = mgba.get_coordinates()
                    while c['y'] < y: try_step("Down"); c = mgba.get_coordinates()
                    while c['y'] > y: try_step("Up"); c = mgba.get_coordinates()

    print("\n=== SWEEP COMPLETED ===")
    print(f"Total exits found: {len(exits)}")
    for e in exits:
        print(f"Exit: {e}")

if __name__ == "__main__":
    main()
