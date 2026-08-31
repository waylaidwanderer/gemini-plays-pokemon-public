import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Initial Position on 3F West:", pos)
    
    # Path to (2, 6)
    path = [
        (4, 11),
        (3, 11),
        (2, 11),
        (2, 10),
        (2, 9),
        (2, 8),
        (2, 7),
        (2, 6)
    ]
    
    for tx, ty in path:
        cx, cy = mgba.get_coordinates()['x'], mgba.get_coordinates()['y']
        direction = None
        if tx > cx: direction = "Right"
        elif tx < cx: direction = "Left"
        elif ty > cy: direction = "Down"
        elif ty < cy: direction = "Up"
        
        if direction is not None:
            print(f"Current: ({cx}, {cy}) | Heading to: ({tx}, {ty}) via {direction}")
            mgba.press_buttons([direction])
            time.sleep(0.5)
            
    # Now stand at (2, 6) and face UP
    print("Facing Up to look at the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch (4 A-presses)
    print("Toggling Mewtwo Switch...")
    for press in range(1, 5):
        print(f"A-press {press}...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
    print("Successfully toggled switch to State B!")
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
