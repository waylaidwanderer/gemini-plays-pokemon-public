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

# Standing at B3F (15, 18)
print("Starting B3F to B4F run from:", mgba.get_coordinates())

try:
    # 1. Walk Left 2 onto (13, 18) LEFT spinner -> slides to (11, 20) stopper
    print("Walking to (14, 18)...")
    move("Left", 1)
    print("Stepping Left onto (13, 18) LEFT spinner...")
    move("Left", 1)
    verify_position((11, 20))

    # 2. Walk Right 2 onto Row 20 Column 13, then Up onto (13, 19) LEFT spinner -> slides to (10, 18) stopper
    print("Walking to (13, 20)...")
    move("Right", 2)
    print("Stepping Up onto (13, 19) LEFT spinner...")
    move("Up", 1)
    verify_position((10, 18))

    # 3. Walk Up onto (10, 17) RIGHT spinner -> slides to (14, 17) UP spinner stopper
    print("Stepping Up onto (10, 17) RIGHT spinner...")
    move("Up", 1)
    verify_position((14, 17))

    # 4. Walk Up 2 steps to (14, 15)
    print("Walking Up 2 steps to (14, 15)...")
    move("Up", 2)
    verify_position((14, 15), wait_time=0.4)

    # 5. Walk to (16, 13) Right Room via (16, 14) UP spinner
    print("Walking to (16, 15)...")
    move("Right", 2)
    print("Stepping Up onto (16, 14) UP spinner...")
    move("Up", 1)
    verify_position((16, 13))

    # 6. Walk Column 28 path on B3F to stairs at (19, 18) -> warps to B4F (19, 10)
    print("Walking to B3F stairs...")
    move("Right", 12) # to (28, 13)
    move("Down", 5)   # to (28, 18)
    move("Left", 9)   # to (19, 18) stairs
    verify_position((19, 10), wait_time=4.0) # Wait for warp transition to B4F

    # 7. Walk B4F to the gate:
    # Down 6 from (19, 10) -> (19, 16)
    print("Walking Down 6 steps on B4F...")
    move("Down", 6)
    # Right 6 from (19, 16) -> (25, 16)
    print("Walking Right 6 steps on B4F...")
    move("Right", 6)
    # Up 9 from (25, 16) -> (25, 7)
    print("Walking Up 9 steps on B4F...")
    move("Up", 9)
    
    pos = verify_position((25, 7), wait_time=1.0)
    print("Successfully reached Giovanni's Gate at B4F (25, 7) on foot!")
    screenshot = mgba.take_screenshot()
    print("Screenshot on B4F:", screenshot)

except ValueError as e:
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
