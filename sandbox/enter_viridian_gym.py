import mgba
import time

def walk_from_19_7_safe():
    print("Walking to Gym front from (19, 7) avoiding NPC at (19, 5)...")
    
    # Path avoiding NPC
    path = [
        "Left",                          # (19, 7) -> (18, 7)
        "Up", "Up", "Up",                # (18, 7) -> (18, 4)
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # (18, 4) -> (27, 4)
        "Down", "Down",                  # (27, 4) -> (27, 6)
        "Left",                          # (27, 6) -> (26, 6)
        "Down", "Down",                  # (26, 6) -> (26, 8)
        "Right", "Right", "Right"        # (26, 8) -> (29, 8)
    ]
    
    for btn in path:
        mgba.press_buttons([btn])
        time.sleep(0.25)
        
    pos = mgba.get_coordinates()
    print(f"Arrived at: {pos}")
    
    if pos['x'] == 29 and pos['y'] == 8:
        # Turn right and talk to the NPC
        mgba.press_buttons(["Right", "A"])
        time.sleep(0.5)
        # Take a screenshot
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

walk_from_19_7_safe()
