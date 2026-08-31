import mgba
import time

def test_7_10():
    # Currently at (5, 12)
    # Path to (7, 10):
    # 1. UP to (5, 10)
    # 2. Right to (7, 10)
    print("Walking to (7, 10)...")
    path = [(5, 11), (5, 10), (6, 10), (7, 10)]
    for step in path:
        pos = mgba.get_coordinates()
        print(f"Current: {pos} | Heading to {step}")
        if step[0] > pos['x']: dir = "Right"
        elif step[0] < pos['x']: dir = "Left"
        elif step[1] > pos['y']: dir = "Down"
        else: dir = "Up"
        mgba.press_buttons([dir])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Moved to: {new_pos}")
        
    # Face UP at (7, 10) and press UP to trigger warp
    print("At (7, 10). Pressing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    
    final_pos = mgba.get_coordinates()
    print("Final position after warp attempt:", final_pos)

if __name__ == "__main__":
    test_7_10()
