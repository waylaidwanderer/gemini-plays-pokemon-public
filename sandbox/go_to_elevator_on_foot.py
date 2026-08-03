import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

def verify_position(expected_coords, wait_time=1.0):
    time.sleep(wait_time)
    pos = mgba.get_coordinates()
    print(f"  Coordinates: {pos} (expected: {expected_coords})")
    if (pos['x'], pos['y']) != expected_coords:
        raise ValueError(f"COORDINATE DESYNC! Expected {expected_coords}, got {pos}")
    return pos

try:
    print("=== Step 1: Navigating B4F to B3F ===")
    print("Current Position on B4F:", mgba.get_coordinates())
    
    # We are at (19, 17)
    # Walk Right 2 steps to (21, 17)
    print("Walking Right 2 to (21, 17)...")
    move("Right", 2)
    verify_position((21, 17), wait_time=0.5)
    
    # Walk Down 7 steps to (21, 24) to warp to B3F
    print("Walking Down 7 steps to warp...")
    move("Down", 7)
    
    time.sleep(3.0)
    print("Spawned on B3F. Current Position:", mgba.get_coordinates())
    # Note: coming UP B4F (21, 24) spawns us on B3F at (21, 26) or (21, 22)? Let's check
    pos = mgba.get_coordinates()
    if pos['x'] != 21:
        raise ValueError(f"Unexpected spawn column on B3F: {pos}")
        
    print("=== Step 2: Navigating B3F to B2F ===")
    # We want to go to row 7 on B3F
    # From current y-coord to row 7
    dist_y = pos['y'] - 7
    print(f"Walking Up {dist_y} steps to row 7...")
    move("Up", dist_y)
    verify_position((21, 7), wait_time=0.5)
    
    # Walk Right 4 steps to (25, 7)
    print("Walking Right 4 to (25, 7)...")
    move("Right", 4)
    verify_position((25, 7), wait_time=0.5)
    
    # Walk Up 1 step onto B3F (25, 6) stairs to warp UP to B2F
    print("Walking Up 1 onto stairs to warp...")
    move("Up", 1)
    
    time.sleep(3.0)
    print("Spawned on B2F. Current Position:", mgba.get_coordinates())
    
    # On B2F, we should spawn around (21, 8)
    verify_position((21, 8), wait_time=1.0)
    
    print("=== Step 3: Navigating B2F to Elevator door ===")
    # Walk Down 6 steps to (21, 14)
    print("Walking Down 6 to (21, 14)...")
    move("Down", 6)
    verify_position((21, 14), wait_time=0.5)
    
    # Walk Right 3 steps to (24, 14)
    print("Walking Right 3 to (24, 14)...")
    move("Right", 3)
    verify_position((24, 14), wait_time=0.5)
    
    # Face UP (just in case)
    print("Facing UP...")
    mgba.press_buttons(["Up", "sleep 300"])
    time.sleep(0.4)
    
    print("SUCCESS: Standing in front of elevator doors on B2F at (24, 14)!")
    mgba.take_screenshot()

except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
