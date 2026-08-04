import mgba, time

def run_away_if_battle():
    mgba.press_buttons(["B", "Right", "Down", "A"])
    time.sleep(0.1)

print("Start pos:", mgba.get_coordinates())

cur = mgba.get_coordinates()

# From (37, 13), walk Left across Row 13, testing 'Down' at each column
for target_x in range(cur['x'], 0, -1):
    c = mgba.get_coordinates()
    while c['x'] > target_x:
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
        run_away_if_battle()
        c = mgba.get_coordinates()
        
    print(f"Testing Southbound step 'Down' at X={c['x']} (Y={c['y']})...")
    before = c
    mgba.press_buttons(["Down"])
    time.sleep(0.05)
    run_away_if_battle()
    after = mgba.get_coordinates()
    
    if after['y'] > before['y']:
        print(f"SUCCESS! Open Southbound gap found at X={c['x']}: {before} -> {after}")
        # Continue Down to Row 16
        while mgba.get_coordinates()['y'] < 16:
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
            run_away_if_battle()
            
        final_row = mgba.get_coordinates()
        print(f"Reached Row {final_row['y']} at X={final_row['x']}")
        if final_row['y'] >= 16:
            print("Reached Row 16 Highway! Walking East to Exit Warp at (37, 16)...")
            while mgba.get_coordinates()['x'] < 37:
                mgba.press_buttons(["Right"])
                time.sleep(0.05)
                run_away_if_battle()
            print("At Exit Warp tile:", mgba.get_coordinates())
            mgba.press_buttons(["Down"])
            time.sleep(0.1)
            print("Final Position after Exit:", mgba.get_coordinates())
            break
