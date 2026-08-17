import mgba
import time

def run():
    print("--- DYNAMIC 1F EAST ROOM EXPLORER & EXIT ---")
    pos = mgba.get_coordinates()
    print("Start position on 2F:", pos)
    
    # 1. Step Right to (7, 8) to trigger warp down to 1F
    print("Stepping onto stairs (Right)...")
    mgba.press_buttons(["Right"])
    time.sleep(2.0) # Wait for transition to complete
    
    land_pos = mgba.get_coordinates()
    print("Landed on 1F at:", land_pos)
    
    # Let's define a safe local BFS to find the exit (x >= 8) on 1F
    # To prevent double-warp, we must avoid stepping onto (7, 7) or (7, 9) unless we are transitioning out of the map.
    # Actually, let's just probe coordinates and find a path.
    # Visually, on 1F, the staircase is on column 7.
    # If the landing is at (7, 7), the corridor is at Row 9.
    # Let's try:
    # 1. Step Left to (6, 7)
    # 2. Step Down to (6, 8)
    # 3. Step Down to (6, 9)
    # 4. Step Right 3 times to transition to Route 15 overworld.
    
    # Let's execute this path step-by-step and print the positions!
    path = ["Left", "Down", "Down", "Right", "Right", "Right"]
    
    for i, move in enumerate(path):
        mgba.press_buttons([move])
        time.sleep(0.4)
        curr = mgba.get_coordinates()
        print(f"Step {i+1} ({move}): {curr}")
        if curr['x'] < land_pos['x'] - 5: # If coordinates reset or became very small, we transitioned!
            print("Successfully transitioned to Route 15 overworld!")
            break
            
    time.sleep(1.5) # Wait for overworld map transition
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
