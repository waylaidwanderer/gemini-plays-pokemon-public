import mgba
import time

def print_pos(label):
    time.sleep(0.1)
    print(f"{label}: {mgba.get_coordinates()}")

# Start
print_pos("Start at B3F")

# Walk Right to (4, 13)
for i in range(3):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    print_pos(f"Step Right {i+1}")

# Walk Down to (4, 14)
mgba.press_buttons(["Down"])
time.sleep(0.3)
print_pos("Step Down to row 14")

