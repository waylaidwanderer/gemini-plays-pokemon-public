import mgba
import time

def surf_debug():
    print("Step 1: Pressing Start...")
    mgba.press_buttons(["Start"])
    time.sleep(1.0)
    img1 = mgba.take_screenshot()
    print(f"Screenshot after Start: {img1}")
    
    print("Step 2: Pressing Up 6 times to reset cursor...")
    mgba.press_buttons(["Up", "Up", "Up", "Up", "Up", "Up"])
    time.sleep(1.0)
    img2 = mgba.take_screenshot()
    print(f"Screenshot after Up 6: {img2}")
    
    print("Step 3: Pressing Down once...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    img3 = mgba.take_screenshot()
    print(f"Screenshot after Down: {img3}")
    
    print("Step 4: Pressing A to enter Pokemon menu...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img4 = mgba.take_screenshot()
    print(f"Screenshot after A: {img4}")
    
    print("Step 5: Pressing A to select SHELLBY...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img5 = mgba.take_screenshot()
    print(f"Screenshot after selecting SHELLBY: {img5}")

surf_debug()
