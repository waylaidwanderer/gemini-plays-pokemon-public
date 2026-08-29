import mgba
import time

def main():
    print("probe_drop: Testing walking DOWN from (26, 3) in State B...")
    pos = mgba.get_coordinates()
    print(f"Start coordinates: {pos}")
    
    # Try to step Down to (26, 4)
    print("Stepping Down to (26, 4)...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Coordinates after Down: {pos}")
    if pos['y'] != 4:
        print("We fell or moved elsewhere!")
        return
        
    # Try to step Down to (26, 5)
    print("Stepping Down to (26, 5)...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Coordinates after Down: {pos}")
    if pos['y'] != 5:
        print("We fell or moved elsewhere!")
        return
        
    # Try to step Down to (26, 6)
    print("Stepping Down to (26, 6)...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Coordinates after Down: {pos}")
    
if __name__ == "__main__":
    main()
