import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def test_steps():
    print("=== PROBING LOCAL WALKABILITY ON COLUMN 6 ===")
    
    pos = get_pos()
    print("Start position:", pos)
    if pos is None:
        return
        
    # 1. Try to walk Right to (6, 23)
    print("Walking Right...")
    bridge.press_buttons(["Right"])
    time.sleep(0.5)
    pos = get_pos()
    print("Position after Right:", pos)
    if pos != (6, 23):
        print("Failed to walk Right!")
        return
        
    # 2. Try to walk Down to (6, 24)
    print("Walking Down...")
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    pos = get_pos()
    print("Position after Down:", pos)
    
    # 3. Try to walk Down to (6, 25)
    print("Walking Down...")
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    pos = get_pos()
    print("Position after Down 2:", pos)
    
    # 4. Try to walk Down to (6, 26)
    print("Walking Down...")
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    pos = get_pos()
    print("Position after Down 3:", pos)

if __name__ == "__main__":
    test_steps()
