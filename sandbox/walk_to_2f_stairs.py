import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating from (1, 11) to 2F stairs to warp back to 1F...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Check if we warped to 1F (1F position on stairs is (7, 10) or we are at (7, 11) on 1F)
    # On 1F, (7, 10) is the stairs.
    
    btn = None
    if pos['x'] == 1 and pos['y'] < 13:
        btn = 'Down'
    elif pos['y'] == 13 and pos['x'] < 8:
        btn = 'Right'
    elif pos['x'] == 8 and pos['y'] > 10:
        btn = 'Up'
    elif pos['y'] == 10 and pos['x'] > 7:
        btn = 'Left'
    elif pos['x'] == 7 and pos['y'] == 10:
        print("At 2F stairs! Stepping onto them to warp to 1F...")
        btn = 'Up'
    else:
        print("Warp check...")
        break
        
    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        run_from_battle()
        buttons_pressed += 6
        
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

print("Script completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
