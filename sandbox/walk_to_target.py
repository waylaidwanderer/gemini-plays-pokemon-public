import mgba
import time

def run_away():
    print("Attempting to run away from potential battle...")
    # Standard runaway sequence: Down, Right, A
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 1000"])
    # Clear text with B presses
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 300"])

def walk_east(target_x):
    print(f"Starting walk to target X={target_x}...")
    current = mgba.get_coordinates()
    print(f"Initial coordinates: {current}")
    
    stuck_count = 0
    while current['x'] < target_x:
        last_x = current['x']
        last_y = current['y']
        
        # Try to step Right
        mgba.press_buttons(["Right", "sleep 400"])
        current = mgba.get_coordinates()
        print(f"Tried Right. New coordinates: {current}")
        
        if current['x'] > last_x:
            # Successfully moved!
            stuck_count = 0
            continue
            
        # If we didn't move
        stuck_count += 1
        if stuck_count >= 2:
            print("Detected possible battle or obstacle. Trying runaway sequence...")
            run_away()
            current = mgba.get_coordinates()
            stuck_count = 0

walk_east(36)
print("Script finished.")
