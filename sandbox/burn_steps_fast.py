import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def burn_steps():
    print("=== BURNING SAFARI STEPS SAFELY ===")
    
    # We will send batches of 80 buttons (40 steps Left/Right)
    # This is well under the 100 buttons limit per press_buttons call
    # We will do this in a loop until we get warped back to the Gatehouse,
    # or until our steps run out!
    
    batch = []
    for _ in range(40):
        batch.extend(["Left", "sleep 150", "Right", "sleep 150"])
        
    print(f"Sending batch of {len(batch)} actions to burn steps...")
    res = bridge.press_buttons(batch)
    print(f"Response: {res}")
    
    # Get coordinates to see where we are
    pos = bridge.get_coordinates()
    print(f"Current coordinates: {pos}")
    
if __name__ == "__main__":
    burn_steps()
