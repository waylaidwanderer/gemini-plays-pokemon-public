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
    print("Executing final master navigation to Giovanni's Gate via B3F...")
    print("Initial Position on B4F:", mgba.get_coordinates())
    
    # 1. Walk B4F (19, 17) to (21, 22) stairs to warp UP to B3F
    print("Walking Down 8 steps to (19, 25)...")
    move("Down", 8)
    verify_position((19, 25), wait_time=0.5)

    print("Walking Right 2 steps to (21, 25)...")
    move("Right", 2)
    verify_position((21, 25), wait_time=0.5)

    print("Walking Up 3 steps onto stairs...")
    move("Up", 3)
    # Warps to B3F (21, 22)
    time.sleep(4.0)
    print("Position on B3F:", mgba.get_coordinates())

    # 2. On B3F, navigate from (21, 22) to Western stairs (19, 18)
    print("On B3F, walking Down 3 to (21, 25)...")
    move("Down", 3)
    verify_position((21, 25), wait_time=0.5)

    print("Walking Left 2 to (19, 25)...")
    move("Left", 2)
    verify_position((19, 25), wait_time=0.5)

    print("Walking Up 4 to (19, 21)...")
    move("Up", 4)
    verify_position((19, 21), wait_time=0.5)

    print("Walking Left 3 to (16, 21)...")
    move("Left", 3)
    verify_position((16, 21), wait_time=0.5)

    print("Walking Up 8 to (16, 13)...")
    move("Up", 8)
    verify_position((16, 13), wait_time=2.0) # wait for slide to complete

    print("Walking Right 3 to (19, 13)...")
    move("Right", 3)
    verify_position((19, 13), wait_time=0.5)

    print("Walking Down 5 onto stairs...")
    move("Down", 5)
    # Warps to B4F (19, 15)
    time.sleep(4.0)
    print("Position on B4F (Above Row 16):", mgba.get_coordinates())

    # 3. Navigate B4F to Giovanni's Gate
    print("Walking Right 6 to (25, 15)...")
    move("Right", 6)
    verify_position((25, 15), wait_time=0.5)

    print("Walking Up 8 to (25, 7)...")
    move("Up", 8)
    verify_position((25, 7), wait_time=0.5)

    print("Facing Left at the gate...")
    mgba.press_buttons(["Left", "sleep 300"])
    time.sleep(0.4)

    print("SUCCESSFULLY REACHED GIOVANNI'S GATE!")
    mgba.take_screenshot()

except Exception as e:
    print("ERROR:", e)
    mgba.take_screenshot()
