import mgba
import time

print("--- EXITING WARDEN'S HOUSE VIA ROW 16 ---")

# We are at (9, 12).
# Let's walk Down to (9, 16).
# Then Left to (6, 16).
# Then Up to (6, 15) to exit!

def get_pos():
    return mgba.get_coordinates()

path_moves = [
    ("Down", 4), # Down 4 steps to (9, 16)
    ("Left", 3), # Left 3 steps to (6, 16)
    ("Up", 1),   # Up 1 step to (6, 15) (warp)
]

for move, steps in path_moves:
    for s in range(steps):
        pos = get_pos()
        print(f"Current Position: {pos}. Pressing {move}...")
        
        # Press twice to handle turn if needed, or sleep to let it step
        mgba.press_buttons([move])
        time.sleep(0.4)
        mgba.press_buttons([move])
        time.sleep(0.4)
        
        new_pos = get_pos()
        print(f"New Position after {move}: {new_pos}")
        
        # Check if we successfully warped out (Fuchsia City coordinate space)
        if new_pos and new_pos['x'] > 12:
            print("Successfully warped out to Fuchsia City!")
            break
    else:
        continue
    break

mgba.take_screenshot()
print("Final Position:", get_pos())
