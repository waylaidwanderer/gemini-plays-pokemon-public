import mgba
import time

def walk_to_gym_front():
    print("Walking to the Gym front at (29, 8)...")
    
    # 18-step path
    path = [
        "Up", "Up", "Up",               # (19, 8) -> (19, 5)
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # (19, 5) -> (27, 5)
        "Down",                          # (27, 5) -> (27, 6)
        "Left",                          # (27, 6) -> (26, 6)
        "Down", "Down",                  # (26, 6) -> (26, 8)
        "Right", "Right", "Right"        # (26, 8) -> (29, 8)
    ]
    
    for btn in path:
        mgba.press_buttons([btn])
        time.sleep(0.15)
        
    pos = mgba.get_coordinates()
    print(f"Arrived at: {pos}")
    
    # Turn right to face the NPC at (30, 8) and talk to him
    mgba.press_buttons(["Right"])
    time.sleep(0.15)
    
    # Talk
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    print("Talked. Let's close any textboxes.")
    mgba.press_buttons(["B"])
    time.sleep(0.2)
    mgba.press_buttons(["B"])
    time.sleep(0.2)
    
    # Try to walk Right
    mgba.press_buttons(["Right"])
    time.sleep(0.15)
    print(f"Final coordinates: {mgba.get_coordinates()}")

walk_to_gym_front()
