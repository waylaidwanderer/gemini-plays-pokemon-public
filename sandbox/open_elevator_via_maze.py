import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

try:
    print("=== Executing Master B2F Elevator Unlock Route ===")
    print("Initial Position:", mgba.get_coordinates())
    
    # 1. Walk to the start of the maze at B2F (27, 8)
    # We are at (20, 14)
    print("Walking Up to row 8...")
    move("Up", 6)
    print("Walking Right to column 27...")
    move("Right", 7)
    
    # Verify we are at the start of the maze
    # Wait, coming from (20, 14) to (27, 8) we might spawn or be at (27, 8)
    pos = mgba.get_coordinates()
    print("At start of maze:", pos)
    if pos['x'] != 27 or pos['y'] != 8:
        raise ValueError(f"Desync! Expected (27, 8), got {pos}")
        
    # 2. Walk Down 5 steps to (27, 13)
    print("Walking Down 5 to (27, 13)...")
    move("Down", 5)
    
    # 3. Walk Left 15 steps onto (12, 13) UP spinner -> slides to (2, 9)
    print("Stepping Left onto (12, 13) UP spinner...")
    move("Left", 15)
    time.sleep(5.0) # Wait for slide to complete
    pos = mgba.get_coordinates()
    print("Position after slide 1 (expect (2, 9)):", pos)
    if pos['x'] != 2 or pos['y'] != 9:
        raise ValueError(f"Desync after slide 1! Expected (2, 9), got {pos}")
        
    # 4. Walk Right 1 step to (3, 9)
    print("Walking Right 1...")
    move("Right", 1)
    
    # 5. Walk Down 2 steps to (3, 11)
    print("Walking Down 2...")
    move("Down", 2)
    
    # 6. Walk Right 1 step onto (4, 11) RIGHT spinner -> slides to (8, 11)
    print("Stepping Right onto (4, 11) RIGHT spinner...")
    move("Right", 1)
    time.sleep(2.0) # Wait for slide to complete
    pos = mgba.get_coordinates()
    print("Position after slide 2 (expect (8, 11)):", pos)
    if pos['x'] != 8 or pos['y'] != 11:
        raise ValueError(f"Desync after slide 2! Expected (8, 11), got {pos}")
        
    # 7. Walk Down 4 steps to (8, 15)
    print("Walking Down 4 to (8, 15)...")
    move("Down", 4)
    
    # 8. Walk Right 7 steps to (15, 15)
    print("Walking Right 7 to (15, 15)...")
    move("Right", 7)
    
    # 9. Walk Down 1 step onto (15, 16) DOWN spinner -> slides to (15, 18)
    print("Stepping Down onto (15, 16) DOWN spinner...")
    move("Down", 1)
    time.sleep(2.0) # Wait for slide to complete
    pos = mgba.get_coordinates()
    print("Spawned in lower chamber (expect (15, 18)):", pos)
    if pos['y'] < 17:
        raise ValueError(f"Desync after slide 3! Expected lower chamber, got {pos}")
        
    # 10. Walk Right 9 steps to (24, 18) (or we can just walk to (24, 18) based on x-coord)
    current_pos = mgba.get_coordinates()
    dist_x = 24 - current_pos['x']
    print(f"Walking Right {dist_x} steps...")
    move("Right", dist_x)
    
    # 11. Face DOWN
    print("Facing DOWN...")
    mgba.press_buttons(["Down", "sleep 300"])
    time.sleep(0.5)
    
    # 12. Press A with Lift Key to unlock and open doors!
    print("Pressing A to open elevator doors...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 13. Walk Down 1 step into the elevator!
    print("Walking DOWN into elevator cabin...")
    move("Down", 1)
    time.sleep(3.0)
    
    print("Final Position inside elevator:", mgba.get_coordinates())
    mgba.take_screenshot()
except Exception as e:
    print("Error:", e)
    mgba.take_screenshot()
