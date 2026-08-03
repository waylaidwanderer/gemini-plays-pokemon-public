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
    print("Executing final Rocket Hideout master speedrun to Giovanni's Gate...")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. B2F to B3F via hole
    print("Walking Down 1 to (4, 14)...")
    move("Down", 1)
    verify_position((4, 14), wait_time=0.5)

    print("Stepping Right onto (5, 14) RIGHT spinner...")
    move("Right", 1)
    verify_position((8, 14), wait_time=2.0)

    print("Stepping Right onto (9, 14) hole...")
    move("Right", 1)
    # Falls to B3F (9, 16)
    time.sleep(4.0)
    print("Position on B3F:", mgba.get_coordinates())

    # 2. Navigate B3F to stairs
    print("Walking Right to (10, 16)...")
    move("Right", 1)
    verify_position((10, 16), wait_time=0.5)

    print("Stepping Right onto (11, 16) RIGHT spinner...")
    move("Right", 1)
    verify_position((15, 18), wait_time=3.0)

    print("Walking Left to (14, 18)...")
    move("Left", 1)
    verify_position((14, 18), wait_time=0.5)

    print("Stepping Left onto (13, 18) LEFT spinner...")
    move("Left", 1)
    verify_position((11, 20), wait_time=3.0)

    print("Walking Right to (14, 20)...")
    move("Right", 3)
    verify_position((14, 20), wait_time=0.5)

    print("Walking Down to (14, 22)...")
    move("Down", 2)
    verify_position((14, 22), wait_time=0.5)

    print("Stepping Left onto (13, 22) LEFT spinner...")
    move("Left", 1)
    verify_position((9, 24), wait_time=3.0)

    print("Walking Right to (10, 24)...")
    move("Right", 1)
    verify_position((10, 24), wait_time=0.5)

    print("Stepping Down onto (10, 25) RIGHT spinner...")
    move("Down", 1)
    verify_position((14, 25), wait_time=3.0)

    print("Walking Right to (21, 25)...")
    move("Right", 7)
    verify_position((21, 25), wait_time=0.5)

    print("Walking Up onto B3F stairs at (21, 22)...")
    move("Up", 3)
    # Warps to B4F (21, 24) spawning at (21, 25)
    time.sleep(4.0)
    print("Position on B4F:", mgba.get_coordinates())

    # 3. Navigate B4F to Giovanni's Gate
    print("On B4F, walking Up 4 to (21, 21)...")
    move("Up", 4)
    verify_position((21, 21), wait_time=0.5)

    print("Walking Left 2 to (19, 21)...")
    move("Left", 2)
    verify_position((19, 21), wait_time=0.5)

    print("Walking Up 6 to (19, 15)...")
    move("Up", 6)
    verify_position((19, 15), wait_time=0.5)

    print("Walking Right 6 to (25, 15)...")
    move("Right", 6)
    verify_position((25, 15), wait_time=0.5)

    print("Walking Up 8 to (25, 7)...")
    move("Up", 8)
    verify_position((25, 7), wait_time=0.5)

    print("Facing Left at the gate...")
    mgba.press_buttons(["Left", "sleep 300"])
    time.sleep(0.4)

    print("SUCCESSFULLY ARRIVED AT GIOVANNI'S GATE!")
    mgba.take_screenshot()

except Exception as e:
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
