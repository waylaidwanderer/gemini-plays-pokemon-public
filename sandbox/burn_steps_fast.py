import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def burn_steps():
    print("=== BURNING SAFARI STEPS EXTREMELY FAST ===")
    
    # We will send a batch of 90 buttons (45 steps Left/Right with 100ms sleeps)
    # This is under the 100-button limit of a single execution!
    batch = []
    # Left 5, Right 5, repeated 9 times (90 buttons total)
    for _ in range(9):
        batch.append("Left")
        batch.append("Right")
        
    print(f"Sending batch of {len(batch)} actions to burn {len(batch)} steps...")
    res = bridge.press_buttons(batch)
    print(f"Response: {res}")
    
    pos = bridge.get_coordinates()
    print(f"Current coordinates: {pos}")
    
if __name__ == "__main__":
    burn_steps()
