import mgba
import time

def test_room():
    print("Starting room exploration to map walkable tiles...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    start_pos = mgba.get_coordinates()
    print("Start position:", start_pos)
    
    # Let's try to walk to all adjacent tiles from current position (23, 10)
    # We will step in a direction, log the new position, and if we moved, step back.
    directions = ["Up", "Right", "Down", "Left"]
    walkable = []
    
    for d in directions:
        print(f"Testing direction: {d}")
        mgba.press_buttons([d])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        
        if pos != start_pos:
            print(f"Tile {d} is walkable! Reached: {pos}")
            walkable.append((d, pos))
            # Step back
            opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
            mgba.press_buttons([opposite])
            time.sleep(0.4)
        else:
            print(f"Tile {d} is blocked!")
            
    print("Walkable adjacent tiles from (23, 10):", walkable)
    mgba.take_screenshot()

if __name__ == "__main__":
    test_room()
