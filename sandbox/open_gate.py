import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

def verify_position(expected_coords, wait_time=3.0):
    time.sleep(wait_time)
    pos = mgba.get_coordinates()
    print(f"  Coordinates: {pos} (expected: {expected_coords})")
    if (pos['x'], pos['y']) != expected_coords:
        raise ValueError(f"COORDINATE DESYNC! Expected {expected_coords}, got {pos}")
    return pos

try:
    print("Opening Giovanni's Gate at B4F...")
    print("Initial Position:", mgba.get_coordinates())
    
    # We are at (25, 15)
    # 1. Walk Up 8 steps to (25, 7)
    print("Walking Up 8 steps to (25, 7)...")
    move("Up", 8)
    verify_position((25, 7), wait_time=0.5)

    # 2. Turn Left to face the gate at (24, 7)
    print("Facing Left...")
    mgba.press_buttons(["Left", "sleep 300"])
    time.sleep(0.4)

    # 3. Press A to unlock the gate
    print("Interacting with the gate...")
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000"])
    time.sleep(3.0)

    # 4. Walk Left 3 steps into Giovanni's room
    print("Walking Left into Giovanni's room...")
    move("Left", 3)
    
    print("Current Position inside Giovanni's room:", mgba.get_coordinates())
    mgba.take_screenshot()

except Exception as e:
    print("ERROR:", e)
    mgba.take_screenshot()
