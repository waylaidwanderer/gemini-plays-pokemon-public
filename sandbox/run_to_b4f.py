import mgba
import time

# Robust, self-validating path runner to B4F Giovanni's gate

def get_stable_coords():
    # Wait for any slide/animation to completely finish
    last_pos = mgba.get_coordinates()
    while True:
        time.sleep(0.5)
        cur_pos = mgba.get_coordinates()
        if cur_pos == last_pos:
            return cur_pos
        last_pos = cur_pos

def execute_move(direction, expected_coords=None, wait_stable=False):
    print(f"Pressing {direction}...")
    mgba.press_buttons([direction, "sleep 300"])
    
    if wait_stable:
        pos = get_stable_coords()
    else:
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        
    print(f"  Current position: {pos}")
    if expected_coords:
        if (pos['x'], pos['y']) != expected_coords:
            raise ValueError(f"COORDINATE DESYNC! Expected {expected_coords}, got {pos}")
    return pos

# We start at B2F (2, 9)
pos = get_stable_coords()
print("Starting run from:", pos)
if (pos['x'], pos['y']) != (2, 9):
    print("WARNING: Starting position is not (2, 9)!")

try:
    # 1. Walk B2F path to (4, 11) RIGHT spinner -> slides to (8, 11) stopper
    execute_move("Right", (3, 9))
    execute_move("Down", (3, 10))
    execute_move("Down", (3, 11))
    execute_move("Right", (8, 11), wait_stable=True)

    # 2. Walk to Column 10, then Down to Row 14, then Left onto (9, 14) DOWN spinner/hole -> B3F (9, 16)
    execute_move("Right", (9, 11))
    execute_move("Right", (10, 11))
    execute_move("Down", (10, 12))
    execute_move("Down", (10, 13))
    execute_move("Down", (10, 14))
    execute_move("Left", (9, 16), wait_stable=True) # Warps to B3F

    # 3. B3F Slide sequence to (15, 18)
    execute_move("Right", (10, 16))
    execute_move("Down", (11, 17), wait_stable=True) # slides to (11, 17)
    execute_move("Down", (12, 17), wait_stable=True) # slides to (12, 17)
    execute_move("Down", (13, 17), wait_stable=True) # slides to (13, 17)
    execute_move("Down", (14, 16), wait_stable=True) # slides to (14, 16)
    execute_move("Down", (14, 15), wait_stable=True) # slides to (14, 15)
    execute_move("Right", (15, 15))
    execute_move("Down", (15, 18), wait_stable=True) # slides to (15, 18)

    # 4. Walk to (11, 20) via (13, 18) LEFT spinner
    execute_move("Left", (14, 18))
    execute_move("Left", (11, 20), wait_stable=True)

    # 5. Walk to (11, 19) via (13, 19) LEFT spinner
    execute_move("Right", (12, 20))
    execute_move("Right", (13, 20))
    execute_move("Up", (11, 19), wait_stable=True)

    # 6. Walk to (14, 15) via (12, 17) RIGHT spinner
    execute_move("Right", (12, 19))
    execute_move("Up", (12, 18))
    execute_move("Up", (14, 15), wait_stable=True)

    # 7. Walk to (16, 13) Right Room via (16, 14) UP spinner
    execute_move("Right", (15, 15))
    execute_move("Right", (16, 15))
    execute_move("Up", (16, 13), wait_stable=True)

    # 8. Walk Column 28 path on B3F to stairs at (19, 18) -> warps to B4F (19, 10)
    for _ in range(12):
        execute_move("Right")
    # Expected at (28, 13)
    pos = get_stable_coords()
    if (pos['x'], pos['y']) != (28, 13):
        raise ValueError(f"Desync on Right 12! Expected (28, 13), got {pos}")

    for _ in range(5):
        execute_move("Down")
    # Expected at (28, 18)
    pos = get_stable_coords()
    if (pos['x'], pos['y']) != (28, 18):
        raise ValueError(f"Desync on Down 5! Expected (28, 18), got {pos}")

    for _ in range(9):
        execute_move("Left")
    # Expected at B4F (19, 10) (warp triggered!)
    pos = get_stable_coords()
    print("Warp triggered. Stable coords after warp:", pos)
    if (pos['x'], pos['y']) != (19, 10):
        raise ValueError(f"Desync on warp DOWN to B4F! Expected (19, 10), got {pos}")

    # 9. Walk B4F to the gate:
    # Down 6 from (19, 10) -> (19, 16)
    for _ in range(6):
        execute_move("Down")
    pos = get_stable_coords()
    if (pos['x'], pos['y']) != (19, 16):
        raise ValueError(f"Desync on B4F Down 6! Expected (19, 16), got {pos}")

    # Right 6 from (19, 16) -> (25, 16)
    for _ in range(6):
        execute_move("Right")
    pos = get_stable_coords()
    if (pos['x'], pos['y']) != (25, 16):
        raise ValueError(f"Desync on B4F Right 6! Expected (25, 16), got {pos}")

    # Up 9 from (25, 16) -> (25, 7)
    for _ in range(9):
        execute_move("Up")
    pos = get_stable_coords()
    if (pos['x'], pos['y']) != (25, 7):
        raise ValueError(f"Desync on B4F Up 9! Expected (25, 7), got {pos}")

    print("Successfully reached Giovanni's Gate at B4F (25, 7) on foot!")
    mgba.take_screenshot()

except ValueError as e:
    print("ERROR OCCURRED:", e)
    mgba.take_screenshot()
