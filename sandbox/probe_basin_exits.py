import mgba

def try_step(direction):
    mgba.press_buttons([direction, "sleep 120"])
    return mgba.get_coordinates()

def main():
    pos = mgba.get_coordinates()
    print(f"Initial Position: {pos}")
    
    exits = []
    
    # Test sweep along y=14
    for x in range(28, 54):
        # Move to (x, 14)
        c = mgba.get_coordinates()
        while c['x'] < x: c = try_step("Right")
        while c['x'] > x: c = try_step("Left")
        while c['y'] < 14: c = try_step("Down")
        while c['y'] > 14: c = try_step("Up")
        
        # Test UP
        nxt = try_step("Up")
        if nxt['y'] < 14 or nxt['x'] != x:
            print(f"SUCCESS EXIT UP at ({x}, 14) -> {nxt}")
            exits.append((x, 14, "Up", nxt))
            # Step back
            c = mgba.get_coordinates()
            while c['y'] < 14: c = try_step("Down")
            
        # If x == 28, test LEFT
        if x == 28:
            nxt = try_step("Left")
            if nxt['x'] < 28:
                print(f"SUCCESS EXIT LEFT at (28, 14) -> {nxt}")
                exits.append((28, 14, "Left", nxt))
                c = mgba.get_coordinates()
                while c['x'] < 28: c = try_step("Right")

        # If x == 53, test RIGHT
        if x == 53:
            nxt = try_step("Right")
            if nxt['x'] > 53:
                print(f"SUCCESS EXIT RIGHT at (53, 14) -> {nxt}")
                exits.append((53, 14, "Right", nxt))
                c = mgba.get_coordinates()
                while c['x'] > 53: c = try_step("Left")

    # Test sweep along y=15
    for x in range(28, 54):
        # Move to (x, 15)
        c = mgba.get_coordinates()
        while c['x'] < x: c = try_step("Right")
        while c['x'] > x: c = try_step("Left")
        while c['y'] < 15: c = try_step("Down")
        while c['y'] > 15: c = try_step("Up")
        
        # Test DOWN
        nxt = try_step("Down")
        if nxt['y'] > 15 or nxt['x'] != x:
            print(f"SUCCESS EXIT DOWN at ({x}, 15) -> {nxt}")
            exits.append((x, 15, "Down", nxt))
            c = mgba.get_coordinates()
            while c['y'] > 15: c = try_step("Up")

        # If x == 28, test LEFT
        if x == 28:
            nxt = try_step("Left")
            if nxt['x'] < 28:
                print(f"SUCCESS EXIT LEFT at (28, 15) -> {nxt}")
                exits.append((28, 15, "Left", nxt))
                c = mgba.get_coordinates()
                while c['x'] < 28: c = try_step("Right")

        # If x == 53, test RIGHT
        if x == 53:
            nxt = try_step("Right")
            if nxt['x'] > 53:
                print(f"SUCCESS EXIT RIGHT at (53, 15) -> {nxt}")
                exits.append((53, 15, "Right", nxt))
                c = mgba.get_coordinates()
                while c['x'] > 53: c = try_step("Left")

    print("\n=== SWEEP COMPLETED ===")
    print(f"Total exits found: {len(exits)}")
    for e in exits:
        print(f"Exit: From {e[0]},{e[1]} dir {e[2]} -> {e[3]}")

if __name__ == "__main__":
    main()
