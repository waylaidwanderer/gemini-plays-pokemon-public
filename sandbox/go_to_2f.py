import mgba
import time

def walk_to_stairs():
    print("Walking to stairs at (5, 10) on 3F...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Initial pos:", pos)
    
    # Walk left to column 5
    for x in range(pos['x'] - 1, 4, -1):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        curr = mgba.get_coordinates()
        print(f"Moved Left: {curr}")
        if curr['x'] == 5 and curr['y'] == 10:
            print("Arrived at stairs!")
            break
            
    # Step onto the stairs tile (usually triggers on entry, or need one more step)
    time.sleep(1.0)
    final_pos = mgba.get_coordinates()
    print("Final position after warp attempt:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    walk_to_stairs()
