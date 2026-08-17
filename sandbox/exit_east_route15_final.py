import mgba
import time

def run():
    print("--- CORRECTED GATEHOUSE EAST EXIT WITH TURN-IN-PLACE ---")
    pos = mgba.get_coordinates()
    print("Start position on 2F:", pos)
    
    # We are at (6, 8) on 2F facing UP.
    # To step Right to (7, 8):
    # 1. Turn Right (Right)
    # 2. Step Right (Right) - triggers warp down
    print("Turning and stepping onto stairs (Right, Right)...")
    mgba.press_buttons(["Right", "sleep 200", "Right"])
    time.sleep(2.5) # Wait for transition to complete
    
    land_pos = mgba.get_coordinates()
    print("Landed on 1F at:", land_pos)
    
    # On 1F, we land at (6, 8) facing DOWN (or similar).
    # To step Down to (6, 9):
    # Press Down to step (since we are facing DOWN, or turn if we aren't).
    # Let's press Down twice to be safe (first to turn, second to step).
    print("Stepping Down to (6, 9)...")
    mgba.press_buttons(["Down", "sleep 200", "Down"])
    time.sleep(0.5)
    print("Position in corridor:", mgba.get_coordinates())
    
    # From (6, 9) on 1F, we are facing DOWN.
    # To step Right 3 times to (9, 9) and exit:
    # 1. Turn Right (Right)
    # 2. Step Right to (7, 9) (Right)
    # 3. Step Right to (8, 9) (Right) - triggers overworld transition
    # 4. Step Right to (9, 9) (Right)
    print("Stepping Right to transition out of gatehouse...")
    mgba.press_buttons(["Right", "sleep 250", "Right", "sleep 250", "Right", "sleep 250", "Right"])
    time.sleep(2.0) # Wait for overworld transition
    
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
