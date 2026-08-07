import mgba

pos = mgba.get_coordinates()
print(f"Script starting at: {pos}")

# Walk Left along Row 34 testing Up at each step
for step in range(12):
    curr = mgba.get_coordinates()
    print(f"At {curr}, pressing Up...")
    mgba.press_buttons(["Up"])
    after_up = mgba.get_coordinates()
    if after_up != curr:
        print(f"TRANSITION DETECTED! Moved to {after_up} from {curr}")
        break
    print(f"Pressing Left...")
    mgba.press_buttons(["Left"])

final_pos = mgba.get_coordinates()
print(f"Final pos: {final_pos}")
