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

def execute_move(direction, expected_coords=None, wait_stable=False, wait_time=0.4):
    print(f"Pressing {direction}...")
    mgba.press_buttons([direction, "sleep 300"])
    
    if wait_stable:
        pos = get_stable_coords()
    else:
        time.sleep(wait_time)
        pos = mgba.get_coordinates()
        
    print(f"  Current position: {pos}")
    if expected_coords:
        if (pos['x'], pos['y']) != expected_coords:
            raise ValueError(f"COORDINATE DESYNC! Expected {expected_coords}, got {pos}")
    return pos

# We start at B3F (14, 15)
pos = get_stable_coords()
print("Starting run from:", pos)
if (pos['x'], pos['y']) != (14, 15):
    print("WARNING: Starting position is not (14, 15)!")

try:
    # 1. Walk to B3F (15, 18)
    execute_move("Right", (15, 15))
    execute_move("Down", (15, 18), wait_stable=True) # slides to (15, 18)

    # 2. Walk to B3F (11, 20) via (13, 18) LEFT spinner
    execute_move("Left", (14, 18))
    execute_move("Left", (11, 20), wait_stable=True)

    # 3. Walk to B3F (10, 18) via (13, 19) LEFT spinner -> (10, 19) UP spinner
    execute_move("Right", (12, 20))
    execute_move("Right", (13, 20))
    execute_move("Up", (10, 18), wait_stable=True)

    # 4. Walk to B3F (14, 15) via (10, 17) RIGHT spinner
    # We found that stepping onto (10, 17) RIGHT spinner slides us to (14, 17) UP spinner stopper!
    execute_move("Up", (14, 17), wait_stable=True)
    # Then we walk Up 2 steps to (14, 15)
    execute_move("Up", (14, 16))
    execute_move("Up", (14, 15))

    # 5. Walk to B3F (16, 13) Right Room via (16, 14) UP spinner
    execute_move("Right", (15, 15))
    execute_move("Right", (16, 15))
    execute_move("Up", (16, 13), wait_stable=True)

    # 6. Walk Column 28 path on B3F to stairs at (19, 18) -> warps to B4F (19, 10)
    print("Walking to B3F stairs...")
    for _ in range(12):
        execute_move("Right")
    pos = get_stable_coords()
    if (pos['x'], pos['y']) != (28, 13):
        raise ValueError(f"Desync on Right 12! Expected (28, 13), got {pos}")

    for _ in range(5):
        execute_move("Down")
    pos = get_stable_coords()
    if (pos['x'], pos['y']) != (28, 18):
        raise ValueError(f"Desync on Down 5! Expected (28, 18), got {pos}")

    for _ in range(9):
        execute_move("Left")
    pos = get_stable_coords()
    print("Warp triggered. Stable coords after warp:", pos)
    if (pos['x'], pos['y']) != (19, 10):
        raise ValueError(f"Desync on warp DOWN to B4F! Expected (19, 10), got {pos}")

    # 7. Walk B4F to the gate:
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
