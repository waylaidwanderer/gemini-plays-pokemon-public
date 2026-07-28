import mgba
import time

def go_to_burgled_house():
    print("Walking up column 34...")
    for i in range(7):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    print("Down to row 21...")
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    
    print("Walking left to column 9...")
    for i in range(25):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
    print("Walking up to row 16...")
    for i in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    print("Walking left to column 0...")
    for i in range(9):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
    print("Stepping left to transition to Route 4...")
    mgba.press_buttons(["Left"])
    time.sleep(1.0) # Wait for map transition screen reload
    
    print("Walking up to row 4 on Route 4...")
    for i in range(4):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    print("Stepping right to transition back to Cerulean City...")
    mgba.press_buttons(["Right"])
    time.sleep(1.0) # Wait for map transition screen reload
    
    print("Walking right to column 27...")
    for i in range(27):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    print("Walking up to enter the Burgled House...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0) # Wait for interior warp
    
    pos = mgba.get_coordinates()
    print(f"Final Position: {pos}")

go_to_burgled_house()
