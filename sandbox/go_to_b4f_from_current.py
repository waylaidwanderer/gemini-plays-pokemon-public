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
    print("Starting B3F recovery script from:", mgba.get_coordinates())
    
    # Current is (28, 15)
    # 1. Walk Up to (28, 14)
    print("Walking Up to (28, 14)...")
    move("Up", 1)
    verify_position((28, 14), wait_time=0.5)

    # 2. Walk Left 6 to (22, 14)
    print("Walking Left 6 to (22, 14)...")
    move("Left", 6)
    verify_position((22, 14), wait_time=0.5)

    # 3. Walk Up 1 to (22, 13)
    print("Walking Up 1 to (22, 13)...")
    move("Up", 1)
    verify_position((22, 13), wait_time=0.5)

    # 4. Walk Left 6 to (16, 13)
    print("Walking Left 6 to (16, 13)...")
    move("Left", 6)
    verify_position((16, 13), wait_time=0.5)

    # 5. Walk Down 5 to (16, 18)
    print("Walking Down 5 to (16, 18)...")
    move("Down", 5)
    verify_position((16, 18), wait_time=0.5)

    # 6. Walk Left 1 to (15, 18)
    print("Walking Left 1 to (15, 18)...")
    move("Left", 1)
    verify_position((15, 18), wait_time=0.5)

    # 7. Walk Left 2 onto (13, 18) LEFT spinner -> slides to (11, 20)
    print("Walking Left 2 onto (13, 18) LEFT spinner...")
    move("Left", 2)
    verify_position((11, 20), wait_time=2.0)

    # 8. Walk Right 3 to (14, 20)
    print("Walking Right 3 to (14, 20)...")
    move("Right", 3)
    verify_position((14, 20), wait_time=0.5)

    # 9. Walk Down 2 to (14, 22)
    print("Walking Down 2 to (14, 22)...")
    move("Down", 2)
    verify_position((14, 22), wait_time=0.5)

    # 10. Walk Left 1 onto (13, 22) LEFT spinner -> slides to (9, 24)
    print("Stepping Left onto (13, 22) LEFT spinner...")
    move("Left", 1)
    verify_position((9, 24), wait_time=2.0)

    # 11. Walk Right 1 to (10, 24)
    print("Walking Right 1 to (10, 24)...")
    move("Right", 1)
    verify_position((10, 24), wait_time=0.5)

    # 12. Walk Down 1 onto (10, 25) RIGHT spinner -> slides to (14, 25)
    print("Stepping Down onto (10, 25) RIGHT spinner...")
    move("Down", 1)
    verify_position((14, 25), wait_time=2.0)

    # 13. Walk Right 7 to (21, 25)
    print("Walking Right 7 to (21, 25)...")
    move("Right", 7)
    verify_position((21, 25), wait_time=0.5)

    # 14. Walk Up 3 to (21, 22) stairs -> warps to B4F (21, 24)
    print("Walking Up 3 steps onto B3F stairs at (21, 22)...")
    move("Up", 3)
    verify_position((21, 24), wait_time=4.0)

    print("SUCCESSFULLY REACHED B4F EASTERN ROOM!")
    mgba.take_screenshot()

except ValueError as e:
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
