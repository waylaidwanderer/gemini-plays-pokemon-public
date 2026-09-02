import mgba
import time

def leave_viridian():
    print("Walking out of Viridian City to Route 1...")
    
    # 22-step path to (19, 10)
    path = [
        "Left", "Left", "Left",         # (29, 8) -> (26, 8)
        "Up", "Up",                      # (26, 8) -> (26, 6)
        "Right",                         # (26, 6) -> (27, 6)
        "Up", "Up",                      # (27, 6) -> (27, 4)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (27, 4) -> (19, 4)
        "Down", "Down", "Down", "Down", "Down", "Down" # (19, 4) -> (19, 10)
    ]
    
    for btn in path:
        mgba.press_buttons([btn])
        time.sleep(0.15)
        
    pos = mgba.get_coordinates()
    print(f"Arrived at west corridor: {pos}")
    
    # Now walk all the way south to the Route 1 transition
    # The southern exit is around (20, 35)
    # Let's walk Down to y=35
    for i in range(25):
        mgba.press_buttons(["Down"])
        time.sleep(0.1)
        pos = mgba.get_coordinates()
        if pos['y'] >= 34:
            print(f"Reached south of city: {pos}")
            break
            
    # Step onto Route 1 (y=35)
    mgba.press_buttons(["Right", "Down", "Down"])
    time.sleep(0.5)
    
    print(f"Map transition attempt finished. Current position: {mgba.get_coordinates()}")

leave_viridian()
