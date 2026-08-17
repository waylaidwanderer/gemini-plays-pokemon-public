import mgba
import time

def run():
    print("--- WALKING LEFT ON ROW 21 ---")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # Let's walk Left up to 14 steps (which would place us at column 0 or transition us)
    for i in range(14):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        curr = mgba.get_coordinates()
        print(f"Step {i+1} Left: {curr}")
        # If the map name changes or coordinates reset, we know we transitioned!
        # But since get_coordinates doesn't return map name, we check if we went to a high x-coord (like Route 18)
        # or if we are blocked (x stopped changing).
        
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
