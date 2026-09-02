import mgba
import time

def wait_for_npc():
    print("Waiting for NPC to move...")
    for i in range(20):
        # Press B to wait
        mgba.press_buttons(["B"])
        time.sleep(1.0)
        
        # Try to step right
        mgba.press_buttons(["Right"])
        time.sleep(0.2)
        pos = mgba.get_coordinates()
        print(f"Time {i}: Position: {pos}")
        
        if pos['x'] >= 30:
            print("NPC moved! Walking to the Gym...")
            # Walk right to (32, 8)
            for _ in range(5):
                if pos['x'] < 32:
                    mgba.press_buttons(["Right"])
                    time.sleep(0.2)
                    pos = mgba.get_coordinates()
            # Walk UP to enter the Gym
            mgba.press_buttons(["Up", "Up"])
            time.sleep(0.5)
            print(f"Entered Gym! Position: {mgba.get_coordinates()}")
            return True
            
    print("NPC did not move.")
    return False

wait_for_npc()
