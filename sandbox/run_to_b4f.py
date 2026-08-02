import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at B1F: {pos}")

# Step 1: Walk Up to (23, 2) stairs to B2F
pos = move(["Up"])
time.sleep(1.0)
pos = mgba.get_coordinates()
print(f"Position on B2F: {pos}")

if pos['x'] == 27 and pos['y'] == 8:
    # Step 2: Walk to B3F stairs at B2F (21, 8)
    print("Walking to B3F stairs...")
    # Down 6 steps
    for _ in range(6):
        pos = move(["Down"])
    # Left 6 steps
    for _ in range(6):
        pos = move(["Left"])
    # Up 6 steps into B3F stairs
    for _ in range(6):
        pos = move(["Up"])
    
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Position on B3F: {pos}")

if pos['x'] == 25 and pos['y'] == 6:
    # Step 3: Solve B3F spinner maze
    print("Solving B3F spinner maze...")
    pos = move(["Down"])
    for _ in range(8):
        pos = move(["Left"])
    for _ in range(3):
        pos = move(["Down"])
    pos = move(["Left"])
    pos = move(["Left"]) # onto (17, 10) LEFT spinner
    time.sleep(2.0)
    
    pos = mgba.get_coordinates()
    print(f"Position at (14, 12) stopper: {pos}")
    
    pos = move(["Down"])
    pos = move(["Left"])
    pos = move(["Left"]) # onto (12, 13) UP spinner -> slides to (2, 9)
    time.sleep(3.0)
    
    pos = mgba.get_coordinates()
    print(f"Position at (2, 9) stopper: {pos}")
    
    for _ in range(2):
        pos = move(["Right"])
    for _ in range(4):
        pos = move(["Down"])
    pos = move(["Down"])
    pos = move(["Right"]) # onto (5, 14) RIGHT spinner -> slides to (9, 16)
    time.sleep(3.0)
    
    pos = mgba.get_coordinates()
    print(f"Position at (9, 16) stopper: {pos}")
    
    pos = move(["Right"])
    pos = move(["Right"]) # onto (11, 16) RIGHT spinner -> slides to (15, 18)
    time.sleep(3.0)
    
    pos = mgba.get_coordinates()
    print(f"Position at (15, 18) stopper: {pos}")
    
    pos = move(["Up"])
    pos = move(["Right"]) # onto (16, 17) UP spinner -> slides to (16, 13)
    time.sleep(3.0)
    
    pos = mgba.get_coordinates()
    print(f"Position at (16, 13) stopper: {pos}")
    
    pos = move(["Right"])
    for _ in range(7):
        pos = move(["Down"])
    for _ in range(2):
        pos = move(["Right"])
    pos = move(["Up"])
    pos = move(["Up"]) # onto (19, 18) B4F stairs -> warps to B4F (19, 10)
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Final position on B4F: {pos}")
    mgba.take_screenshot()
else:
    print("Map alignment mismatch. Taking screenshot.")
    mgba.take_screenshot()
