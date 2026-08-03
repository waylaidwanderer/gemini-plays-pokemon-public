import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

try:
    print("=== Solving B2F Maze from (2, 9) to Elevator ===")
    print("Current Position:", mgba.get_coordinates())
    
    # We are at B2F (2, 9)
    # 1. Walk Right 1 step to (3, 9)
    print("Walking Right 1...")
    move("Right", 1)
    
    # 2. Walk Down 2 steps to (3, 11)
    print("Walking Down 2...")
    move("Down", 2)
    
    # 3. Walk Right 1 step onto (4, 11) RIGHT spinner -> slides to (8, 11)
    print("Stepping Right onto (4, 11) RIGHT spinner...")
    move("Right", 1)
    print("Waiting 3 seconds for slide...")
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after slide (expect (8, 11)):", pos)
    
    # 4. Walk Down 4 steps to (8, 15)
    print("Walking Down 4 to (8, 15)...")
    move("Down", 4)
    
    # 5. Walk Right 7 steps to (15, 15)
    print("Walking Right 7 to (15, 15)...")
    move("Right", 7)
    
    # 6. Walk Down 1 step onto (15, 16) DOWN spinner -> slides to (15, 18)
    print("Stepping Down onto (15, 16) DOWN spinner...")
    move("Down", 1)
    print("Waiting 3 seconds for slide...")
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after slide (expect lower chamber, y >= 17):", pos)
    
    # 7. Walk Right to Column 24
    current_pos = mgba.get_coordinates()
    dist_x = 24 - current_pos['x']
    print(f"Walking Right {dist_x} steps...")
    move("Right", dist_x)
    
    # 8. Face DOWN
    print("Facing DOWN...")
    mgba.press_buttons(["Down", "sleep 300"])
    time.sleep(0.5)
    
    # 9. Press A with Lift Key to unlock and open doors!
    print("Pressing A to open elevator doors...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 10. Walk Down 1 step into the elevator!
    print("Walking DOWN into elevator cabin...")
    move("Down", 1)
    time.sleep(3.0)
    
    print("Final Position inside elevator:", mgba.get_coordinates())
    mgba.take_screenshot()
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
