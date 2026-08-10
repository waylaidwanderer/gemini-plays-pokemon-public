import mgba
import time

print("Starting safe run_out_of_steps...")

# We will generate a list of 100 button presses alternating Left and Right with sleep 150.
# Since we are on normal grass at (9, 24) and (8, 24), no wild battles can occur!
actions = []
for i in range(50):
    actions.append("Left")
    actions.append("sleep 150")
    actions.append("Right")
    actions.append("sleep 150")

# Each list passed to press_buttons has up to 100 actions max.
# We can do this in chunks.
# Let's run a loop in Python to execute this several times.
# We have 404 steps left.
# 50 Left-Right cycles = 100 steps.
# If we do 4 iterations of 50 cycles, that is 400 steps!
# Let's run 4 iterations.
for chunk in range(4):
    print(f"Executing chunk {chunk+1}/4...")
    mgba.press_buttons(actions)
    time.sleep(1) # Sleep to let the emulator settle

print("Finished safe run_out_of_steps.")
