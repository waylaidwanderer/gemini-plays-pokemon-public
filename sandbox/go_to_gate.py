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
    print("Walking to Giovanni's Gate at B4F (25, 7)...")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk Up 9 steps to (21, 16)
    move("Up", 9)
    verify_position((21, 16), wait_time=0.5)

    # 2. Walk Right 4 steps to (25, 16)
    move("Right", 4)
    verify_position((25, 16), wait_time=0.5)

    # 3. Walk Up 9 steps to (25, 7)
    move("Up", 9)
    verify_position((25, 7), wait_time=0.5)

    # 4. Turn Left to face the gate at (24, 7)
    # In Gen 1, just pressing Left will turn us Left.
    mgba.press_buttons(["Left", "sleep 300"])
    time.sleep(0.4)
    
    print("Successfully reached (25, 7) and turned Left!")
    mgba.take_screenshot()

except Exception as e:
    print("ERROR:", e)
    mgba.take_screenshot()
