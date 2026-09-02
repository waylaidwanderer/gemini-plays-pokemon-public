import mgba
import time
import os
from PIL import Image

def capture_trainer_card():
    print("Opening Trainer Card...")
    # Open START menu
    mgba.press_buttons(["Start"])
    time.sleep(0.5)
    
    # Move to ACE and select
    # To be safe, let's reset to top (by pressing Up 7 times, then Down 3 times)
    mgba.press_buttons(["Up"] * 7)
    time.sleep(0.5)
    mgba.press_buttons(["Down"] * 3)
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot
    sc_path = mgba.take_screenshot()
    print(f"Captured screenshot: {sc_path}")
    
    # Close Trainer Card and menu
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Copy to sandbox/screenshots/cropped/trainer_card.png
    os.makedirs("screenshots/cropped", exist_ok=True)
    img = Image.open(sc_path)
    img.save("screenshots/cropped/trainer_card.png")
    print("Saved trainer card image to screenshots/cropped/trainer_card.png")

capture_trainer_card()
