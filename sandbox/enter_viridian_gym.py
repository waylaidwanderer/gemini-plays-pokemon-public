import mgba
import time

def walk_from_19_7():
    print("Walking from (19, 7) to Gym front at (29, 8)...")
    
    # Path from (19, 7)
    path = [
        "Up", "Up",                      # (19, 7) -> (19, 5)
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # (19, 5) -> (27, 5)
        "Down",                          # (27, 5) -> (27, 6)
        "Left",                          # (27, 6) -> (26, 6)
        "Down", "Down",                  # (26, 6) -> (26, 8)
        "Right", "Right", "Right"        # (26, 8) -> (29, 8)
    ]
    
    for btn in path:
        mgba.press_buttons([btn])
        time.sleep(0.2)
        
    pos = mgba.get_coordinates()
    print(f"Arrived at: {pos}")
    
    # Talk to the NPC at (30, 8) if we are at (29, 8)
    if pos['x'] == 29 and pos['y'] == 8:
        # Turn right and talk
        mgba.press_buttons(["Right", "A"])
        time.sleep(0.5)
        # Take a screenshot to see textbox
        sc = mgba.take_screenshot()
        print(f"Took screenshot of textbox: {sc}")
        
        # Close textbox
        mgba.press_buttons(["B"])
        time.sleep(0.2)
        mgba.press_buttons(["B"])
        time.sleep(0.2)
        
        # Try to walk Right
        mgba.press_buttons(["Right"])
        time.sleep(0.2)
        print(f"Final coordinates: {mgba.get_coordinates()}")

walk_from_19_7()
