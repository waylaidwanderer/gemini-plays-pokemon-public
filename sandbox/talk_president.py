import mgba
import time

def check_textbox():
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        pos_after_b = mgba.get_coordinates()
        if pos_after_b != pos_before:
            # We moved after pressing B, meaning a textbox was indeed open!
            # Move back
            mgba.press_buttons(["Up"])
            time.sleep(0.3)
            return True
    else:
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
    return False

def try_talk_from(x, y, face_dir):
    pos = mgba.get_coordinates()
    curr_x, curr_y = pos['x'], pos['y']
    print(f"Moving to ({x}, {y}) from ({curr_x}, {curr_y})...")
    
    # Pathing via Row 9
    while curr_y != 9:
        btn = "Up" if 9 < curr_y else "Down"
        mgba.press_buttons([btn])
        time.sleep(0.3)
        curr_y = mgba.get_coordinates()['y']
        
    while curr_x != x:
        btn = "Left" if x < curr_x else "Right"
        mgba.press_buttons([btn])
        time.sleep(0.3)
        curr_x = mgba.get_coordinates()['x']
        
    while curr_y != y:
        btn = "Up" if y < curr_y else "Down"
        mgba.press_buttons([btn])
        time.sleep(0.3)
        curr_y = mgba.get_coordinates()['y']
        
    print(f"At ({x}, {y}). Facing {face_dir} and pressing A...")
    mgba.press_buttons([face_dir])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    if check_textbox():
        print(f"SUCCESS! Talked to President from ({x}, {y}) facing {face_dir}!")
        return True
    return False

# We start at (5, 7)
spots = [
    (5, 7, "Right"),
    (5, 6, "Right"),
    (7, 9, "Up"),
    (8, 9, "Up"),
    (10, 7, "Left"),
    (10, 6, "Left")
]

for x, y, d in spots:
    if try_talk_from(x, y, d):
        break
else:
    print("Could not talk to the President from any standard outer spot.")

screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
