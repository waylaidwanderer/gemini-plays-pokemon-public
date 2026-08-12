import bridge
import time

def burn_steps():
    print("=== BURNING SAFARI STEPS DIRECTLY ===")
    
    # We are at (3, 4). We'll step Right to (4, 4) and Left to (3, 4) in a loop.
    steps_taken = 0
    while True:
        # Step Right
        bridge.press_buttons(["Right"])
        time.sleep(0.12)
        
        # Step Left
        bridge.press_buttons(["Left"])
        time.sleep(0.12)
        
        steps_taken += 2
        
        # Every 20 steps, check position
        if steps_taken % 20 == 0:
            pos = bridge.get_coordinates()
            print(f"Steps taken: {steps_taken}, Current pos: {pos}")
            
            if pos is None:
                # We might be in a battle or transitioning
                continue
                
            # If we warp, our position will change drastically (typically to (15, 25) in Safari Zone Center,
            # or (18, 3) / (18, 8) in Fuchsia City Gatehouse).
            # The isolated ground is x <= 5 and y <= 8.
            if not (pos[0] <= 5 and pos[1] <= 8):
                print(f"Warp detected! New position: {pos}")
                break
                
            if steps_taken >= 600:
                print("Safety limit of 600 steps reached.")
                break

if __name__ == "__main__":
    burn_steps()
