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
    print("Executing final B4F navigation to Giovanni's Gate...")
    print("Initial Position:", mgba.get_coordinates())
    
    # We are at (19, 15)
    # 1. Walk Down 1 step to (19, 16)
    print("Walking Down 1 step to (19, 16)...")
    move("Down", 1)
    verify_position((19, 16), wait_time=0.5)

    # 2. Walk Right 6 steps to (25, 16)
    print("Walking Right 6 steps to (25, 16)...")
    move("Right", 6)
    verify_position((25, 16), wait_time=0.5)

    # 3. Walk Up 9 steps to (25, 7)
    print("Walking Up 9 steps to (25, 7)...")
    move("Up", 9)
    verify_position((25, 7), wait_time=0.5)

    # 4. Turn Left to face the gate
    print("Turning Left to face the gate...")
    mgba.press_buttons(["Left", "sleep 300"])
    time.sleep(0.4)

    print("Successfully reached Giovanni's Gate at (25, 7) and faced Left!")
    mgba.take_screenshot()

except Exception as e:
    print("ERROR:", e)
    mgba.take_screenshot()
