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
    print("Starting B2F to B3F pocket transition...")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk Down 7 to (25, 14)
    print("Walking Down 7 to (25, 14)...")
    move("Down", 7)
    verify_position((25, 14), wait_time=0.5)

    # 2. Walk Left 4 to (21, 14)
    print("Walking Left 4 to (21, 14)...")
    move("Left", 4)
    verify_position((21, 14), wait_time=0.5)

    # 3. Walk Up 3 to (21, 11)
    print("Walking Up 3 to (21, 11)...")
    move("Up", 3)
    verify_position((21, 11), wait_time=0.5)

    # 4. Walk Left 3 to (18, 11)
    print("Walking Left 3 to (18, 11)...")
    move("Left", 3)
    verify_position((18, 11), wait_time=0.5)

    # 5. Walk Left 1 onto (17, 11) LEFT spinner -> slides to (2, 9)
    print("Stepping Left onto (17, 11) LEFT spinner...")
    move("Left", 1)
    verify_position((2, 9), wait_time=2.0)

    # 6. Walk Right 1 onto (3, 9) hole -> falls to B3F (3, 9)
    print("Stepping Right onto (3, 9) hole...")
    move("Right", 1)
    verify_position((3, 9), wait_time=4.0) # Wait for falling transition

    print("SUCCESSFULLY REACHED B3F POCKET!")
    mgba.take_screenshot()

except Exception as e:
    print("ERROR:", e)
    mgba.take_screenshot()
