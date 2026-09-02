import mgba
import time

def enter_from_east():
    print("Walking right to find a gap or eastern road...")
    # Walk right as far as possible (up to x=38)
    for i in range(10):
        pos = mgba.get_coordinates()
        if pos['x'] >= 38:
            break
        mgba.press_buttons(["Right"])
        time.sleep(0.2)
        
    pos = mgba.get_coordinates()
    print(f"Walked right to: {pos}")
    
    # Now try to walk UP to Row 8
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.2)
        
    pos = mgba.get_coordinates()
    print(f"Walked UP to: {pos}")
    
    # Now walk Left to x=32
    for _ in range(10):
        pos = mgba.get_coordinates()
        if pos['x'] <= 32:
            break
        mgba.press_buttons(["Left"])
        time.sleep(0.2)
        
    pos = mgba.get_coordinates()
    print(f"Walked Left to: {pos}")
    
    # Now walk UP into the Gym
    mgba.press_buttons(["Up", "Up"])
    time.sleep(0.5)
    print(f"Final position: {mgba.get_coordinates()}")

enter_from_east()
