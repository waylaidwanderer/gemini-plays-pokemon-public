import mgba
import time

def use_dig():
    print("Using DIG...")
    # Open menu: Start, Down (to Pokemon), A
    mgba.press_buttons(["Start", "sleep 300", "Down", "sleep 100", "A", "sleep 500"])
    # In Pokemon menu, select TRUFFLE (Paras, usually second or third)
    # Let's check party order. SHELLBY is 1st. Paras is probably 2nd.
    # Let's press Down, A to select TRUFFLE.
    mgba.press_buttons(["Down", "sleep 100", "A", "sleep 500"])
    # Select DIG (Option 1 in TRUFFLE's menu, so A)
    mgba.press_buttons(["A", "sleep 1000"])
    # Wait for DIG animation and map transition to Cinnabar Island
    time.sleep(2)

def enter_mansion_and_walk():
    # We are at Cinnabar Island (11, 12).
    # Mansion entrance is at (6, 3).
    # Path to mansion entrance:
    # Walk Left 5 steps to col 6, Walk Up 9 steps to row 3.
    path_to_entrance = []
    for _ in range(5):
        path_to_entrance.append("Left")
        path_to_entrance.append("sleep 100")
    for _ in range(9):
        path_to_entrance.append("Up")
        path_to_entrance.append("sleep 100")
    print("Walking to Mansion entrance...")
    mgba.press_buttons(path_to_entrance)
    time.sleep(1)
    
    # Now we are inside Mansion 1F at (5, 27).
    # Let's walk to the lobby hallway at row 10:
    # Walk Up 17 steps to (5, 10).
    path_to_lobby = []
    for _ in range(17):
        path_to_lobby.append("Up")
        path_to_lobby.append("sleep 100")
    print("Walking to lobby at (5, 10)...")
    mgba.press_buttons(path_to_lobby)
    time.sleep(1)
    
    # From (5, 10), let's walk East to column 21:
    # Walk Right 16 steps to (21, 10).
    path_to_east = []
    for _ in range(16):
        path_to_east.append("Right")
        path_to_east.append("sleep 100")
    print("Walking East to (21, 10)...")
    mgba.press_buttons(path_to_east)
    time.sleep(1)
    
    # From (21, 10), walk Up 3 steps to (21, 7).
    path_to_gate = []
    for _ in range(3):
        path_to_gate.append("Up")
        path_to_gate.append("sleep 100")
    print("Walking Up to (21, 7)...")
    mgba.press_buttons(path_to_gate)
    time.sleep(1)
    
    # Take a screenshot to inspect
    scr = mgba.take_screenshot()
    print(f"Screenshot at (21, 7): {scr}")
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")

use_dig()
enter_mansion_and_walk()
