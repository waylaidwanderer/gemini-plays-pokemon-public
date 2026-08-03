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
    print("Resuming master navigation from B3F (15, 18)...")
    print("Initial Position:", mgba.get_coordinates())
    
    # We are at B3F (15, 18)
    # 6. Walk Left to (14, 18)
    print("Walking Left to (14, 18)...")
    move("Left", 1)
    verify_position((14, 18), wait_time=0.5)

    # 7. Stepping Left onto (13, 18) LEFT spinner -> slides to (11, 20)
    print("Stepping Left onto (13, 18) LEFT spinner...")
    move("Left", 1)
    verify_position((11, 20), wait_time=3.0)

    # 8. Walk Right to (14, 20)
    print("Walking Right to (14, 20)...")
    move("Right", 3)
    verify_position((14, 20), wait_time=0.5)

    # 9. Walk Down to (14, 22)
    print("Walking Down to (14, 22)...")
    move("Down", 2)
    verify_position((14, 22), wait_time=0.5)

    # 10. Stepping Left onto (13, 22) LEFT spinner -> slides to (9, 24)
    print("Stepping Left onto (13, 22) LEFT spinner...")
    move("Left", 1)
    verify_position((9, 24), wait_time=3.0)

    # 11. Walk Right to (10, 24)
    print("Walking Right to (10, 24)...")
    move("Right", 1)
    verify_position((10, 24), wait_time=0.5)

    # 12. Stepping Down onto (10, 25) RIGHT spinner -> slides to (14, 25)
    print("Stepping Down onto (10, 25) RIGHT spinner...")
    move("Down", 1)
    verify_position((14, 25), wait_time=3.0)

    # 13. Walk Right to (21, 25)
    print("Walking Right to (21, 25)...")
    move("Right", 7)
    verify_position((21, 25), wait_time=0.5)

    # 14. Walking Up onto B3F stairs at (21, 22)...
    print("Walking Up onto B3F stairs at (21, 22)...")
    move("Up", 3)
    # Warps to B4F (21, 24) spawning at (21, 25)
    time.sleep(4.0)
    print("Position on B4F:", mgba.get_coordinates())

    # 15. Navigate B4F to Giovanni's Gate
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
