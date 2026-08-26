import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # We are at (5, 15) on 1F West. Walk UP to (5, 10)
    print("Walking up Column 5...")
    while pos["y"] > 10:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("Current position:", pos)
        
    # Warp UP to 2F West
    print("Warping to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Landed on 2F West:", pos)
    
    # Let's walk to the stairs to 3F West: (7, 10)
    print("Walking to (7, 10) on 2F West...")
    if pos == {"x": 5, "y": 11}:
        mgba.press_buttons(["Up", "sleep 400", "Right", "sleep 400", "Right", "sleep 400"])
        time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("At 2F West stairs approach:", pos)
    
    # Warp UP to 3F West
    print("Warping to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Landed on 3F West:", pos)

if __name__ == "__main__":
    main()
