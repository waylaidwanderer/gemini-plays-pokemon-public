import mgba
import time

def step_strict(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    return "BLOCKED"

print("Starting floor verification...")
print("Current coordinates:", mgba.get_coordinates())

# 1. Step Down to (5, 11)
print("Stepping Down to (5, 11)...")
res = step_strict("Down", 5, 11)
print(f"Step Down result: {res}")

if res == "SUCCESS":
    # 2. Walk Right to (9, 11)
    path = [(6, 11), (7, 11), (8, 11), (9, 11)]
    success = True
    for x, y in path:
        if step_strict("Right", x, y) != "SUCCESS":
            print(f"Blocked at ({x}, {y})")
            success = False
            break
            
    if success:
        # 3. Step UP to (9, 10)
        print("Stepping UP to (9, 10)...")
        res_up = step_strict("Up", 9, 10)
        print(f"Step UP result: {res_up}")
        
        if res_up == "SUCCESS":
            # 4. Step Right to (10, 10)
            print("Stepping Right to (10, 10)...")
            res_right = step_strict("Right", 10, 10)
            print(f"Step Right to (10, 10) result: {res_right}")
            
            if res_right == "SUCCESS":
                # 5. Step UP to (10, 9)
                print("Stepping UP to (10, 9)...")
                res_up2 = step_strict("Up", 10, 9)
                print(f"Step UP to (10, 9) result: {res_up2}")
                
                if res_up2 == "SUCCESS":
                    print("VERDICT: WE ARE ON 3F WEST! (Since Column 10 is open)")
                else:
                    print("VERDICT: WE ARE ON 2F WEST! (Since (10, 9) is blocked by rubble)")
            else:
                print("VERDICT: WE ARE ON 2F WEST! (Since (10, 10) is blocked by rubble)")
else:
    print("Blocked at (5, 10)")
