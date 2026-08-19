import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Testing State A gates by walking to column 19 and going Down...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    btn = None
    if pos['x'] < 11 and pos['y'] == 11:
        btn = 'Right'
    elif pos['x'] == 11 and pos['y'] > 6:
        btn = 'Up'
    elif pos['y'] == 6 and pos['x'] < 19:
        btn = 'Right'
    elif pos['x'] == 19 and pos['y'] < 24:
        btn = 'Down'
    else:
        break
        
    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Check if we are blocked or in battle
        print("We are blocked or in battle!")
        run_from_battle()
        buttons_pressed += 6
        
        # If we are blocked by a permanent wall (not a battle), we can detect it if coordinates still don't change
        time.sleep(0.5)
        new_pos2 = mgba.get_coordinates()
        if new_pos2 == pos:
            print(f"CONFIRMED BLOCKED at {pos} trying to move {btn}!")
            break
            
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

print("State A Test completed. Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
