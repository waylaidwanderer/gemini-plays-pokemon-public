import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# Target: Exit at the bottom-right of 1F (around x=26, y=27)
# Let's walk Right to column 12, then Down column 12 as far as possible
print("Walking to exit...")
steps = ["Right", "Right", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down"]

for i, s in enumerate(steps):
    pos = mgba.get_coordinates()
    print(f"Step {i+1}: At {pos}, pressing {s}")
    mgba.press_buttons([s])
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print("Failed to move, checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
