import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

try:
    print("=== Navigating B3F Spinner Maze to B4F Stairs (21, 22) ===")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk to (11, 14) DOWN spinner
    print("Step 1: Walking to (10, 14)...")
    move("Right", 2)
    move("Down", 3)
    
    print("Stepping onto (11, 14) DOWN spinner...")
    move("Right", 1)
    print("Waiting for slide chain to finish...")
    time.sleep(4.0)
    print("Position after first slide (expect (15, 18)):", mgba.get_coordinates())
    
    # 2. Step Left onto (13, 18) LEFT spinner
    print("Step 2: Stepping Left onto (13, 18) LEFT spinner...")
    move("Left", 2) # from (15, 18) to (13, 18)
    print("Waiting for slide...")
    time.sleep(3.0)
    print("Position after second slide (expect (11, 20)):", mgba.get_coordinates())
    
    # 3. Walk to (13, 22) LEFT spinner
    print("Step 3: Walking to (14, 22)...")
    move("Down", 2) # from (11, 20) to (11, 22)
    move("Right", 3) # from (11, 22) to (14, 22)
    
    print("Stepping Left onto (13, 22) LEFT spinner...")
    move("Left", 1)
    print("Waiting for slide...")
    time.sleep(3.0)
    print("Position after third slide (expect (9, 24)):", mgba.get_coordinates())
    
    # 4. Walk to (10, 25) RIGHT spinner
    print("Step 4: Walking to (10, 24)...")
    move("Right", 1)
    
    print("Stepping Down onto (10, 25) RIGHT spinner...")
    move("Down", 1)
    print("Waiting for slide...")
    time.sleep(3.0)
    print("Position after fourth slide (expect (14, 25)):", mgba.get_coordinates())
    
    # 5. Walk to the stairs at (21, 22)
    print("Step 5: Walking to (21, 22) stairs...")
    move("Right", 7) # from (14, 25) to (21, 25)
    move("Up", 3) # from (21, 25) to (21, 22)
    
    print("Warping to B4F...")
    time.sleep(2.0)
    print("Final Position on B4F:", mgba.get_coordinates())
    mgba.take_screenshot()
    
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
