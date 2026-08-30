import mgba
import time

def probe_switch():
    print("Facing Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    print("Pressing A (1)...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img1 = mgba.take_screenshot()
    print("Captured screenshot 1")
    
    print("Pressing A (2)...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img2 = mgba.take_screenshot()
    print("Captured screenshot 2")
    
    print("Pressing A (3)...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img3 = mgba.take_screenshot()
    print("Captured screenshot 3")

    print("Pressing A (4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img4 = mgba.take_screenshot()
    print("Captured screenshot 4")

probe_switch()
print("Probing complete.")
