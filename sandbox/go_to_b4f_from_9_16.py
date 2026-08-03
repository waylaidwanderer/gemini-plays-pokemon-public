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
    print("Starting B3F to B4F final navigation from:", mgba.get_coordinates())
    
    # We are at (9, 16)
    # 1. Walk Right 1 step to (10, 16)
    print("Walking to (10, 16)...")
    move("Right", 1)
    verify_position((10, 16), wait_time=0.5)

    # 2. Walk Right 1 step onto (11, 16) RIGHT spinner -> slides to (15, 18)
    print("Stepping onto (11, 16) RIGHT spinner...")
    move("Right", 1)
    verify_position((15, 18), wait_time=2.0)

    # 3. Walk Left 1 step to (14, 18)
    print("Walking to (14, 18)...")
    move("Left", 1)
    verify_position((14, 18), wait_time=0.5)

    # 4. Walk Left 1 step onto (13, 18) LEFT spinner -> slides to (11, 20)
    print("Stepping onto (13, 18) LEFT spinner...")
    move("Left", 1)
    verify_position((11, 20), wait_time=2.0)

    # 5. Walk Right 3 steps to (14, 20)
    print("Walking to (14, 20)...")
    move("Right", 3)
    verify_position((14, 20), wait_time=0.5)

    # 6. Walk Down 2 steps to (14, 22)
    print("Walking to (14, 22)...")
    move("Down", 2)
    verify_position((14, 22), wait_time=0.5)

    # 7. Walk Left 1 step onto (13, 22) LEFT spinner -> slides to (9, 24)
    print("Stepping onto (13, 22) LEFT spinner...")
    move("Left", 1)
    verify_position((9, 24), wait_time=2.0)

    # 8. Walk Right 1 step to (10, 24)
    print("Walking to (10, 24)...")
    move("Right", 1)
    verify_position((10, 24), wait_time=0.5)

    # 9. Walk Down 1 step onto (10, 25) RIGHT spinner -> slides to (14, 25)
    print("Stepping onto (10, 25) RIGHT spinner...")
    move("Down", 1)
    verify_position((14, 25), wait_time=2.0)

    # 10. Walk Right 7 steps to (21, 25)
    print("Walking to (21, 25)...")
    move("Right", 7)
    verify_position((21, 25), wait_time=0.5)

    # 11. Walk Up 3 steps onto stairs at (21, 22) -> warps to B4F (21, 24)
    print("Walking Up 3 steps onto B3F stairs at (21, 22)...")
    move("Up", 3)
    verify_position((21, 24), wait_time=4.0)

    print("SUCCESSFULLY REACHED B4F!")
    mgba.take_screenshot()

except Exception as e:
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
