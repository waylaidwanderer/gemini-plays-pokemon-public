import mgba, time

def run_away_if_battle():
    mgba.press_buttons(["B", "Right", "Down", "A"])
    time.sleep(0.1)

print("Start pos:", mgba.get_coordinates())

# From (4, 31): walk Right to Column 33 at (33, 31)
for step in range(29):
    mgba.press_buttons(["Right"])
    time.sleep(0.05)
    run_away_if_battle()

cur = mgba.get_coordinates()
print("Reached:", cur)

if cur['x'] == 33 and cur['y'] == 31:
    print("Ascending Column 33 North...")
    for s in range(16):
        b = mgba.get_coordinates()
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
        run_away_if_battle()
        a = mgba.get_coordinates()
        print(f"Step {s+1}: {b} -> {a}")
        if a['y'] <= 16:
            print("REACHED ROW 16 HIGHWAY AT", a)
            break
