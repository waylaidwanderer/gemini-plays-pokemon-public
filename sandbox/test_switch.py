import mgba
import time
from PIL import Image

def main():
    print("test_switch: Walking to (2, 12)...")
    # We are at (1, 10)
    mgba.press_buttons(["Down", "sleep 500", "Down", "sleep 500", "Right", "sleep 500", "Up", "sleep 500"])
    time.sleep(3.0)
    
    # Check if we are at (2, 12)
    pos = mgba.get_coordinates()
    print(f"Standing position before toggling: {pos}")
    
    # Step 1: Press A
    print("Pressing A (1/4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img1 = mgba.take_screenshot()
    
    # Step 2: Press A
    print("Pressing A (2/4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img2 = mgba.take_screenshot()
    
    # Step 3: Press A
    print("Pressing A (3/4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img3 = mgba.take_screenshot()
    
    # Step 4: Press A
    print("Pressing A (4/4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img4 = mgba.take_screenshot()
    
    # Save the 4 switch screenshots
    Image.open(img1).save("mansion_switch_1.png")
    Image.open(img2).save("mansion_switch_2.png")
    Image.open(img3).save("mansion_switch_3.png")
    Image.open(img4).save("mansion_switch_4.png")
    print("Saved mansion_switch_1-4.png")
    
    # Try to walk back to (1, 10) and then Up
    print("Walking Left and Up...")
    mgba.press_buttons(["Left", "sleep 500", "Up", "sleep 500", "Up", "sleep 500", "Up", "sleep 500"])
    time.sleep(3.0)
    
    img5 = mgba.take_screenshot()
    Image.open(img5).save("mansion_switch_5.png")
    print("Saved mansion_switch_5.png")
    
    print(f"Final coordinates: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
