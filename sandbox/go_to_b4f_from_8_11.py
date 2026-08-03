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
    print("Starting B3F navigation script from:", mgba.get_coordinates())
    
    # 1. Walk Right 2 steps to (10, 11)
    print("Walking Right 2 steps to (10, 11)...")
    move("Right", 2)
    verify_position((10, 11), wait_time=0.5)

    # 2. Walk Down 3 steps to (10, 14)
    print("Walking Down 3 steps to (10, 14)...")
    move("Down", 3)
    verify_position((10, 14), wait_time=0.5)

    # 3. Walk Left 1 step onto (9, 14) DOWN spinner -> slides to (9, 16)
    print("Stepping Left onto (9, 14) DOWN spinner...")
    move("Left", 1)
    verify_position((9, 16), wait_time=2.0)

    # 4. Walk Right 1 step to (10, 16)
    print("Walking Right 1 step to (10, 16)...")
    move("Right", 1)
    verify_position((10, 16), wait_time=0.5)

    # 5. Walk Right 1 step onto (11, 16) RIGHT spinner -> slides to (15, 18)
    print("Stepping Right onto (11, 16) RIGHT spinner...")
    move("Right", 1)
    verify_position((15, 18), wait_time=2.0)

    # 6. Walk Right 1 step onto (16, 18) UP spinner -> slides to (16, 13)
    print("Stepping Right onto (16, 18) UP spinner...")
    move("Right", 1)
    verify_position((16, 13), wait_time=2.0)

    # 7. Walk Right 12 steps to (28, 13)
    print("Walking Right 12 steps to (28, 13)...")
    move("Right", 12)
    verify_position((28, 13), wait_time=0.5)

    # 8. Walk Down 5 steps to (28, 18)
    print("Walking Down 5 steps to (28, 18)...")
    move("Down", 5)
    verify_position((28, 18), wait_time=0.5)

    # 9. Walk Left 9 steps to (19, 18) stairs -> warps to B4F (19, 10)
    print("Walking Left 9 steps to stairs at (19, 18)...")
    move("Left", 9)
    verify_position((19, 10), wait_time=4.0)

    print("SUCCESSFULLY REACHED B4F!")
    mgba.take_screenshot()

except ValueError as e:
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
