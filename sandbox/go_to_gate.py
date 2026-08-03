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
    print("Walking from B4F (21, 17) to Giovanni's Gate at (25, 7)...")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk Down 8 steps to (21, 25)
    move("Down", 8)
    verify_position((21, 25), wait_time=0.5)

    # 2. Walk Right 4 steps to (25, 25)
    move("Right", 4)
    verify_position((25, 25), wait_time=0.5)

    # 3. Walk Up 18 steps to (25, 7)
    move("Up", 18)
    verify_position((25, 7), wait_time=0.5)

    # 4. Turn Left to face the gate
    mgba.press_buttons(["Left", "sleep 300"])
    time.sleep(0.4)
    
    print("Successfully reached Giovanni's Gate at (25, 7) and faced Left!")
    mgba.take_screenshot()

except Exception as e:
    print("ERROR:", e)
    mgba.take_screenshot()
