import mgba

print("--- Starting Systematic Route 8 Door Probe ---")
pos = mgba.get_coordinates()
print(f"Initial Position: {pos}")

# Ensure we are at y=14
while pos['y'] > 14:
    mgba.press_buttons(["Up"])
    pos = mgba.get_coordinates()

# Walk east along Row 14 and test Down at each tile
doors_found = []

for x in range(pos['x'], 53):
    curr = mgba.get_coordinates()
    if curr['x'] < x:
        mgba.press_buttons(["Right"])
        curr = mgba.get_coordinates()
        if curr['x'] != x:
            print(f"Blocked moving right to x={x}, current pos: {curr}")
            break
            
    print(f"At x={curr['x']}, y={curr['y']}. Testing Down...")
    mgba.press_buttons(["Down"])
    after = mgba.get_coordinates()
    
    if after['x'] != curr['x'] or after['y'] != curr['y']:
        print(f"*** POSITION CHANGE AT x={curr['x']}! New Pos: {after} ***")
        mgba.take_screenshot()
        doors_found.append((curr['x'], curr['y'], after))
        if after['y'] != curr['y'] + 1 or after['x'] != curr['x']:
            print("MAP TRANSITION DETECTED!")
            break
        else:
            print(f"Stepped onto y={after['y']}. Testing Down again...")
            mgba.press_buttons(["Down"])
            after2 = mgba.get_coordinates()
            if after2['x'] != after['x'] or after2['y'] != after['y']:
                print(f"*** SECOND DOWN PASSED AT x={after['x']}! New Pos: {after2} ***")
                mgba.take_screenshot()
                doors_found.append((after['x'], after['y'], after2))
                break
            else:
                mgba.press_buttons(["Up"])

print(f"Probe Finished. Doors found: {doors_found}")
