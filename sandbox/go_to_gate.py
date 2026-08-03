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
    print("Executing revised B3F to B4F Western Room stairs navigation...")
    print("Initial Position:", mgba.get_coordinates())
    
    # We are at B3F (19, 25)
    # 1. Walk Up 4 steps to (19, 21)
    print("Walking Up 4 steps to (19, 21)...")
    move("Up", 4)
    verify_position((19, 21), wait_time=0.5)

    # 2. Walk Left 3 steps to (16, 21) via (18, 21) gap
    print("Walking Left 3 steps to (16, 21)...")
    move("Left", 3)
    verify_position((16, 21), wait_time=0.5)

    # 3. Walk Up 8 steps to (16, 13)
    print("Walking Up 8 steps to (16, 13)...")
    move("Up", 8)
    verify_position((16, 13), wait_time=2.0) # wait for spinner slide to complete!

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
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
