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
    print("Executing B3F to B4F Western Room stairs...")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk Down 3 to (21, 25)
    print("Walking Down 3 steps to (21, 25)...")
    move("Down", 3)
    verify_position((21, 25), wait_time=0.5)

    # 2. Walk Left 5 to (16, 25)
    print("Walking Left 5 steps to (16, 25)...")
    move("Left", 5)
    verify_position((16, 25), wait_time=0.5)

    # 3. Walk Up 12 to (16, 13)
    print("Walking Up 12 steps to (16, 13)...")
    move("Up", 12)
    verify_position((16, 13), wait_time=0.5)

    # 4. Walk Right 3 to (19, 13)
    print("Walking Right 3 steps to (19, 13)...")
    move("Right", 3)
    verify_position((19, 13), wait_time=0.5)

    # 5. Walk Down 5 steps onto stairs at (19, 18) -> warp to B4F (19, 10)
    print("Walking Down 5 steps onto (19, 18) stairs...")
    move("Down", 5)
    verify_position((19, 10), wait_time=4.0)

    # 6. On B4F, walk to Giovanni's Gate at (25, 7)
    print("On B4F, walking Down 6 steps to (19, 16)...")
    move("Down", 6)
    verify_position((19, 16), wait_time=0.5)

    print("Walking Right 6 steps to (25, 16)...")
    move("Right", 6)
    verify_position((25, 16), wait_time=0.5)

    print("Walking Up 9 steps to (25, 7)...")
    move("Up", 9)
    verify_position((25, 7), wait_time=0.5)

    # 7. Turn Left to face the gate
    print("Turning Left to face the gate...")
    mgba.press_buttons(["Left", "sleep 300"])
    time.sleep(0.4)

    print("Successfully reached Giovanni's Gate at (25, 7) and faced Left!")
    mgba.take_screenshot()

except Exception as e:
    print("ERROR:", e)
    mgba.take_screenshot()
