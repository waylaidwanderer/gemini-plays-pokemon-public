import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

try:
    print("=== Solving B2F Spinner Maze to Reach Lower Chamber ===")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. We are at B2F (2, 9)
    # Walk Right 1 to (3, 9)
    print("Walking Right 1...")
    move("Right", 1)
    
    # Walk Down 2 to (3, 11)
    print("Walking Down 2...")
    move("Down", 2)
    
    # Walk Right 1 onto (4, 11) RIGHT spinner -> slides to (8, 11)
    print("Stepping onto (4, 11) RIGHT spinner...")
    move("Right", 1)
    time.sleep(2.0) # Wait for slide to complete
    print("Position after slide 1:", mgba.get_coordinates())
    
    # 2. Walk Down 4 to (8, 15)
    print("Walking Down 4 to (8, 15)...")
    move("Down", 4)
    
    # 3. Walk Right 7 steps to (15, 15)
    print("Walking Right 7 to (15, 15)...")
    move("Right", 7)
    print("Position at (15, 15):", mgba.get_coordinates())
    
    # 4. Walk Down 1 step onto (15, 16) DOWN spinner -> slides to (15, 18)
    print("Stepping Down onto (15, 16) DOWN spinner...")
    move("Down", 1)
    time.sleep(2.0) # Wait for slide to complete
    print("Spawned in lower chamber at:", mgba.get_coordinates())
    
    # 5. Walk Right 9 steps to stand at B2F (24, 18)
    print("Walking Right 9 to (24, 18)...")
    move("Right", 9)
    print("Position in front of elevator:", mgba.get_coordinates())
    
    # 6. Face DOWN
    print("Facing DOWN...")
    mgba.press_buttons(["Down", "sleep 300"])
    time.sleep(0.5)
    
    print("SUCCESSFULLY COMPLETED MAZE AND REACHED ELEVATOR ENTRANCE!")
    mgba.take_screenshot()
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
