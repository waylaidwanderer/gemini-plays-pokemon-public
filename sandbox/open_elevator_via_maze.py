import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

try:
    print("=== Solving B2F Maze from (10, 14) to Elevator ===")
    print("Current Position:", mgba.get_coordinates())
    
    # We are at B2F (10, 14)
    # 1. Walk Right 1 step onto (11, 14) DOWN spinner -> slides to (15, 18)
    print("Stepping Right onto (11, 14) DOWN spinner...")
    move("Right", 1)
    print("Waiting 4 seconds for full slide chain...")
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Position after slide chain (expect (15, 18)):", pos)
    
    # 2. Walk Right to Column 24
    dist_x = 24 - pos['x']
    print(f"Walking Right {dist_x} steps...")
    move("Right", dist_x)
    
    # 3. Face DOWN
    print("Facing DOWN...")
    mgba.press_buttons(["Down", "sleep 300"])
    time.sleep(0.5)
    
    # 4. Press A with Lift Key to unlock and open doors!
    print("Pressing A to open elevator doors...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 5. Walk Down 1 step into the elevator!
    print("Walking DOWN into elevator cabin...")
    move("Down", 1)
    time.sleep(3.0)
    
    print("Final Position inside elevator:", mgba.get_coordinates())
    mgba.take_screenshot()
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
