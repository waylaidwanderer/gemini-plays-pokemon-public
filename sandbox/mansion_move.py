import mgba
import time

def use_dig():
    print("Using DIG to exit to Cinnabar Island...")
    # Open menu: Start, Down (to Pokemon), A
    mgba.press_buttons(["Start", "sleep 300", "Down", "sleep 100", "A", "sleep 500"])
    # TRUFFLE (Paras) is in the 6th slot. Press Down 5 times, then A.
    mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "A", "sleep 500"])
    # Select DIG (Option 1, so press A)
    mgba.press_buttons(["A", "sleep 1000"])
    time.sleep(2)

def walk_to_mansion_and_climb():
    # We are at Cinnabar Island (11, 12).
    # Walk Left 5 steps to column 6: (11,12) -> (6,12)
    path_to_col6 = ["Left", "sleep 100"] * 5
    mgba.press_buttons(path_to_col6)
    time.sleep(0.5)

    # From (6,12), we want to walk to the Mansion entrance at (6,3).
    # But Cinnabar Lab entrance is at (6,9). We must bypass it!
    # Bypass path: Down 1 step to row 13, Left 1 step to column 5, Up 10 steps to (5,3), Right 1 step to (6,3).
    bypass_lab = [
        "Down", "sleep 100",
        "Left", "sleep 100",
    ]
    for _ in range(10):
        bypass_lab.append("Up")
        bypass_lab.append("sleep 100")
    bypass_lab.append("Right")
    bypass_lab.append("sleep 100")
    bypass_lab.append("Up") # Step into Mansion entrance at (6,3)
    bypass_lab.append("sleep 300")
    
    print("Bypassing Lab and entering Mansion...")
    mgba.press_buttons(bypass_lab)
    time.sleep(1)

    # Now we are inside Mansion 1F at (5, 27).
    # Let's walk Up 17 steps to stairs at (5,10) to warp to 2F.
    print("Climbing to 2F...")
    path_to_2f = ["Up", "sleep 100"] * 17
    mgba.press_buttons(path_to_2f)
    time.sleep(1)

    # Now we are on 2F at (5, 11).
    # Walk Up 1 step to stairs at (5,10) to warp to 3F.
    print("Climbing to 3F...")
    path_to_3f = ["Up", "sleep 300"]
    mgba.press_buttons(path_to_3f)
    time.sleep(1)

def toggle_switch_and_fall():
    # Now we are on 3F at (5, 11).
    # We need to walk Left to (2, 12), face UP, and toggle the switch on Mewtwo statue at (2, 11).
    # Path: Left 3 steps, Down 1 step, Up (to face UP).
    print("Walking to 3F switch...")
    path_to_switch = [
        "Left", "sleep 100",
        "Left", "sleep 100",
        "Left", "sleep 100",
        "Down", "sleep 100",
        "Up", "sleep 300",
        "A", "sleep 500",  # Toggle switch to State B
        "A", "sleep 500",
        "A", "sleep 500",
    ]
    mgba.press_buttons(path_to_switch)
    time.sleep(1)

    # From (2, 12) on 3F, we walk east to column 12, north to row 7, east to column 21, and north through the open gate at (21,5) to the northeast room.
    # Path:
    # 1. Right 10 steps to (12, 12)
    # 2. Up 5 steps to (12, 7)
    # 3. Right 9 steps to (21, 7)
    # 4. Up 2 steps to (21, 5) (through open gate)
    # 5. Right 3 steps to (24, 5) (the pit)
    print("Walking to 3F pit...")
    path_to_pit = []
    for _ in range(10):
        path_to_pit.append("Right")
        path_to_pit.append("sleep 100")
    for _ in range(5):
        path_to_pit.append("Up")
        path_to_pit.append("sleep 100")
    for _ in range(9):
        path_to_pit.append("Right")
        path_to_pit.append("sleep 100")
    path_to_pit.append("Up")
    path_to_pit.append("sleep 100")
    path_to_pit.append("Up")
    path_to_pit.append("sleep 100")
    path_to_pit.append("Right")
    path_to_pit.append("sleep 100")
    path_to_pit.append("Right")
    path_to_pit.append("sleep 100")
    path_to_pit.append("Right")
    path_to_pit.append("sleep 500") # step into pit and fall to 1F

    mgba.press_buttons(path_to_pit)
    time.sleep(2)

def walk_to_b1f():
    # Now we should have landed on 1F at (22, 7) in State B.
    # We walk Left 3 steps to (19, 7), Down 2 steps to (19, 9) (through open gate), Right 2 steps to (21, 9), and Down 15 steps to (21, 24).
    # Then step Left 1 step onto B1F stairs.
    print("Walking to B1F stairs on 1F...")
    path_to_b1f = [
        "Left", "sleep 100",
        "Left", "sleep 100",
        "Left", "sleep 100",
        "Down", "sleep 100",
        "Down", "sleep 100",
        "Right", "sleep 100",
        "Right", "sleep 100",
    ]
    for _ in range(15):
        path_to_b1f.append("Down")
        path_to_b1f.append("sleep 100")
    path_to_b1f.append("Left")
    path_to_b1f.append("sleep 300")

    mgba.press_buttons(path_to_b1f)
    time.sleep(1)

    pos = mgba.get_coordinates()
    print(f"Coordinates on B1F: {pos}")
    scr = mgba.take_screenshot()
    print(f"Screenshot on B1F: {scr}")

use_dig()
walk_to_mansion_and_climb()
toggle_switch_and_fall()
walk_to_b1f()
