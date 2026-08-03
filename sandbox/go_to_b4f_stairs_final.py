import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

try:
    print("=== Final Navigation from (10, 22) on B3F to B4F ===")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk Down to (10, 24) and step onto (10, 25) RIGHT spinner
    print("Walking to (10, 24)...")
    move("Down", 2)
    
    print("Stepping Down onto (10, 25) RIGHT spinner...")
    move("Down", 1)
    print("Waiting for slide to finish...")
    time.sleep(3.0)
    print("Position after slide (expect (14, 25)):", mgba.get_coordinates())
    
    # 2. Walk to stairs at (21, 22)
    print("Walking Right to (21, 25)...")
    move("Right", 7)
    
    print("Walking Up to (21, 22) stairs...")
    move("Up", 3)
    
    print("Warping to B4F...")
    time.sleep(2.0)
    print("Final Position on B4F:", mgba.get_coordinates())
    mgba.take_screenshot()
    
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
