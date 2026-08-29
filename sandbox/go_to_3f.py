import mgba
import time
import test_gate
import importlib

def main():
    # 1. Escape battle
    print("go_to_3f_finish: Escaping Grimer...")
    importlib.reload(test_gate)
    test_gate.handle_battle_escape()
    
    pos = mgba.get_coordinates()
    print(f"go_to_3f_finish: Overworld position: {pos}")
    
    # 2. Walk Right to (7, 11)
    # We are at (5, 11) or close. Let's make sure we walk to (7, 11)
    while pos['x'] < 7:
        pos_after = test_gate.move_safe_battle("Right", pos['x'] + 1, 11)
        if not pos_after:
            print("Failed to move Right.")
            return
        pos = mgba.get_coordinates()
        
    # 3. Walk UP onto the stairs at (7, 10) to warp UP to 3F West!
    print("go_to_3f_finish: Stepping onto stairs at (7, 10) to warp UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"go_to_3f_finish: Arrived on 3F! Position: {pos}")

if __name__ == "__main__":
    main()
