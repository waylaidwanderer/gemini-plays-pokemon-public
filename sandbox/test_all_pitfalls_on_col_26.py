import mgba
import time

def main():
    print("test_all_pitfalls_on_col_26: Starting walk down Column 26 from current...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # We are currently at (26, 6)
    # Let's walk Down to (26, 10) step-by-step
    for target_y in [7, 8, 9, 10]:
        pos_before = mgba.get_coordinates()
        print(f"Step DOWN to (26, {target_y})...")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        print(f"Landed at: {pos_after}")
        
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
            print(f"FELL THROUGH PITFALL!!! From {pos_before} to {pos_after}")
            return
            
        if pos_after['y'] != target_y:
            print(f"Blocked or deviated! Current: {pos_after}")
            break

if __name__ == "__main__":
    main()
