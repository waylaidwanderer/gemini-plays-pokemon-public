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
    print("Executing master navigation to Giovanni's Gate via B3F Western Stairs...")
    print("Initial Position on B4F:", mgba.get_coordinates())
    
    # 1. Walk to B4F stairs at (21, 24)
    # Current is (19, 17)
    print("Walking Right to (21, 17)...")
    move("Right", 2)
    verify_position((21, 17), wait_time=0.5)

    print("Walking Down 7 steps to warp UP to B3F...")
    move("Down", 7)
    # Warps UP to B3F (21, 24)
    verify_position((21, 24), wait_time=4.0)

    # 2. On B3F, walk from (21, 24) to Western stairs at (19, 18)
    print("On B3F, walking Down 1 step to (21, 25)...")
    move("Down", 1)
    verify_position((21, 25), wait_time=0.5)

    print("Walking Left 7 steps to (14, 25)...")
    move("Left", 7)
    verify_position((14, 25), wait_time=0.5)

    print("Walking Up 7 steps to (14, 18)...")
    move("Up", 7)
    verify_position((14, 18), wait_time=0.5)

    print("Walking Right 5 steps to Western stairs at (19, 18) -> warp to B4F...")
    move("Right", 5)
    # Warps DOWN to B4F (19, 10)
    verify_position((19, 10), wait_time=4.0)

    # 3. On B4F, walk to Giovanni's Gate at (25, 7)
    print("On B4F, walking Down 6 steps to (19, 16)...")
    move("Down", 6)
    verify_position((19, 16), wait_time=0.5)

    print("Walking Right 6 steps to (25, 16)...")
    move("Right", 6)
    verify_position((25, 16), wait_time=0.5)

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
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
