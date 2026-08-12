import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def burn_steps():
    print("=== BURNING SAFARI STEPS FAST ===")
    
    # We will send a batch of 80 buttons (40 steps Left/Right with 100ms sleeps)
    # This takes 80 * 100ms = 8 seconds of sleep, well under our new 25-second socket timeout!
    
    batch = []
    # Left 5, Right 5, repeated 4 times (40 steps total)
    for _ in range(4):
        batch.extend(["Left", "sleep 100"] * 5)
        batch.extend(["Right", "sleep 100"] * 5)
        
    print(f"Sending batch of {len(batch)} actions to burn 40 steps...")
    res = bridge.press_buttons(batch)
    print(f"Response: {res}")
    
    pos = bridge.get_coordinates()
    print(f"Current coordinates: {pos}")
    
if __name__ == "__main__":
    burn_steps()
