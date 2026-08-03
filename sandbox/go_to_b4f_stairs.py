import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

try:
    print("=== Navigating B3F Spinner Maze to B4F Stairs ===")
    print("Initial Position:", mgba.get_coordinates())
    
    # We are at B3F (15, 18)
    # 1. Step Left onto (13, 18) LEFT spinner
    print("Step 1: Stepping Left onto (13, 18) LEFT spinner...")
    move("Left", 2)
    print("Waiting for slide 1 to complete...")
    time.sleep(3.0)
    print("Position after slide 1 (expect (11, 20)):", mgba.get_coordinates())
    
    # 2. Walk to (14, 22) via Row 20
    print("Step 2: Walking to (14, 22) via Row 20...")
    move("Right", 3) # from (11, 20) to (14, 20)
    move("Down", 2) # from (14, 20) to (14, 22)
    print("Position at (14, 22):", mgba.get_coordinates())
    
    # 3. Step Left onto (13, 22) LEFT spinner
    print("Step 3: Stepping Left onto (13, 22) LEFT spinner...")
    move("Left", 1)
    print("Waiting for slide 2 to complete...")
    time.sleep(3.0)
    print("Position after slide 2 (expect (9, 24)):", mgba.get_coordinates())
    
    # 4. Walk to (10, 24) and step onto (10, 25) RIGHT spinner
    print("Step 4: Walking to (10, 24)...")
    move("Right", 1)
    print("Stepping Down onto (10, 25) RIGHT spinner...")
    move("Down", 1)
    print("Waiting for slide 3 to complete...")
    time.sleep(3.0)
    print("Position after slide 3 (expect (14, 25)):", mgba.get_coordinates())
    
    # 5. Walk to the stairs at (21, 22)
    print("Step 5: Walking to (21, 22) stairs...")
    move("Right", 7) # from (14, 25) to (21, 25)
    move("Up", 3) # from (21, 25) to (21, 22)
    print("Position at stairs:", mgba.get_coordinates())
    
    # Step into warp
    print("Warping to B4F...")
    time.sleep(2.0)
    print("Final Position on B4F:", mgba.get_coordinates())
    mgba.take_screenshot()
    
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
