import mgba
import time
import shutil

def test_statue_dialogue():
    print("Starting dialogue test...")
    # Ensure facing Up
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # 1st A
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    img = mgba.take_screenshot()
    shutil.copy(img, "mansion_switch_1.png")
    print("mansion_switch_1.png saved.")
    
    # 2nd A
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    img = mgba.take_screenshot()
    shutil.copy(img, "mansion_switch_2.png")
    print("mansion_switch_2.png saved.")
    
    # 3rd A
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    img = mgba.take_screenshot()
    shutil.copy(img, "mansion_switch_3.png")
    print("mansion_switch_3.png saved.")
    
    # 4th A
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    img = mgba.take_screenshot()
    shutil.copy(img, "mansion_switch_4.png")
    print("mansion_switch_4.png saved.")

test_statue_dialogue()
