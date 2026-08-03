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
    print("Navigating from B2F (2, 9) to Giovanni's Gate...")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk Right 1 to (3, 9), Down 4 to (3, 13), Right 1 onto B3F stairs at (4, 13)
    print("Walking Right to (3, 9)...")
    move("Right", 1)
    verify_position((3, 9), wait_time=0.5)

    print("Walking Down 4 to (3, 13)...")
    move("Down", 4)
    verify_position((3, 13), wait_time=0.5)

    print("Walking Right 1 onto B3F stairs...")
    move("Right", 1)
    # Warps to B3F (5, 15) spawning at (5, 15) facing Down
    time.sleep(4.0)
    print("Position on B3F:", mgba.get_coordinates())

    # 2. On B3F: Walk Right 9 to (14, 15), Up 2 to (14, 13), Right 5 to (19, 13), Down 5 onto stairs at (19, 18)
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

    # 3. On B4F: Walk Right 6 to (25, 15), Up 8 to (25, 7), Turn Left to face the gate
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
    print("ERROR:", e)
    mgba.take_screenshot()
