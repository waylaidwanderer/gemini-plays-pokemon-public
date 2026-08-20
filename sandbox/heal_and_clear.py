import mgba
import time

def close_menus():
    print("Closing menus...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def exit_mart():
    print("Exiting Poké Mart...")
    # Walk Down until we are outside (coordinates change to Cinnabar Island)
    # The Mart exit is around row 7 or 8.
    for i in range(5):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    
    time.sleep(1.5) # wait for map transition
    pos = mgba.get_coordinates()
    print("Outside coordinates:", pos)
    return pos

def walk_to_center_and_enter(pos):
    if pos['y'] != 12 and pos['y'] != 11:
        # If we are not at the expected y coordinate, try to move to row 12
        print("Adjusting Y to 12...")
        if pos['y'] < 12:
            for _ in range(12 - pos['y']):
                mgba.press_buttons(["Down"])
                time.sleep(0.5)
        elif pos['y'] > 12:
            for _ in range(pos['y'] - 12):
                mgba.press_buttons(["Up"])
                time.sleep(0.5)
        pos = mgba.get_coordinates()

    # Now we are at row 12. Walk Left to column 11.
    dx = pos['x'] - 11
    print(f"Walking Left {dx} steps to Pokémon Center...")
    for _ in range(dx):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print("At Pokémon Center door:", pos)
    
    # Enter Center
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # wait for warp
    
    pos_center = mgba.get_coordinates()
    print("Inside Center coordinates:", pos_center)
    return pos_center

def heal_pokemon(pos_center):
    # We land inside the Pokémon Center at (3, 8) or similar.
    # Move horizontally to column 3.
    if pos_center['x'] != 3:
        dir_x = "Left" if pos_center['x'] > 3 else "Right"
        for _ in range(abs(pos_center['x'] - 3)):
            mgba.press_buttons([dir_x])
            time.sleep(0.5)
            
    # Move vertically to row 4 or 5 (Nurse Joy is at row 3, counter is at row 4)
    pos_center = mgba.get_coordinates()
    dy = pos_center['y'] - 4
    print(f"Walking Up {dy} steps to Nurse Joy...")
    for _ in range(dy):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
    pos_final = mgba.get_coordinates()
    print("At Nurse Joy counter:", pos_final)
    
    # Talk to Nurse Joy (we are facing Up)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Advance dialogue
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
    print("Waiting for healing jingle...")
    time.sleep(4.5)
    
    # Dismiss post-healing text
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
    # Extra B press to ensure dialogue is completely closed
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print("Healing completed successfully!")
    mgba.take_screenshot()

def main():
    close_menus()
    pos = exit_mart()
    pos_center = walk_to_center_and_enter(pos)
    heal_pokemon(pos_center)

if __name__ == "__main__":
    main()
