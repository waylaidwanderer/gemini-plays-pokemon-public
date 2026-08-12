import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def burn_steps():
    print("=== BURNING SAFARI STEPS SAFELY ===")
    
    # We will send batches of 30 buttons (15 steps Left/Right)
    # This takes 30 * 150ms = 4.5 seconds to execute, well under the 10-second socket timeout!
    
    batch = []
    # Left 5, Right 5, Left 5 (15 steps total)
    batch.extend(["Left", "sleep 150"] * 5)
    batch.extend(["Right", "sleep 150"] * 5)
    batch.extend(["Left", "sleep 150"] * 5)
        
    print(f"Sending batch of {len(batch)} actions to burn 15 steps...")
    res = bridge.press_buttons(batch)
    print(f"Response: {res}")
    
    pos = bridge.get_coordinates()
    print(f"Current coordinates: {pos}")
    
if __name__ == "__main__":
    burn_steps()
