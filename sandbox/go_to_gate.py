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
    print("Executing ultimate Rocket Hideout speedrun to Giovanni's Gate...")
    print("Initial Position on B1F:", mgba.get_coordinates())
    
    # Phase 1: B1F to B2F
    # We are at (19, 3). Walk Right 4 to (23, 3), then Up 1 onto stairs at (23, 2)
    print("Walking Right 4 to (23, 3)...")
    move("Right", 4)
    verify_position((23, 3), wait_time=0.5)

    print("Walking Up 1 onto stairs to B2F...")
    move("Up", 1)
    # Warps to B2F (27, 8) spawning at (27, 9) facing Down
    time.sleep(4.0)
    print("Position on B2F:", mgba.get_coordinates())

    # Phase 2: B2F to B3F pocket
    # Current on B2F should be (27, 9) facing Down.
    # Walk Left 2 to (25, 9), Down 5 to (25, 14), Left 4 to (21, 14)
    print("Walking Left to (25, 9)...")
    move("Left", 2)
    verify_position((25, 9), wait_time=0.5)

    print("Walking Down 5 to (25, 14)...")
    move("Down", 5)
    verify_position((25, 14), wait_time=0.5)

    print("Walking Left 4 to (21, 14)...")
    move("Left", 4)
    verify_position((21, 14), wait_time=0.5)

    # Walk Up 3 to (21, 11), Left 3 to (18, 11), Left 1 onto (17, 11) LEFT spinner -> slides to (2, 9)
    print("Walking Up 3 to (21, 11)...")
    move("Up", 3)
    verify_position((21, 11), wait_time=0.5)

    print("Walking Left 3 to (18, 11)...")
    move("Left", 3)
    verify_position((18, 11), wait_time=0.5)

    print("Stepping Left onto (17, 11) LEFT spinner...")
    move("Left", 1)
    # Slides to B2F (2, 9)
    verify_position((2, 9), wait_time=3.0)

    # Walk Right 1 to (3, 9), Down 4 to (3, 13), Right 1 onto stairs at (4, 13)
    print("Walking Right to (3, 9)...")
    move("Right", 1)
    verify_position((3, 9), wait_time=0.5)

    print("Walking Down 4 to (3, 13)...")
    move("Down", 4)
    verify_position((3, 13), wait_time=0.5)

    print("Walking Right 1 onto B3F stairs...")
    move("Right", 1)
    # Warps to B3F (5, 15) spawning at (5, 15) facing Down/Right?
    time.sleep(4.0)
    print("Position on B3F:", mgba.get_coordinates())

    # Phase 3: B3F to B4F Western Room
    # Current on B3F is (5, 15).
    # Walk Right 9 to (14, 15), Up 2 to (14, 13), Right 5 to (19, 13), Down 5 onto stairs at (19, 18)
    print("Walking Right 9 to (14, 15)...")
    move("Right", 9)
    verify_position((14, 15), wait_time=0.5)

    print("Walking Up 2 to (14, 13)...")
    move("Up", 2)
    verify_position((14, 13), wait_time=0.5)

    print("Walking Right 5 to (19, 13)...")
    move("Right", 5)
    verify_position((19, 13), wait_time=0.5)

    print("Walking Down 5 onto (19, 18) stairs...")
    move("Down", 5)
    # Warps to B4F (19, 15) spawning at (19, 15) facing Down
    time.sleep(4.0)
    print("Position on B4F:", mgba.get_coordinates())

    # Phase 4: B4F to Giovanni's Gate
    # Current on B4F is (19, 15).
    # Walk Right 6 to (25, 15), Up 8 to (25, 7), Turn Left to face the gate at (24, 7)
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
