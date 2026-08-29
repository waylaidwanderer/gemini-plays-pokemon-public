import mgba
import time
import shutil

def debug_mansion_switch():
    print(f"Starting debug from: {mgba.get_coordinates()}")
    
    # 1. Walk to (2, 12) facing Up
    steps = ["Down", "Down", "Right", "Up"]
    for step in steps:
        mgba.press_buttons([step])
        time.sleep(0.3)
        
    print(f"At switch standing position: {mgba.get_coordinates()}")
    
    # Press B to ensure no active dialog
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Take screenshot 1: Initial state
    img1 = mgba.take_screenshot()
    shutil.copy(img1, "mansion_switch_1.png")
    print("1. Initial state screenshot copied to mansion_switch_1.png")
    
    # Press A once: Interact
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img2 = mgba.take_screenshot()
    shutil.copy(img2, "mansion_switch_2.png")
    print("2. After 1st A (A secret switch!): mansion_switch_2.png")
    
    # Press A second time: Advance to YES/NO
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img3 = mgba.take_screenshot()
    shutil.copy(img3, "mansion_switch_3.png")
    print("3. After 2nd A (Press it?): mansion_switch_3.png")
    
    # Press A third time: Select YES
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img4 = mgba.take_screenshot()
    shutil.copy(img4, "mansion_switch_4.png")
    print("4. After 3rd A (Who wouldn't?): mansion_switch_4.png")
    
    # Press A fourth time: Dismiss
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img5 = mgba.take_screenshot()
    shutil.copy(img5, "mansion_switch_5.png")
    print("5. After 4th A (Dismissed): mansion_switch_5.png")

debug_mansion_switch()
