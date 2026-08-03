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
    
    # 1. Walk Down 1 to (10, 14)
    print("Step 1: Walking Down to (10, 14)...")
    move("Down", 1)
    
    # 2. Walk Right 1 onto (11, 14) DOWN spinner
    print("Step 2: Stepping Right onto (11, 14) DOWN spinner...")
    move("Right", 1)
    print("Waiting for slide 1 to complete...")
    time.sleep(2.5)
    print("Position after slide 1 (expect (11, 15)):", mgba.get_coordinates())
    
    # 3. Walk Down 1 onto (11, 16) RIGHT spinner
    print("Step 3: Stepping Down onto (11, 16) RIGHT spinner...")
    move("Down", 1)
    print("Waiting for slide 2 to complete...")
    time.sleep(2.5)
    print("Position after slide 2 (expect (12, 16)):", mgba.get_coordinates())
    
    # 4. Walk Right 1 onto (13, 16) RIGHT spinner
    print("Step 4: Stepping Right onto (13, 16) RIGHT spinner...")
    move("Right", 1)
    print("Waiting for slide 3 to complete...")
    time.sleep(3.5)
    print("Position after slide 3 (expect (15, 18)):", mgba.get_coordinates())
    
    # 5. Walk Right 4 to the stairs at (19, 18)
    print("Step 5: Walking Right to (19, 18) stairs...")
    move("Right", 4)
    print("Position at stairs:", mgba.get_coordinates())
    
    # 6. Take the stairs DOWN to B4F
    print("Step 6: Taking stairs down to B4F...")
    move("Down", 1)
    time.sleep(2.5) # Wait for warp transition
    print("Position on B4F:", mgba.get_coordinates())
    mgba.take_screenshot()
    
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
