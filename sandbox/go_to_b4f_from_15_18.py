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
    print("Starting B3F part 2 navigation script from:", mgba.get_coordinates())
    
    # 1. Walk Right 1 step onto (16, 18) UP spinner -> slides to (16, 13)
    print("Stepping Right onto (16, 18) UP spinner...")
    move("Right", 1)
    verify_position((16, 13), wait_time=3.0)

    # 2. Walk Right 12 steps to (28, 13)
    print("Walking Right 12 steps to (28, 13)...")
    move("Right", 12)
    verify_position((28, 13), wait_time=0.5)

    # 3. Walk Down 5 steps to (28, 18)
    print("Walking Down 5 steps to (28, 18)...")
    move("Down", 5)
    verify_position((28, 18), wait_time=0.5)

    # 4. Walk Left 9 steps to (19, 18) stairs -> warps to B4F (19, 10)
    print("Walking Left 9 steps to stairs at (19, 18)...")
    move("Left", 9)
    verify_position((19, 10), wait_time=4.0)

    print("SUCCESSFULLY REACHED B4F!")
    mgba.take_screenshot()

except ValueError as e:
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
