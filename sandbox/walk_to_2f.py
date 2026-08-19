import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Walking to stairs at (7, 10) to warp to 2F...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # We warped to 2F (indicated by a change in coordinates to 2F landing, or we stepped onto 2F at y=11)
    if pos['x'] == 7 and pos['y'] == 11:
        # Wait, the landing on 2F is at (7, 11). But on 1F, (7, 11) is also open.
        # How do we know we are on 2F?
        # Let's check if we just stepped UP onto the stairs at (7, 10) and then the next step or state was 2F.
        pass

    btn = None
    if pos['y'] > 12:
        btn = 'Up'
    elif pos['y'] == 12 and pos['x'] > 7:
        btn = 'Left'
    elif pos['x'] == 7 and pos['y'] == 12:
        btn = 'Up'
    elif pos['x'] == 7 and pos['y'] == 10:
        # We are on the stairs tile!
        print("We are on 1F stairs (7, 10). Let's step onto it to warp to 2F.")
        btn = 'Up'
    else:
        # If we warped to 2F, our coordinates might change or we might be at (7, 11) facing DOWN.
        # Let's check if we are on 2F. On 2F, (7, 10) is the stairs.
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
        break

print("Script execution completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
