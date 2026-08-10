import mgba
import time

print("Starting safe run_out_of_steps with 100 actions max...")

# 25 cycles = 25 Left + 25 Right = 50 steps.
# Plus 50 sleep actions = 100 total actions! This is the absolute limit.
actions = []
for i in range(25):
    actions.append("Left")
    actions.append("sleep 150")
    actions.append("Right")
    actions.append("sleep 150")

# We want to consume 204 steps.
# 4 iterations of 50 steps = 200 steps!
for chunk in range(4):
    print(f"Executing chunk {chunk+1}/4...")
    mgba.press_buttons(actions)
    time.sleep(1) # Let the emulator settle

print("Finished safe run_out_of_steps.")
