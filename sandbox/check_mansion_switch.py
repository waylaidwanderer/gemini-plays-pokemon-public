import mgba
import time
from PIL import Image

if __name__ == "__main__":
    # We are at (2, 6). Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Step 1: Interact
    print("Pressing A (1) to interact...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    img1 = mgba.take_screenshot()
    print(f"Step 1 screenshot: {img1}")
    
    # Step 2: Show prompt
    print("Pressing A (2) to show prompt...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    img2 = mgba.take_screenshot()
    print(f"Step 2 screenshot: {img2}")
    
    # Step 3: Select YES
    print("Pressing A (3) to select YES...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    img3 = mgba.take_screenshot()
    print(f"Step 3 screenshot: {img3}")
    
    # Step 4: Close dialogue
    print("Pressing A (4) to close dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    img4 = mgba.take_screenshot()
    print(f"Step 4 screenshot: {img4}")
    
    # Copy to static names
    Image.open(img1).save("step1.png")
    Image.open(img2).save("step2.png")
    Image.open(img3).save("step3.png")
    Image.open(img4).save("step4.png")
    print("Saved steps 1-4 to step1.png, step2.png, step3.png, step4.png")
    
    # Test Right
    print("Testing stepping Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    print(f"Final position: {mgba.get_coordinates()}")
