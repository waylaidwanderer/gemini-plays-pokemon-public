import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Walking to stairs at (7, 10) via Row 6 to warp to 2F...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Check if we warped to 2F (indicated by a change in coordinates to 2F landing, or we are back on 2F at y=11)
    # On 2F, (7, 11) is the landing. If we are on 2F, pos['y'] will be 11, but on 1F, we start at y=10.
    # So if pos['y'] == 11 and we just warped, we are on 2F!
    
    btn = None
    if pos['x'] == 16 and pos['y'] > 6:
        btn = 'Up'
    elif pos['y'] == 6 and pos['x'] > 7:
        btn = 'Left'
    elif pos['x'] == 7 and pos['y'] < 10:
        btn = 'Down'
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

print("Script execution completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
