import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

try:
    print("=== Executing Ultimate B2F Elevator Unlock Route ===")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk from (21, 9) to (17, 11) LEFT spinner
    print("Walking Right 1 to (22, 9)...")
    move("Right", 1)
    
    print("Walking Down 2 to (22, 11)...")
    move("Down", 2)
    
    print("Walking Left 5 onto (17, 11) LEFT spinner...")
    move("Left", 5)
    time.sleep(5.0) # Wait for slide to complete
    pos = mgba.get_coordinates()
    print("Position after slide 1 (expect (2, 9)):", pos)
    if pos['x'] != 2 or pos['y'] != 9:
        raise ValueError(f"Desync after slide 1! Expected (2, 9), got {pos}")
        
    # 2. Walk Right 1 step to (3, 9)
    print("Walking Right 1...")
    move("Right", 1)
    
    # 3. Walk Down 2 steps to (3, 11)
    print("Walking Down 2...")
    move("Down", 2)
    
    # 4. Walk Right 1 step onto (4, 11) RIGHT spinner -> slides to (8, 11)
    print("Stepping Right onto (4, 11) RIGHT spinner...")
    move("Right", 1)
    time.sleep(2.0) # Wait for slide to complete
    pos = mgba.get_coordinates()
    print("Position after slide 2 (expect (8, 11)):", pos)
    if pos['x'] != 8 or pos['y'] != 11:
        raise ValueError(f"Desync after slide 2! Expected (8, 11), got {pos}")
        
    # 5. Walk Down 4 steps to (8, 15)
    print("Walking Down 4 to (8, 15)...")
    move("Down", 4)
    
    # 6. Walk Right 7 steps to (15, 15)
    print("Walking Right 7 to (15, 15)...")
    move("Right", 7)
    
    # 7. Walk Down 1 step onto (15, 16) DOWN spinner -> slides to (15, 18)
    print("Stepping Down onto (15, 16) DOWN spinner...")
    move("Down", 1)
    time.sleep(2.0) # Wait for slide to complete
    pos = mgba.get_coordinates()
    print("Spawned in lower chamber (expect (15, 18)):", pos)
    if pos['y'] < 17:
        raise ValueError(f"Desync after slide 3! Expected lower chamber, got {pos}")
        
    # 8. Walk Right 9 steps to B2F (24, 18)
    current_pos = mgba.get_coordinates()
    dist_x = 24 - current_pos['x']
    print(f"Walking Right {dist_x} steps...")
    move("Right", dist_x)
    
    # 9. Face DOWN
    print("Facing DOWN...")
    mgba.press_buttons(["Down", "sleep 300"])
    time.sleep(0.5)
    
    # 10. Press A with Lift Key to unlock and open doors!
    print("Pressing A to open elevator doors...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 11. Walk Down 1 step into the elevator!
    print("Walking DOWN into elevator cabin...")
    move("Down", 1)
    time.sleep(3.0)
    
    print("Final Position inside elevator:", mgba.get_coordinates())
    mgba.take_screenshot()
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
